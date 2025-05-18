import os
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click_pagination_button(driver, page_number):
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.presence_of_element_located(
        (By.XPATH, f"//a[contains(@class, 'paginate_button') and text()='{page_number}']")
    ))

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    wait.until(EC.element_to_be_clickable(button))
    driver.execute_script("arguments[0].click();", button)
    print(f"[INFO] Botão da página {page_number} clicado via JS com sucesso.")

def download_invoices_paginated(driver, due_invoices):
    try:
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        print("[INFO] Troca para iframe feita no download")
    except Exception:
        print("[INFO] Nenhum iframe encontrado no download, continuando no contexto principal")

    invoice_files = []

    for page in range(1, 4):  # páginas 1, 2 e 3
        click_pagination_button(driver, page)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr"))
        )

        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        for invoice in due_invoices:
            found = False
            for row in rows:
                try:
                    id_cell = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)")
                    id_text = id_cell.text.strip()
                    if id_text == invoice['ID']:
                        download_link = row.find_element(By.CSS_SELECTOR, "a")
                        invoice_url = download_link.get_attribute('href')

                        response = requests.get(invoice_url)
                        file_name = f"invoice_{invoice['ID']}.jpg"
                        with open(file_name, 'wb') as f:
                            f.write(response.content)
                        invoice_files.append({
                            'file': file_name,
                            'ID': invoice['ID'],
                            'Due Date': invoice['Due Date']
                        })
                        print(f"[INFO] Fatura {invoice['ID']} baixada com sucesso na página {page}.")
                        found = True
                        break
                except Exception as e:
                    print(f"[ERRO] Falha ao processar linha para fatura {invoice['ID']} na página {page}: {e}")
            if not found:
                print(f"[WARN] Fatura {invoice['ID']} não encontrada na página {page}.")

    driver.switch_to.default_content()
    return invoice_files
