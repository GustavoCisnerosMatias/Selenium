from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


import scrapy

class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes_spider'
    allowed_domains = ['tripadvisor.es']
    start_urls = ['https://www.tripadvisor.es/Hotels-g297539-Salinas_Santa_Elena_Province-Hotels.html']
    visited_hotels = set()

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'tutorial.middlewares.CustomHeadersMiddleware': 543,
        }
    }
    
    def parse(self, response):
        # Selenium!
        # Opciones de navegación
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')

        # Ruta al archivo ejecutable del ChromeDriver
        driver_path = r'C:\Users\Cisneros\tutorial\chrome drive\chromedriver-win64\chromedriver.exe'

        # Crear un objeto Service
        service = Service(driver_path)

        # Inicializar el controlador de Chrome
        driver = webdriver.Chrome(service=service, options=options)

        driver.get('https://www.tripadvisor.es/Hotels-g297539-Salinas_Santa_Elena_Province-Hotels.html')

        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.bqhCp _T u z Gz Wh sglCU'.replace(' ', '.'))))\
        .click()

        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[1]'.replace(' ', '.'))))\
        .click()

        WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[5]/div[3]'.replace(' ', '.'))))\
        .click()
    
        WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/button'.replace(' ', '.'))))\
        .click()  
                
        time.sleep(15)

        listanombres = driver.find_elements(By.CSS_SELECTOR, '.jsTLT.K')
        listaprecios = driver.find_elements(By.CSS_SELECTOR, '.fwoto.f')

        for i, (nombre, precio) in enumerate(zip(listanombres, listaprecios)):
            nombreHotel = nombre.text
            precioHotel = precio.text
            print(nombreHotel + " " + precioHotel )
            if precioHotel !=None:
                yield {'NombreHotel': nombreHotel, 'PrecioHotel': precioHotel, 'Dias':"30"}
         
        driver.get('https://www.tripadvisor.es/Hotels-g297539-Salinas_Santa_Elena_Province-Hotels.html')
        
        WebDriverWait(driver, 25)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.bqhCp _T u z Gz Wh sglCU'.replace(' ', '.'))))\
        .click()
        
        WebDriverWait(driver, 25)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div[1]'.replace(' ', '.'))))\
        .click()
        
        WebDriverWait(driver, 25)\
            .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[3]/div[2]'.replace(' ', '.'))))\
            .click() 

        time.sleep(15)

        listanombres15 = driver.find_elements(By.CSS_SELECTOR, '.jsTLT.K')
        listaprecios15 = driver.find_elements(By.CSS_SELECTOR, '.fwoto.f')

        for i, (nombre15, precio15) in enumerate(zip(listanombres15, listaprecios15)):
            nombreHotel15 = nombre15.text
            precioHotel15 = precio15.text
            print(nombreHotel15 + " " + precioHotel15 )
            if precioHotel15 !=None:
                yield {'NombreHotel': nombreHotel15, 'PrecioHotel': precioHotel15, 'Dias':"15"}
        
        time.sleep(25)

        driver.get('https://www.tripadvisor.es/Hotels-g297539-Salinas_Santa_Elena_Province-Hotels.html')
        
        WebDriverWait(driver, 25)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.bqhCp _T u z Gz Wh sglCU'.replace(' ', '.'))))\
        .click()
        
        WebDriverWait(driver, 25)\
        .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div[1]'.replace(' ', '.'))))\
        .click()
        WebDriverWait(driver, 25)\
            .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[3]'.replace(' ', '.'))))\
            .click() 

        time.sleep(15)
        listanombres1 = driver.find_elements(By.CSS_SELECTOR, '.jsTLT.K')
        listaprecios1 = driver.find_elements(By.CSS_SELECTOR, '.fwoto.f')

        for i, (nombre1, precio1) in enumerate(zip(listanombres1, listaprecios1)):
            nombre1 = nombre1.text
            precio1 = precio1.text
            print(nombre1 + " " + precio1 )
            if precio1 !=None:
                yield {'NombreHotel': nombre1, 'PrecioHotel': precio1, 'Dias':"3"}
        
        time.sleep(25)
        