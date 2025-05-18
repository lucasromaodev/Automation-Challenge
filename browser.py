from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_browser():
    # Inicializa o navegador Chrome
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://rpachallengeocr.azurewebsites.net/")

    # supondo que driver já está aberto e carregou o site
    wait = WebDriverWait(driver, 10)  # timeout de 10 segundos

    # esperar até o botão START estar clicável
    start_button = wait.until(EC.element_to_be_clickable((By.ID, "start")))

    # clicar no botão
    start_button.click()

    print("Botão START clicado com sucesso!")
    return driver

