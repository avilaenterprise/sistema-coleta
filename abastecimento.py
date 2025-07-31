import sqlite3
from datetime import datetime
import streamlit as st
import pandas as pd

# ====== 1. BANCO DE DADOS E FUNÇÕES ======

def criar_tabelas():
    conn = sqlite3.connect('abastecimento.db')
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS abastecimentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tag_rfid TEXT NOT NULL,
        veiculo TEXT NOT NULL,
        operador TEXT NOT NULL,
        datahora TEXT DEFAULT (datetime('now')),
        litros REAL NOT NULL,
        tanque TEXT NOT NULL,
        km_inicial INTEGER NOT NULL,
        km_final INTEGER,
        media_kml REAL,
        status_sap TEXT DEFAULT 'Pendente',
        solicitacao_compra TEXT DEFAULT 'Pendente',
        observacoes TEXT
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS estoque_tanques (
        tanque TEXT PRIMARY KEY,
        quantidade_atual REAL NOT NULL,
        ultima_atualizacao TEXT
    );
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS solicitacoes_compra (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tanque TEXT NOT NULL,
        quantidade REAL NOT NULL,
        datahora TEXT DEFAULT (datetime('now')),
        status TEXT DEFAULT 'Pendente'
    );
    """)
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect('abastecimento.db', check_same_thread=False)

def inicializar_estoque_tanque(tanque_nome, quantidade_litros):
    conn = get_connection()
    cur = conn.cursor()
    datahora = datetime.now().isoformat(timespec='seconds')
    cur.execute("""
        INSERT OR REPLACE INTO estoque_tanques (tanque, quantidade_atual, ultima_atualizacao)
        VALUES (?, ?, ?)
    """, (tanque_nome, quantidade_litros, datahora))
    conn.commit()
    conn.close()

def registrar_abastecimento(tag_rfid, veiculo, operador, litros, tanque, km_inicial, km_final=None, observacoes=None):
    conn = get_connection()
    cur = conn.cursor()a
    datahora = datetime.now().isoformat(timespec='seconds')
    km_rodado = km_final - km_inicial if km_final and km_inicial else None
    media_kml = (km_rodado / litros) if km_rodado and litros > 0 else None
    cur.execute("""
        INSERT INTO abastecimentos
        (tag_rfid, veiculo, operador, datahora, litros, tanque, km_inicial, km_final, media_kml, status_sap, solicitacao_compra, observacoes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        tag_rfid,
        veiculo,
        operador,
        datahora,
        litros,
        tanque,
        km_inicial,
        km_final,
        media_kml,
        "Pendente",
        "Pendente",
        observacoes
    ))
    cur.execute("""
        UPDATE estoque_tanques
        SET quantidade_atual = quantidade_atual - ?, ultima_atualizacao = ?
        WHERE tanque = ?
    """, (litros, datahora, tanque))
    cur.execute("""
        INSERT INTO solicitacoes_compra (tanque, quantidade, datahora, status)
        VALUES (?, ?, ?, ?)
    """, (tanque, litros, datahora, "Pendente"))
    conn.commit()
    conn.close()

def listar_abastecimentos(limite=50):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, tag_rfid, veiculo, operador, datahora, litros, tanque, km_inicial, km_final, media_kml, status_sap, solicitacao_compra, observacoes
        FROM abastecimentos
        ORDER BY datahora DESC
        LIMIT ?
    """, (limite,))
    rows = cur.fetchall()
    conn.close()
    return rows

def get_estoque():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT tanque, quantidade_atual, ultima_atualizacao FROM estoque_tanques")
    rows = cur.fetchall()
    conn.close()
    return rows

# ====== 2. INICIALIZAÇÃO AUTOMÁTICA ======
criar_tabelas()
try:
    if not get_estoque():
        inicializar_estoque_tanque("Principal", 10000)
except:
    inicializar_estoque_tanque("Principal", 10000)

# ====== 3. STREAMLIT DASHBOARD ======

st.set_page_config(page_title="Dashboard de Abastecimento", page_icon="⛽", layout="wide")
st.title("⛽ Dashboard de Abastecimento Premium")

with st.sidebar:
    st.header("Novo Abastecimento")
    with st.form(key="abastecimento_form"):
        tag_rfid = st.text_input("TAG RFID", max_chars=50)
        veiculo = st.text_input("Veículo (Placa ou código)")
        operador = st.text_input("Operador (Nome)")
        litros = st.number_input("Litros abastecidos", min_value=0.0, step=0.1)
        tanque = st.text_input("Tanque", value="Principal")
        km_inicial = st.number_input("KM Inicial", min_value=0)
        km_final = st.number_input("KM Final", min_value=0)
        observacoes = st.text_area("Observações (opcional)")
        submitted = st.form_submit_button("Registrar Abastecimento")
        if submitted:
            if not tag_rfid or not veiculo or not operador or litros == 0 or not tanque or km_inicial == 0:
                st.error("Preencha todos os campos obrigatórios!")
            else:
                registrar_abastecimento(
                    tag_rfid, veiculo, operador, litros, tanque, km_inicial, km_final if km_final != 0 else None, observacoes
                )
                st.success("Abastecimento registrado com sucesso!")

st.markdown("## 📝 Abastecimentos Recentes")
abastecimentos = listar_abastecimentos(50)
df = pd.DataFrame(abastecimentos, columns=[
    "ID", "TAG RFID", "Veículo", "Operador", "Data/Hora", "Litros", "Tanque",
    "KM Inicial", "KM Final", "Média KM/L", "Status SAP", "Solicitação Compra", "Observações"
])
st.dataframe(df, use_container_width=True)

st.markdown("## 📊 Indicadores Gerais")
col1, col2, col3, col4 = st.columns(4)
if not df.empty:
    col1.metric("Total Litros", f"{df['Litros'].sum():,.2f} L")
    col2.metric("Abastecimentos", f"{len(df)}")
    medias = df["Média KM/L"].dropna()
    col3.metric("Média KM/L", f"{medias.mean():.2f}" if not medias.empty else "N/A")
    col4.metric("Veículos Únicos", df["Veículo"].nunique())
else:
    st.info("Nenhum abastecimento registrado ainda.")

st.markdown("## 🛢️ Estoque de Tanques")
estoque = get_estoque()
df_estoque = pd.DataFrame(estoque, columns=["Tanque", "Quantidade Atual (L)", "Última Atualização"])
st.dataframe(df_estoque, use_container_width=True)

st.markdown("###### Desenvolvido por Avila DevOps – Solução Premium 🚀")
