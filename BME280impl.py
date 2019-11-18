from BME280 import BME280

#    I2C ADDRESS/BITS/SETTINGS
#    -----------------------------------------------------------------------
_BME280_ADDRESS = const(0x77)
_BME280_CHIPID = const(0x60)

class BME280_I2C(BME280):
    """Driver for BME280 connected over I2C"""
    def __init__(self, i2c, address=_BME280_ADDRESS):
        self._i2c = i2c
        self._address = address
        super().__init__()

    def _read_register(self, register, length):
        register &= 0xFF
        result = bytearray(length)
        self._i2c.readfrom_mem_into(self._address, register, result)
        print("$%02X => %s" % (register, [hex(i) for i in result]))
        return result

    def _write_register_byte(self, register, value):
        register &= 0xFF
        value &= 0xFF
        self._i2c.writeto_mem(self._address, register, value)
        print("$%02X <= 0x%02X" % (register, value))

class BME280_SPI(BME280):
    """Driver for BME280 connected over SPI"""
    def __init__(self, spi, cs, baudrate=100000):
        self._spi = spi
        self._cs = cs
        super().__init__()

    def _read_register(self, register, length):
        self._cs(0)
        #self._spi.write(bytes(register))
        self._spi.write(bytearray([register | 0x80]))  #pylint: disable=no-member
        result = self._spi.read(length)              #pylint: disable=no-member
        self._cs(1)
        #print("_read_register $%02X => %s" % (register, [hex(i) for i in result]))
        return result

    def _write_register_byte(self, register, value):
        self._cs(0)

        self._spi.write(bytearray([register&0x7F])) #pylint: disable=no-member
        self._spi.write(bytearray([value])) #pylint: disable=no-member
        self._cs(1)
        #print("_write_register_byte $%02X => %s" % (register, [hex(i) for i in bytearray([value])]))
