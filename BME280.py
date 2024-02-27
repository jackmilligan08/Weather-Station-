#Libraries 
import smbus2
import time
from time import sleep 

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)
#Continuous Loop
while True:
#Recieving Data from BME280 
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
#Printing Data from BME280)
    print("Humidity:", humidity,"%")
    print("Pressure:", pressure,"hPa")
    print("Ambient_Temperature:", ambient_temperature,"*C")
    print("")
    sleep(1)
