import Adafruit_DHT
import time
import random  

# Configuração do sensor DHT22
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  

def read_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return temperature, humidity

def read_air_quality():
    
    air_quality = random.uniform(50, 150)  # Simula um valor de qualidade do ar
    return air_quality

def main():
    while True:
        temperature, humidity = read_temperature_humidity()
        air_quality = read_air_quality()

        if temperature is not None and humidity is not None:
            print(f"Temperatura: {temperature:.2f}°C, Umidade: {humidity:.2f}%")
        else:
            print("Falha na leitura do sensor de temperatura/umidade.")

        print(f"Qualidade do ar: {air_quality:.2f}")

        recommendations = analyze_data(temperature, humidity, air_quality) # type: ignore (a ser definido)
        if recommendations:
            for recommendation in recommendations:
                print(f"Recomendação: {recommendation}")
        
        time.sleep(10)  

if __name__ == "__main__":
    main()
