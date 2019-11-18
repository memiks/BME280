import sys
import time
from machine import Pin, SPI
from BME280impl import BME280_SPI

#
# Example. Using SPI at P14, P13, P12
#
hspi = SPI(-1, polarity=1, phase=1, firstbit=SPI.MSB, sck=Pin(14), mosi=Pin(13), miso=Pin(12))

#
# Chip Select at P15
#
cspin = Pin(15,Pin.OUT)
cspin.on()

bme280 = BME280_SPI(hspi, cspin)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    time.sleep(2)
