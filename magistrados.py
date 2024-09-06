from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Ruta del driver (ajusta esto a la ubicación donde descargaste ChromeDriver o el driver de tu navegador)
#driver_path = '/ruta/al/chromedriver'

# Crear opciones para Chrome
#chrome_options = Options()
#chrome_options.add_argument("--headless")  # Opcional: ejecuta Chrome en modo sin cabeza (sin abrir ventana)
#chrome_options.add_argument("--no-sandbox")
#chrome_options.add_argument("--disable-dev-shm-usage")

# Servicio de ChromeDriver
#service = Service(executable_path=driver_path)

# Inicializar el driver con las opciones y servicio
#driver = webdriver.Chrome(service=service, options=chrome_options)

driver = webdriver.Chrome()  # Asegúrate de tener el driver de Chrome o el que prefieras usar

# URL de la página principal con la lista de magistrados
url = 'https://w3.cjf.gob.mx/sevie_page/busquedas/Consultas/Res_Alfabeto.asp?sTipo=J&sLetra=A'

# Abrir la página
driver.get(url)

# Pausa breve para cargar la página
time.sleep(3)

# Encontrar el primer magistrado usando el XPath proporcionado
xpath_primer_nombre = '/html/body/div/center/table/tbody/tr[5]/td/div/center/table/tbody/tr[1]/td/font[2]/a'
primer_nombre = driver.find_element(By.XPATH, xpath_primer_nombre)

# Hacer clic en el primer nombre
primer_nombre.click()

# Pausa para asegurarse de que la nueva página cargue completamente
time.sleep(3)

# XPaths proporcionados
xpath_lugar_de_trabajo = '//*[@id="table8"]/tbody/tr[3]/td/font/a'
xpath_estudios = '//*[@id="table10"]/tbody/tr[5]/td/font/curriculum:/p/text()[1]'
xpath_cargos = '//*[@id="table10"]/tbody/tr[10]/td/font/dentro/p/text()'
xpath_fecha_titulacion = '//*[@id="table11"]/tbody/tr[1]/td[2]/font'
xpath_cedula_profesional = '//*[@id="table11"]/tbody/tr[3]/td[2]/font'

# Extraer la información de la página
lugar_de_trabajo = driver.find_element(By.XPATH, xpath_lugar_de_trabajo).text
estudios = driver.find_element(By.XPATH, xpath_estudios).text
cargos = driver.find_element(By.XPATH, xpath_cargos).text
fecha_titulacion = driver.find_element(By.XPATH, xpath_fecha_titulacion).text
cedula_profesional = driver.find_element(By.XPATH, xpath_cedula_profesional).text

# Cerrar el navegador
driver.quit()

# Crear un dataframe con la información extraída
df = pd.DataFrame({
    'Lugar de Trabajo': [lugar_de_trabajo],
    'Estudios': [estudios],
    'Cargos Desempeñados': [cargos],
    'Fecha de Titulación': [fecha_titulacion],
    'Cédula Profesional': [cedula_profesional]
})

# Guardar la información en un archivo Excel
df.to_excel('informacion_magistrado.xlsx', index=False)

print('Información guardada exitosamente en Excel.')