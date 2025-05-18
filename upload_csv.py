from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def upload_csv(driver):
    wait = WebDriverWait(driver, 10)

    # Espera até o input de arquivo estar presente no DOM
    file_input = wait.until(EC.presence_of_element_located((By.NAME, "csv")))

    # Caminho absoluto para o arquivo invoices.csv
    file_path = os.path.abspath("invoices.csv")

    # Envia o arquivo diretamente para o input
    file_input.send_keys(file_path)
