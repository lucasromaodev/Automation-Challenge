import os
import requests
from selenium.webdriver.common.by import By
from datetime import datetime
from utils import is_due_date_passed


def download_invoices(driver, due_invoices):
    invoice_files = []
    for invoice in due_invoices:
        # Localiza o botão de download da fatura
        download_button = driver.find_element(By.XPATH, f"//tr[td[text()='{invoice['ID']}']]//a")
        invoice_url = download_button.get_attribute('href')

        # Faz o download da imagem da fatura
        response = requests.get(invoice_url)
        file_name = f"invoice_{invoice['ID']}.jpg"
        with open(file_name, 'wb') as f:
            f.write(response.content)
        invoice_files.append({'file': file_name, 'ID': invoice['ID'], 'Due Date': invoice['Due Date']})
    return invoice_files
