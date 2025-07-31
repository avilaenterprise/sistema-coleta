import streamlit as st
import sqlite3
from datetime import datetime

# Funções de banco
def get_connection():
    return sqlite3.connect('abastecimento.db', check_same_thread=False)

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

def registrar_abastecimento(tag_rfid, veiculo, operador, litros, tanque, km_inicial, km_final, observacoes):
    conn = get_connection()
    cur = conn.cursor()
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
    conn.commit()
    conn.close()

# Layout Streamlit
st.set_page_config(page_title="Dashboard de Abastecimento", page_icon="⛽", layout="wide")
st.title("⛽ Dashboard de Abastecimento Premium")

st.sidebar.header("Novo Abastecimento")

with st.sidebar.form(key="abastecimento_form"):
    tag_rfid = st.text_input("TAG RFID", max_chars=50)
    veiculo = st.text_input("Veículo (Placa ou código)")
    operador = st.text_input("Operador (Nome)")
    litros = st.number_input("Litros abastecidos", min_value=0.0, s
