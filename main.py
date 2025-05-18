from browser import init_browser
from invoice_downloader import download_invoices
from ocr_processor import extract_invoice_data
from csv_generator import generate_csv
from utils import get_due_invoices

def main():
    print("Iniciando automação...")

    driver = init_browser()
    print("Navegador iniciado e site carregado.")

    # Coleta das faturas vencidas ou que vencem hoje
    due_invoices = get_due_invoices(driver)
    print(f"Total de faturas com vencimento hoje ou anterior: {len(due_invoices)}")

    # Baixa as imagens das faturas
    invoice_files = download_invoices(driver, due_invoices)
    print(f"Faturas baixadas: {len(invoice_files)}")

    # Corrigido: extrai apenas os caminhos dos arquivos das faturas
    extracted_data = extract_invoice_data(invoice_files)
    print(f"Dados extraídos de {len(extracted_data)} faturas.")

    # Gera o CSV com os dados extraídos
    generate_csv(extracted_data)
    print("CSV gerado com sucesso!")

    # Finaliza o navegador
    driver.quit()
    print("Automação finalizada com sucesso.")

if __name__ == "__main__":
    main()
