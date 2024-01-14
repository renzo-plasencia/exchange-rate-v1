# Exchange Rate Script
## **¿Cuál es el objetivo?**
El objetivo de este script es obtener de forma automática la tasa de tipo de cambio de una casa de cambio peruana específica. Se busca obtener la tasa de compra y venta de dólares de forma diaria y que se guarde dentro de un archivo que será revisado luego.

## **Limitaciones:**
- Algunas casas de cambio pueden demorar en actualizar su tasa de cambio.
- La tasa puede variar al momento de hacer la compra final por factores externos.

## **¿Qué se usó?**
Se programó un script en Python usando las librerías **Selenium** y **Pandas** para obtener el tipo de cambio de la página web y almacenarlo en un archivo de Excel. Se usó la libería selenium para ejecutar un script dentro de la web pública de la empresa y la libería Pandas para posteriormente guardar los datos en un DataFrame. Así mismo, luego de probar y tener el script completo se agregó al programador de tareas de Windows permitiendo que se ejecute de forma automática y repetitiva diariamente.

## **Siguientes Pasos:**
- Guardar las tasas de compra y venta de dólares de otras casas de cambio online.
- Realizar análisis automático que busque la mejor opción.
- Enviar una alerta en Windows sobre la casa de cambio que tiene la mejor tasa ese día.

# Script
> Conoce el script completo: https://github.com/renzo-plasencia/exchange-rate-v1/blob/main/exchange_rate.py
