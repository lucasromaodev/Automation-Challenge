from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def is_due_date_passed(due_date_str):
    try:
        due_date = datetime.strptime(due_date_str, '%d-%m-%Y').date()
        today = datetime.today().date()
        return due_date <= today
    except Exception as e:
        print(f"[ERRO] Falha ao processar data '{due_date_str}': {e}")
        return False

def get_due_invoices(driver):

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr")))

    invoices = []
    paginacao = driver.find_elements(By.CLASS_NAME, "paginate_button")

    total_pages = len(paginacao) - 2  # -2 para tirar previous e next

    for page_num in range(1, total_pages + 1):
        print(f"[INFO] Processando página {page_num}...")

        # Espera tabela aparecer
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr")))
        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        print(f"[INFO] Total de linhas na tabela na página {page_num}: {len(rows)}")

        for i, row in enumerate(rows, start=1):
            try:
                id_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text.strip()
                due_date_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text.strip()

                print(f"[PÁG {page_num} - LINHA {i}] ID: {id_text} - Due Date: {due_date_text}")

                if is_due_date_passed(due_date_text):
                    print(f"[PÁG {page_num} - LINHA {i}] Fatura {id_text} está vencida ou vence hoje.")
                    invoices.append({'ID': id_text, 'Due Date': due_date_text})
                else:
                    print(f"[PÁG {page_num} - LINHA {i}] Fatura {id_text} ainda não venceu.")
            except Exception as e:
                print(f"[ERRO] Falha ao ler linha {i} na página {page_num}: {e}")

        # Clicar no botão da próxima página, se não for a última
        if page_num < total_pages:
            try:
                pagination_button = driver.find_element(By.LINK_TEXT, str(page_num + 1))
                pagination_button.click()
                print(f"[INFO] Clicou no botão da página {page_num + 1}")
                time.sleep(2)  # Dá tempo da página carregar a tabela nova
            except Exception as e:
                print(f"[ERRO] Falha ao clicar no botão da página {page_num + 1}: {e}")

    driver.switch_to.default_content()
    print(f"[INFO] Total de faturas vencidas ou vencendo hoje: {len(invoices)}")
    return invoices
