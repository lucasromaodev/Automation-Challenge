from selenium import webdriver

def init_browser():
    # Inicializa o navegador Chrome
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get("https://rpachallengeocr.azurewebsites.net/")
    return driver