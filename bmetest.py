#
# Example. Using I2C at P9, P10
#
import sys
from machine import I2C, Pin, SPI
import BME280Float

hspi = SPI(1, baudrate=80000000, polarity=0, phase=0)

cspin = Pin(15,Pin.OUT)

bme280 = BME280Float(spi=hspi,cspin=cspin)
bme280.values
