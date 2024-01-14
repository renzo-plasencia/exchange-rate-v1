# exchange-rate-v1
Script en python para obtener el tipo de cambio de forma automatizada y diaria.

**¿Cuál es el objetivo?**
Obtener el tipo de cambio dólares de una casa de cambio peruana. En un periodo diario y que se agregue la información a un excel.

**Limitaciones:**
- Las casas de cambio pueden demorar en actualizar su tasa.
- La tasa puede variar al momento de hacer la compra final.

**¿Qué se usó?**
Se programó un script en Python usando Selenium y Pandas para obtener el tipo de cambio de la página web. Se usó selenium debido a que se ejecutaba un script dentro de la web y Pandas para guardar los datos en un DataFrame. 
Así mismo, el programador de tareas de Windows para que se ejecute el script de forma repetitiva diariamente en un lapso de tiempo especificado.


**Pasos siguientes:**
- Rescatar diferentes tasas de otras casas de cambio.
- Realizar análisis automático de la mejor opción.
- Enviar una alerta en windows sobre qué casa de cambio podría elegir ese día.
