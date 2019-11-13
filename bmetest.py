#
# Example. Using I2C at P9, P10
#
import sys
from machine import I2C, Pin, SPI
from BME280 import BME280

hspi = SPI(1, polarity=1, phase=1)

cspin = Pin(15,Pin.OUT)
cspin.on()

#i2c = I2C(scl=Pin(12), sda=Pin(13), freq=100000)                                                                                                  
#bme280 = BME280(i2c=i2c)                                                                                                                     


bme280 = BME280(spi=hspi,cspin=cspin)
values = bme280.read_compensated_data()
print('compensated values=')
print(values)

bme280.read_raw_data(values)
print('RAW values')
print(values)
