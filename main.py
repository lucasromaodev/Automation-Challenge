from browser import init_browser
from invoice_downloader import download_invoices_paginated
from ocr_processor import extract_invoice_data
from csv_generator import generate_csv
from utils import get_due_invoices
from cleanup import cleanup_jpg_files
from upload_csv import upload_csv

def main():
    print("Iniciando automação...")

    # Limpa arquivos .jpg antigos antes de começar
    cleanup_jpg_files()

    driver = init_browser()
    print("Navegador iniciado e site carregado.")

    due_invoices = get_due_invoices(driver)
    print(f"Total de faturas com vencimento hoje ou anterior: {len(due_invoices)}")

    invoice_files = download_invoices_paginated(driver, due_invoices)
    print(f"Faturas baixadas: {len(invoice_files)}")

    extracted_data = extract_invoice_data(invoice_files)
    print(f"Dados extraídos de {len(extracted_data)} faturas.")

    generate_csv(extracted_data)
    print("CSV gerado com sucesso!")

    upload_csv(driver)
    print("CSV enviado com sucesso!")

    driver.quit()
    print("Automação finalizada com sucesso.")

if __name__ == "__main__":
    main()
