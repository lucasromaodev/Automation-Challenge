from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rpachallengeocr.azurewebsites.net/")

# Aguarde carregar tudo, se necessário (ou clique em "Start" se isso for necessário para liberar a tabela)
input("Pressione Enter após clicar em 'Start' manualmente, se necessário...")

import time

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def testar_paginacao_por_numeros(driver):
    wait = WebDriverWait(driver, 10)
    pagina_atual = 1

    while True:
        print(f"\n[PÁGINA {pagina_atual}] ------------------------------")
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table tbody tr")))
        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

        for i, row in enumerate(rows, start=1):
            try:
                id_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text.strip()
                due_date_text = row.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text.strip()
                print(f"[LINHA {i}] ID: {id_text} | Due Date: {due_date_text}")
            except Exception as e:
                print(f"[ERRO] Linha {i} não pôde ser lida: {e}")

        # Esperar para visualização
        time.sleep(2)

        try:
            # Buscar todos os botões da paginação
            pagination_items = driver.find_elements(By.CSS_SELECTOR, "ul.pagination li.page-item")

            # Encontrar o índice da página atual
            current_index = None
            for index, item in enumerate(pagination_items):
                if "active" in item.get_attribute("class"):
                    current_index = index
                    break

            # Verifica se há próxima página
            if current_index is not None and current_index + 1 < len(pagination_items):
                next_page = pagination_items[current_index + 1]
                next_link = next_page.find_element(By.TAG_NAME, "a")

                driver.execute_script("arguments[0].style.border='3px solid red'", next_link)
                driver.execute_script("arguments[0].click();", next_link)

                # Esperar carregar nova página
                wait.until(EC.staleness_of(rows[0]))
                pagina_atual += 1
            else:
                print("[INFO] Última página alcançada.")
                break

        except Exception as e:
            print(f"[ERRO] Falha ao avançar para próxima página: {e}")
            break




testar_paginacao_por_numeros(driver)

driver.quit()
