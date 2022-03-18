# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
import os
import eel


@eel.expose
def ua_to_en(text):

    ua_characters = ["а", "А", "В", "е", "Е", "З", "і", "І", "К", "М", "Н", "о", "О", "р", "Р", "с", "С", "Т", "у", "х"]
    en_characters = ["a", "A", "B", "e", "E", "3", "i", "I", "K", "M", "H", "o", "O", "p", "P", "c", "C", "T", "y", "x"]

    for i in range(len(ua_characters)):
        text = text.replace(ua_characters[i], en_characters[i])

    substitute = 0
    matched_list = [characters in en_characters for characters in text]

    for i in range(len(matched_list)):
        if matched_list[i] == True:
            substitute += 1

    #print(f"Я замінив {substitute} із {len(text)} символів :)")

    return text

@eel.expose
def replace_sybmols(text, sybmol1, sybmol2):

    text = text.replace(sybmol1, sybmol2)

    return text

@eel.expose
def synonymizer(text):

    options = Options()
    #options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\new_chrome.exe"
    options.add_argument("headless")
    driver = webdriver.Chrome(r"webdriver\chromedriver.exe", chrome_options = options)

    driver.get("https://rustxt.ru/synonymizer")
    driver.set_window_size(1920,1080)
    driver.execute_script("window.scrollTo(0, 1080)")
    sleep(2)

    driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div[2]/form/div/div[1]/div/div[1]/div[2]/label").click()
    sleep(2)
    driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div[2]/form/div/div[1]/div/div[2]/select").click()
    sleep(1)
    driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div[2]/form/div/div[1]/div/div[2]/select/option[3]").click()
    sleep(1)

    text_window = driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div[2]/form/div/div[2]/div[1]/textarea")
    text_window.send_keys(text)
    sleep(2)

    driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div[2]/form/div/div[2]/div[2]/button").click()
    sleep(5)

    new_text = driver.find_element_by_xpath("/html/body/main/div[1]/div/div/div[4]/div[3]")
    result = new_text.text
    driver.quit()
    os.system("CLS")

    return result

@eel.expose
def clear_text(text):

    text = re.sub(r'\([^)]*\)', '', text)

if __name__ == "__main__":

    eel.init("web")
    eel.start("main.html", size = (700, 700))
