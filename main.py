from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import datetime

# Configurar o ambiente Jinja2 para carregar templates de um diretório específico
env = Environment(loader=FileSystemLoader("."))  # Use o diretório atual

# Carregar o template HTML
template = env.get_template("template.html")


def get_date():
    today = datetime.datetime.now()

    months = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }

    # Formata a data no formato desejado
    data_formatada = (
        f"{today.day} de {months[today.month]} de {today.year}"
    )

    return data_formatada


def render_and_save(vaga, empresa):
    data = get_date()

    dados = {"vaga": vaga, "empresa": empresa, "data": data}
    # Renderize o template com os dados
    html_output = template.render(dados)

    file = "output.html"
    # Salve o HTML em um arquivo (opcional)
    with open(file, "w", encoding="utf-8") as output_file:
        output_file.write(html_output)

    return file


def generate_pdf(file):
    pdf_file = "output.pdf"

    HTML(string=open(file, "rb").read()).write_pdf(pdf_file)


file = render_and_save("Estagiário", "Osklen")
generate_pdf(file)
