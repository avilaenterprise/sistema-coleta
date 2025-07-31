import streamlit as st
from fpdf import FPDF
import io

# --- Dados do exemplo ---
remetente_cnpj = "08.652.441/0001-80"
destinatario_cnpj = "80.342.330/0001-02"
frete_tipo = "CIF"
valor_nf = "R$ 2.615,55"
peso = "17 kg 300 g"
medidas = ["24 x 44 x 51 cm", "55 x 32 x 32 cm", "50 x 36 x 42 cm"]

class CotacaoPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 12, "Solicitação de Cotação de Frete", align="C", ln=True)
        self.ln(6)
        self.set_draw_color(0, 102, 204)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def corpo(self, dados):
        self.set_font("Arial", "", 12)
        self.cell(50, 8, "CNPJ Remetente:", 0, 0)
        self.cell(0, 8, dados['remetente_cnpj'], 0, 1)
        self.cell(50, 8, "CNPJ Destino:", 0, 0)
        self.cell(0, 8, dados['destinatario_cnpj'], 0, 1)
        self.cell(50, 8, "Tipo de Frete:", 0, 0)
        self.cell(0, 8, dados['frete_tipo'], 0, 1)
        self.cell(50, 8, "Valor da NF:", 0, 0)
        self.cell(0, 8, dados['valor_nf'], 0, 1)
        self.cell(50, 8, "Peso Total:", 0, 0)
        self.cell(0, 8, dados['peso'], 0, 1)
        self.cell(50, 8, "Medidas:", 0, 1)
        for m in dados['medidas']:
            self.cell(60, 8, "", 0, 0)
            self.cell(0, 8, m, 0, 1)
        self.ln(4)
        self.multi_cell(0, 8, "Solicito cotação de frete para o transporte da mercadoria acima. Favor informar o valor, prazo de entrega e condições comerciais.")
        self.ln(8)
        self.set_font("Arial", "B", 12)
        self.cell(0, 8, "Atenciosamente,", ln=1)
        self.set_font("Arial", "", 12)
        self.cell(0, 8, "Nícolas Rosa Ávila Barros")
        self.cell(0, 8, "Avila Transportes", ln=1)
        self.cell(0, 8, "E-mail: avila@avilatransportes.com.br | WhatsApp: (xx) xxxxx-xxxx")

# Gera o PDF em memória
pdf = CotacaoPDF()
pdf.add_page()
dados = {
    "remetente_cnpj": remetente_cnpj,
    "destinatario_cnpj": destinatario_cnpj,
    "frete_tipo": frete_tipo,
    "valor_nf": valor_nf,
    "peso": peso,
    "medidas": medidas
}
pdf.corpo(dados)
pdf_buffer = io.BytesIO()
pdf.output(pdf_buffer)
pdf_buffer.seek(0)

st.markdown("### 📝 Solicitação de Cotação de Frete pronta!")
st.success("Clique abaixo para baixar o PDF da sua cotação.")

st.download_button(
    label="📄 Baixar Solicitação de Cotação (PDF)",
    data=pdf_buffer,
    file_name="solicitacao_cotacao_avila.pdf",
    mime="application/pdf"
)
