import time
from bs4 import BeautifulSoup
from config import user, password
from selenium import webdriver

def obtDriver(url='https://windset.macmms.com/?a=11664581'):
    driver = webdriver.Chrome('/Users/juansantos/Desktop/Python/web-scrapping/driver/chromedriver')  # Optional argument, if not specified will search path.
    driver.get(url)
    j_username = driver.find_element_by_name('j_username')
    j_username.send_keys(user)
    j_password = driver.find_element_by_name('j_password')
    j_password.send_keys(password)
    j_password.submit()

    time.sleep(1)

    return driver

def obtNameProduct(driver):

    value = driver.find_element_by_class_name('graingerNameFld').get_attribute("value")

    return value

def obtCodeProduct(driver):
    codeContainer = driver.find_elements_by_class_name('formCellInside35')
    code = codeContainer[3].find_element_by_tag_name('input').get_attribute("value")

    return code

def obtQtyOnHand(driver):
    driver.find_element_by_class_name('listRow35').click()
    time.sleep(1)

    qtyContainer = driver.find_elements_by_class_name('formCellInside35')
    qty = qtyContainer[22].find_element_by_tag_name('input').get_attribute("value")

    return qty

def dataObt(url):
    driver = obtDriver(url)
        
    name = obtNameProduct(driver)
    qty = obtQtyOnHand(driver)
    code = obtCodeProduct(driver)

    driver.quit()

    lista = [name, qty, code]

    return lista

def printer(data):
    print('-'*10)
    print(f"\nEl Nombre del producto es { data[0] } con codigo { data[2] }")
    print(f"La cantidad en mano es: { data[1] }\n")
    print('-'*10)

def main():
    while True:
        codeQR = input("Scanea la pieza: ")
        data = dataObt(codeQR.strip())
        printer(data)


if __name__ == '__main__':
    main()