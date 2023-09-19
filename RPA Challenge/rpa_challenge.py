from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time


def initialize(browser):

    url = "https://rpachallenge.com/"

    #abre o url desejado
    browser.get(url)
    browser.maximize_window()

    #clica no botao start
    browser.find_element('xpath', '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()


def setData(data, browser):

    for index, row in data.iterrows():

        #insere os dados em seus respectivos campos
        browser.find_element('xpath', '//*[@ng-reflect-name="labelFirstName"]').send_keys(row['First Name'])
        browser.find_element('xpath', '//*[@ng-reflect-name="labelLastName"]').send_keys(row['Last Name'])
        browser.find_element('xpath', '//*[@ng-reflect-name="labelCompanyName"]').send_keys(row['Company Name'])
        browser.find_element('xpath', '//*[@ng-reflect-name="labelRole"]').send_keys(row['Role in Company'])
        browser.find_element('xpath', '//*[@ng-reflect-name="labelAddress"]').send_keys(row['Address'])
        browser.find_element('xpath', '//*[@ng-reflect-name="labelEmail"]').send_keys(row['Email'])
        browser.find_element('xpath', '//*[@ng-reflect-name="labelPhone"]').send_keys(row['Phone Number'])

        #clica no botao submit
        browser.find_element('xpath', '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()



service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)
data = pd.read_excel(r"E:\Documentos\LucasClemente\Projetos\Python RPA\challenge.xlsx", "Sheet1")


initialize(browser)
setData(data, browser)
time.sleep(3)
