#Entrada de dados

projeto = input("Digite a descrição do projeto: ")
horas_estimadas = input("Digite o total de horas estimadas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo_estimado = input("Digite o prazo estimado: ")

#Cálculo do valor total estimado
valor_total_estimado = int(horas_estimadas) * int(valor_hora)

#Criando um arquivo PDF
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

#Utilizando o template
pdf.image("template.png", x=0, y=0 )

#Inserindo os dados do projeto
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_estimadas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo_estimado)
pdf.text(115, 205, str(valor_total_estimado))

#Salvando o arquivo
pdf.output("orçamento.pdf")
print("Orçamento gerado com sucesso!")