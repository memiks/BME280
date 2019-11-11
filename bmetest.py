#
# Example. Using I2C at P9, P10
#
import sys
from machine import I2C, Pin, SPI
from BME280Float import BME280Float

hspi = SPI(1, polarity=0, phase=0)

cspin = Pin(15,Pin.OUT)
cspin.on()

bme280 = BME280Float(spi=hspi,cspin=cspin)
values = bme280.read_compensated_data()
print('compensated values=')
print(values)

bme280.read_raw_data(values)
print('RAW values')
print(values)
