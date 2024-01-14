############# LIBRERÍAS #############
from selenium import webdriver
from datetime import date
import pandas as pd

############# VARIABLES #############
root = 'D:/Ruta/Prueba'
file = 'Dolar Precios.xlsx'
ruta=root+file
data = pd.read_excel(ruta)
today = str(date.today())

############# WEB #############
website = "https://pagina.com.pe/" #(se ocultó el nombre de la web)
path = "C:/Users/Usuario/Downloads/chromedriver.exe" #Ruta de prueba
driver = webdriver.Chrome(path)
driver.get(website)

############# ENCONTRAR ELEMENTOS EN LA WEB #############
buy_rate = driver.find_element_by_xpath('//span[@id="buyRate"]').text
sell_rate = driver.find_element_by_xpath('//span[@id="sellRate"]').text
driver.quit()

############# DataFrame #############
dic_valores= {
    'Fecha': [today],
    'Compra': [buy_rate],
    'Venta': [sell_rate]
}
new_data = pd.DataFrame(dic_valores)
data = pd.concat([data, new_data], ignore_index=True) #Concatenar con el anterior
data.to_excel(ruta, index=False) #Guardar
