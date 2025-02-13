import matplotlib.pyplot as plt
from fpdf import FPDF

class Relatorios:
    def gerar_grafico(self, dados):
        departamentos = list(dados.keys())
        custos = list(dados.values())
        plt.pie(custos, labels=departamentos, autopct='%1.1f%%')
        plt.title("Custos por Departamento")
        plt.show()

    def gerar_pdf(self, dados):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for linha in dados:
            pdf.cell(200, 10, txt=linha, ln=True)
        pdf.output("relatorio.pdf")