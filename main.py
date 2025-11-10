from selenium import webdriver


# Função simulando um seletor autorreparável
def find_element_autorepair(driver, selector):
    try:
        # Tenta encontrar o seletor original
        return driver.find_element("xpath", selector)
    except:
        print("Elemento não encontrado! Buscando alternativa...")
        # Simula heurística de reparo (busca similar)
        alternatives = driver.find_elements("xpath", "//*[contains(text(), 'Entrar') or contains(text(), 'Login')]")
        if alternatives:
            print("Elemento alternativo encontrado!")
            return alternatives[0]
        else:
            raise Exception("Elemento não encontrado e sem alternativa.")

# Execução do teste
driver = webdriver.Chrome()
driver.get("https://ldvk-bf.github.io/mc646-autorepair-test/")

botao = find_element_autorepair(driver, "//button[text()='Entrar']")
botao.click()

print("Teste executado com sucesso mesmo após mudança de interface!")
driver.quit()
