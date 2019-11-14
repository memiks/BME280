from BME280 import BME280

class BME280_I2C(BME280):
    """Driver for BME280 connected over I2C"""
    def __init__(self, i2c, address=_BME280_ADDRESS):
        self._i2c = i2c
        self._address = address
        super().__init__()

    def _read_register(self, register, length):
        register &= 0xFF
        result = bytearray(length)
        with self._i2c as i2c:
            i2c.readfrom_mem_into(self._address, register, result)
            print("$%02X => %s" % (register, [hex(i) for i in result]))
            return result

    def _write_register_byte(self, register, value):
        register &= 0xFF
        value &= 0xFF
        with self._i2c as i2c:
            i2c.writeto_mem(self._address, register, value)
            print("$%02X <= 0x%02X" % (register, value))

class BME280_SPI(BME280):
    """Driver for BME280 connected over SPI"""
    def __init__(self, spi, cs, baudrate=100000):
        self._spi = spi
        self._cs = cs
        super().__init__()

    def _read_register(self, register, length):
        register = (register | 0x80) & 0xFF  # Read single, bit 7 high.
        with self._spi as spi:
            self._cs.off()
            spi.write(bytearray([register]))  #pylint: disable=no-member
            result = bytearray(length)
            spi.readinto(result)              #pylint: disable=no-member
            self._cs.on()
            print("$%02X => %s" % (register, [hex(i) for i in result]))
            return result

    def _write_register_byte(self, register, value):
        register &= 0x7F  # Write, bit 7 low.
        value &= 0xFF
        with self._spi as spi:
            self._cs.off()

            spi.write(bytearray([register, value])) #pylint: disable=no-member
            self._cs.on()
            print("$%02X => %s" % (register, [hex(i) for i in value]))
