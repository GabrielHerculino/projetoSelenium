from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from time import sleep

servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service = servico)
driver.get('https://dados.es.gov.br/')

#deixar em fullscream
driver.maximize_window()

#entra em dados
WebDriverWait(driver, 10).until(e_c.presence_of_element_located(
    (By.XPATH, '//*[@id="navbar"]/ul/li[3]/a'))).click()
#despesas - execução orçamentária e financeira
WebDriverWait(driver, 10).until(e_c.presence_of_element_located(
    (By.XPATH, '//*[@id="content"]/div[3]/div/section[1]/div[1]/ul/li[11]/div/h3/a'))).click()

#despesas 2023 - explorar
WebDriverWait(driver, 10).until(e_c.presence_of_element_located(
    (By.XPATH, '//*[@id="dataset-resources"]/ul/li[77]/div/a'))).click()
#download 2023
WebDriverWait(driver, 10).until(e_c.presence_of_element_located(
    (By.XPATH, '//*[@id="dataset-resources"]/ul/li[77]/div/ul/li[2]/a'))).click()

#despesas 2022 - explorar
WebDriverWait(driver, 10).until(e_c.presence_of_element_located(
    (By.XPATH, '//*[@id="dataset-resources"]/ul/li[73]/div/a'))).click()
#download 2022
WebDriverWait(driver, 10).until(e_c.presence_of_element_located(
    (By.XPATH, '//*[@id="dataset-resources"]/ul/li[73]/div/ul/li[2]/a'))).click()
sleep(40)

pass