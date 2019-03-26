# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pyupm_urm37', [dirname(__file__)])
        except ImportError:
            import _pyupm_urm37
            return _pyupm_urm37
        if fp is not None:
            try:
                _mod = imp.load_module('_pyupm_urm37', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyupm_urm37 = swig_import_helper()
    del swig_import_helper
else:
    import _pyupm_urm37
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


URM37_DEFAULT_UART = _pyupm_urm37.URM37_DEFAULT_UART
class URM37(_object):
    """
    API for the DFRobot URM37 Ultrasonic Ranger.

    ID: urm37

    Name: DFRobot URM37 Ultrasonic Ranger

    Category: sound

    Manufacturer: dfrobot

    Connection: uart ainput gpio

    Link:http://www.dfrobot.com/index.php?route=product/product&product_id=53
    The driver was tested with the DFRobot URM37 Ultrasonic Ranger, V4. It
    has a range of between 5 and 500 centimeters (cm). It supports both
    analog distance measurement, and UART based temperature and distance
    measurements. This driver does not support PWM measurement mode.

    For UART operation, the only supported baud rate is 9600. In addition,
    you must ensure that the UART TX/RX pins are configured for TTL
    operation (the factory default) rather than RS232 operation, or
    permanent damage to your URM37 and/or MCU will result. On power up,
    the LED indicator will blink one long pulse, followed by one short
    pulse to indicate TTL operation. See the DFRobot wiki for more
    information:

    (https://www.dfrobot.com/wiki/index.php?title=URM37_V4.0_Ultrasonic_Sensor_%28SKU:SEN0001%29)

    An example using analog modeAn example using UART mode

    C++ includes: urm37.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, URM37, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, URM37, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(upm::URM37 self, int aPin, int resetPin, int triggerPin, float aref=5.0) -> URM37

        Parameters:
            aPin: int
            resetPin: int
            triggerPin: int
            aref: float

        __init__(upm::URM37 self, int aPin, int resetPin, int triggerPin) -> URM37

        Parameters:
            aPin: int
            resetPin: int
            triggerPin: int

        __init__(upm::URM37 self, int uart, int resetPin) -> URM37

        Parameters:
            uart: int
            resetPin: int


        URM37(int uart, int
        resetPin)

        URM37 object constructor (UART mode)

        Parameters:
        -----------

        uart:  Default UART to use (0 or 1).

        resetPin:  GPIO pin to use for reset 
        """
        this = _pyupm_urm37.new_URM37(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyupm_urm37.delete_URM37
    __del__ = lambda self : None;
    def reset(self):
        """
        reset(URM37 self)

        Parameters:
            self: upm::URM37 *


        void reset()

        Reset the device. This will take approximately 3 seconds to complete.

        """
        return _pyupm_urm37.URM37_reset(self)

    def getDistance(self, degrees=0):
        """
        getDistance(URM37 self, int degrees=0) -> float

        Parameters:
            degrees: int

        getDistance(URM37 self) -> float

        Parameters:
            self: upm::URM37 *


        float getDistance(int
        degrees=0)

        Get the distance measurement. A return value of 65535.0 in UART mode
        indicates an invalid measurement.

        Parameters:
        -----------

        degrees:  in UART mode, this specifies the degrees to turn an attached
        PWM servo connected to the MOTO output on the URM37. Default is 0.
        Valid values are 0-270. This option is ignored in analog mode.

        The measured distance in cm 
        """
        return _pyupm_urm37.URM37_getDistance(self, degrees)

    def getTemperature(self):
        """
        getTemperature(URM37 self) -> float

        Parameters:
            self: upm::URM37 *


        float
        getTemperature()

        Get the temperature measurement. This is only valid in UART mode.

        The measured temperature in degrees C 
        """
        return _pyupm_urm37.URM37_getTemperature(self)

    def readEEPROM(self, *args):
        """
        readEEPROM(URM37 self, uint8_t addr) -> uint8_t

        Parameters:
            addr: uint8_t


        uint8_t
        readEEPROM(uint8_t addr)

        In UART mode only, read a value from the EEPROM and return it.

        Parameters:
        -----------

        addr:  The address in the EEPROM to read. Valid values are between
        0x00-0x04.

        The EEPROM value at addr 
        """
        return _pyupm_urm37.URM37_readEEPROM(self, *args)

    def writeEEPROM(self, *args):
        """
        writeEEPROM(URM37 self, uint8_t addr, uint8_t value)

        Parameters:
            addr: uint8_t
            value: uint8_t


        void
        writeEEPROM(uint8_t addr, uint8_t value)

        In UART mode only, write a value into an address on the EEPROM.

        Parameters:
        -----------

        addr:  The address in the EEPROM to write. Valid values are between
        0x00-0x04.

        value:  The value to write

        The EEPROM value at addr 
        """
        return _pyupm_urm37.URM37_writeEEPROM(self, *args)

URM37_swigregister = _pyupm_urm37.URM37_swigregister
URM37_swigregister(URM37)

# This file is compatible with both classic and new-style classes.


