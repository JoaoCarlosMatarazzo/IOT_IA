import Adafruit_DHT
import time
import random  

# Configuração do sensor DHT22
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO4

def read_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return temperature, humidity

def read_air_quality():
    
    air_quality = random.uniform(50, 150)  
    return air_quality
