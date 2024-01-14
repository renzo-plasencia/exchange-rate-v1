from selenium import webdriver
from datetime import date
import pandas as pd

root = 'D:/UDEMY/WEB SCRAPING/'
file = 'Dolar Precios.xlsx'
ruta=root+file

data = pd.read_excel(ruta)

website = "https://jetperu.com.pe/"
path = "C:/Users/Renzo Plasencia/Downloads/chromedriver.exe"

today = str(date.today())
driver = webdriver.Chrome(path) #Activa el driver
driver.get(website) #con el driver abre la web

buy_rate = driver.find_element_by_xpath('//span[@id="buyRate"]').text
sell_rate = driver.find_element_by_xpath('//span[@id="sellRate"]').text
print('Compra '+today+"= "+ buy_rate)
print('Venta '+today+"= "+sell_rate)

driver.quit() #cerrar

#Crear un nuevo DataFrame con los datos actuales
dic_valores= {
    'Fecha': [today],
    'Compra': [buy_rate],
    'Venta': [sell_rate]
}

print(dic_valores)
new_data = pd.DataFrame(dic_valores)
data = pd.concat([data, new_data], ignore_index=True) #Concatenar con el anterior
data.to_excel(ruta, index=False) #Guardar

