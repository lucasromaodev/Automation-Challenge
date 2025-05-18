from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def is_due_date_passed(due_date_str):
    try:
        due_date = datetime.strptime(due_date_str, '%d-%m-%Y').date()
        today = datetime.today().date()
        return due_date <= today
    except Exception as e:
        print(f"[ERRO] Falha ao processar data '{due_date_str}': {e}")
        return False

def get_due_invoices(driver):
    # Tenta trocar para iframe caso exista
    try:
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)
        print("[INFO] Trocou para iframe")
    except:
        print("[INFO] Nenhum iframe encontrado, continuando no contexto principal")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody tr")))

    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
    print(f"[INFO] Total de linhas na tabela: {len(rows)}")

    invoices = []
    for i, row in enumerate(rows, start=1):
        try:
            id_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text.strip()
            due_date_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text.strip()

            print(f"[LINHA {i}] ID: {id_text} - Due Date: {due_date_text}")

            if is_due_date_passed(due_date_text):
                print(f"[LINHA {i}] Fatura {id_text} está vencida ou vence hoje.")
                invoices.append({'ID': id_text, 'Due Date': due_date_text})
            else:
                print(f"[LINHA {i}] Fatura {id_text} ainda não venceu.")
        except Exception as e:
            print(f"[ERRO] Falha ao ler linha {i}: {e}")

    print(f"[INFO] Total de faturas vencidas ou vencendo hoje: {len(invoices)}")
    return invoices
