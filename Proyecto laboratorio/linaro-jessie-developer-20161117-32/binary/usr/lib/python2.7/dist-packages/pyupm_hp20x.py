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
            fp, pathname, description = imp.find_module('_pyupm_hp20x', [dirname(__file__)])
        except ImportError:
            import _pyupm_hp20x
            return _pyupm_hp20x
        if fp is not None:
            try:
                _mod = imp.load_module('_pyupm_hp20x', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyupm_hp20x = swig_import_helper()
    del swig_import_helper
else:
    import _pyupm_hp20x
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


HP20X_I2C_BUS = _pyupm_hp20x.HP20X_I2C_BUS
HP20X_DEFAULT_I2C_ADDR = _pyupm_hp20x.HP20X_DEFAULT_I2C_ADDR
class HP20X(_object):
    """
    API for the HP20X-based Grove Barometer (High-Accuracy)

    ID: hp20x

    Name: Grove Barometer (High-Accuracy)

    Other Names: HP20X Barometer (High-Accuracy)

    Category: pressure

    Manufacturer: seeed

    Link:http://www.seeedstudio.com/depot/Grove-Barometer-
    HighAccuracy-p-1865.html

    Connection: i2c  This is a high-accuracy barometer providing pressure,
    altitude, and temperature data. It can be calibrated for a given
    altitude offset, and a wide range of interrupt generating capabilities
    are supported. As usual, see the HP20X datasheet for more details.

    This module was developed using a Grove Barometer (High-Accuracy)
    based on an HP206C chip.

    C++ includes: hp20x.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HP20X, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HP20X, name)
    __repr__ = _swig_repr
    CMD_SOFT_RST = _pyupm_hp20x.HP20X_CMD_SOFT_RST
    CMD_ADC_CVT = _pyupm_hp20x.HP20X_CMD_ADC_CVT
    CMD_READ_PT = _pyupm_hp20x.HP20X_CMD_READ_PT
    CMD_READ_AT = _pyupm_hp20x.HP20X_CMD_READ_AT
    CMD_READ_P = _pyupm_hp20x.HP20X_CMD_READ_P
    CMD_READ_A = _pyupm_hp20x.HP20X_CMD_READ_A
    CMD_READ_T = _pyupm_hp20x.HP20X_CMD_READ_T
    CMD_ANA_CAL = _pyupm_hp20x.HP20X_CMD_ANA_CAL
    CMD_READ_REG = _pyupm_hp20x.HP20X_CMD_READ_REG
    CMD_WRITE_REG = _pyupm_hp20x.HP20X_CMD_WRITE_REG
    CHNL_PT = _pyupm_hp20x.HP20X_CHNL_PT
    CHNL_T = _pyupm_hp20x.HP20X_CHNL_T
    CHNL_SHIFT = _pyupm_hp20x.HP20X_CHNL_SHIFT
    DSR_4096 = _pyupm_hp20x.HP20X_DSR_4096
    DSR_2048 = _pyupm_hp20x.HP20X_DSR_2048
    DSR_1024 = _pyupm_hp20x.HP20X_DSR_1024
    DSR_512 = _pyupm_hp20x.HP20X_DSR_512
    DSR_256 = _pyupm_hp20x.HP20X_DSR_256
    DSR_128 = _pyupm_hp20x.HP20X_DSR_128
    DSR_SHIFT = _pyupm_hp20x.HP20X_DSR_SHIFT
    REG_ALT_OFF_LSB = _pyupm_hp20x.HP20X_REG_ALT_OFF_LSB
    REG_ALT_OFF_MSB = _pyupm_hp20x.HP20X_REG_ALT_OFF_MSB
    REG_PA_H_TH_LSB = _pyupm_hp20x.HP20X_REG_PA_H_TH_LSB
    REG_PA_H_TH_MSB = _pyupm_hp20x.HP20X_REG_PA_H_TH_MSB
    REG_PA_M_TH_LSB = _pyupm_hp20x.HP20X_REG_PA_M_TH_LSB
    REG_PA_M_TH_MSB = _pyupm_hp20x.HP20X_REG_PA_M_TH_MSB
    REG_PA_L_TH_LSB = _pyupm_hp20x.HP20X_REG_PA_L_TH_LSB
    REG_PA_L_TH_MSB = _pyupm_hp20x.HP20X_REG_PA_L_TH_MSB
    REG_T_H_TH = _pyupm_hp20x.HP20X_REG_T_H_TH
    REG_T_M_TH = _pyupm_hp20x.HP20X_REG_T_M_TH
    REG_T_L_TH = _pyupm_hp20x.HP20X_REG_T_L_TH
    REG_INT_EN = _pyupm_hp20x.HP20X_REG_INT_EN
    REG_INT_CFG = _pyupm_hp20x.HP20X_REG_INT_CFG
    REG_INT_SRC = _pyupm_hp20x.HP20X_REG_INT_SRC
    REG_PARA = _pyupm_hp20x.HP20X_REG_PARA
    INT_EN_T_WIN_EN = _pyupm_hp20x.HP20X_INT_EN_T_WIN_EN
    INT_EN_PA_WIN_EN = _pyupm_hp20x.HP20X_INT_EN_PA_WIN_EN
    INT_EN_T_TRAV_EN = _pyupm_hp20x.HP20X_INT_EN_T_TRAV_EN
    INT_EN_PA_TRAV_EN = _pyupm_hp20x.HP20X_INT_EN_PA_TRAV_EN
    INT_EN_T_RDY_EN = _pyupm_hp20x.HP20X_INT_EN_T_RDY_EN
    INT_EN_PA_RDY_EN = _pyupm_hp20x.HP20X_INT_EN_PA_RDY_EN
    INT_CFG_T_WIN_CFG = _pyupm_hp20x.HP20X_INT_CFG_T_WIN_CFG
    INT_CFG_PA_WIN_CFG = _pyupm_hp20x.HP20X_INT_CFG_PA_WIN_CFG
    INT_CFG_T_TRAV_CFG = _pyupm_hp20x.HP20X_INT_CFG_T_TRAV_CFG
    INT_CFG_PA_TRAV_CFG = _pyupm_hp20x.HP20X_INT_CFG_PA_TRAV_CFG
    INT_CFG_T_RDY_CFG = _pyupm_hp20x.HP20X_INT_CFG_T_RDY_CFG
    INT_CFG_PA_RDY_CFG = _pyupm_hp20x.HP20X_INT_CFG_PA_RDY_CFG
    INT_CFG_PA_MODE = _pyupm_hp20x.HP20X_INT_CFG_PA_MODE
    INT_SRC_T_WIN = _pyupm_hp20x.HP20X_INT_SRC_T_WIN
    INT_SRC_PA_WIN = _pyupm_hp20x.HP20X_INT_SRC_PA_WIN
    INT_SRC_T_TRAV = _pyupm_hp20x.HP20X_INT_SRC_T_TRAV
    INT_SRC_PA_TRAV = _pyupm_hp20x.HP20X_INT_SRC_PA_TRAV
    INT_SRC_T_RDY = _pyupm_hp20x.HP20X_INT_SRC_T_RDY
    INT_SRC_PA_RDY = _pyupm_hp20x.HP20X_INT_SRC_PA_RDY
    INT_SRC_DEV_RDY = _pyupm_hp20x.HP20X_INT_SRC_DEV_RDY
    INT_SRC_TH_ERR = _pyupm_hp20x.HP20X_INT_SRC_TH_ERR
    PARA_CMPS_EN = _pyupm_hp20x.HP20X_PARA_CMPS_EN
    def __init__(self, bus=0, address=0x76): 
        """
        __init__(upm::HP20X self, int bus=0, uint8_t address=0x76) -> HP20X

        Parameters:
            bus: int
            address: uint8_t

        __init__(upm::HP20X self, int bus=0) -> HP20X

        Parameters:
            bus: int

        __init__(upm::HP20X self) -> HP20X

        HP20X(int
        bus=HP20X_I2C_BUS, uint8_t address=HP20X_DEFAULT_I2C_ADDR)

        HP20X constructor

        Parameters:
        -----------

        bus:  I2C bus to use

        address:  Address for this device 
        """
        this = _pyupm_hp20x.new_HP20X(bus, address)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyupm_hp20x.delete_HP20X
    __del__ = lambda self : None;
    def init(self, *args):
        """
        init(HP20X self, upm::HP20X::DSR_BITS_T dsr=DSR_4096) -> bool

        Parameters:
            dsr: enum upm::HP20X::DSR_BITS_T

        init(HP20X self) -> bool

        Parameters:
            self: upm::HP20X *


        bool init(DSR_BITS_T
        dsr=DSR_4096)

        Sets up initial values and starts operation

        Parameters:
        -----------

        dsr:  Data sampling rate; one of the DSR_BITS_T values

        True if successful 
        """
        return _pyupm_hp20x.HP20X_init(self, *args)

    def writeCmd(self, *args):
        """
        writeCmd(HP20X self, uint8_t cmd) -> bool

        Parameters:
            cmd: uint8_t


        bool writeCmd(uint8_t
        cmd)

        Sends a command to the device

        Parameters:
        -----------

        cmd:  Command to send; usually, one of the HP20X_CMD_T values

        True if successful 
        """
        return _pyupm_hp20x.HP20X_writeCmd(self, *args)

    def writeReg(self, *args):
        """
        writeReg(HP20X self, upm::HP20X::HP20X_REG_T reg, uint8_t data) -> bool

        Parameters:
            reg: enum upm::HP20X::HP20X_REG_T
            data: uint8_t


        bool
        writeReg(HP20X_REG_T reg, uint8_t data)

        Writes a value to a register

        Parameters:
        -----------

        reg:  Register to write to; one of the HP20X_REG_T values

        data:  Value to write

        True if successful 
        """
        return _pyupm_hp20x.HP20X_writeReg(self, *args)

    def readReg(self, *args):
        """
        readReg(HP20X self, upm::HP20X::HP20X_REG_T reg) -> uint8_t

        Parameters:
            reg: enum upm::HP20X::HP20X_REG_T


        uint8_t
        readReg(HP20X_REG_T reg)

        Reads a register and returns its value

        Parameters:
        -----------

        reg:  Register to read; one of the HP20X_REG_T values

        Value of a specified register 
        """
        return _pyupm_hp20x.HP20X_readReg(self, *args)

    def readData(self):
        """
        readData(HP20X self) -> int

        Parameters:
            self: upm::HP20X *


        int readData()

        Reads 3 bytes of data in response to a conversion request, and
        converts it to an integer

        Value read back (temperature, pressure, etc.) 
        """
        return _pyupm_hp20x.HP20X_readData(self)

    def isReady(self):
        """
        isReady(HP20X self) -> bool

        Parameters:
            self: upm::HP20X *


        bool isReady()

        Checks to see if the DR_RDY bit is set, indicating the device can
        accept commands

        True if the device is ready, false otherwise 
        """
        return _pyupm_hp20x.HP20X_isReady(self)

    def waitforDeviceReady(self):
        """
        waitforDeviceReady(HP20X self) -> bool

        Parameters:
            self: upm::HP20X *


        bool
        waitforDeviceReady()

        Checks to see if the device is ready, and sleeps/retries if not.
        Returns once the device indicates it's ready.

        True if the device is ready; false if retries are exhausted 
        """
        return _pyupm_hp20x.HP20X_waitforDeviceReady(self)

    def getTemperature(self):
        """
        getTemperature(HP20X self) -> float

        Parameters:
            self: upm::HP20X *


        float
        getTemperature()

        Returns the temperature in Celsius

        Temperature 
        """
        return _pyupm_hp20x.HP20X_getTemperature(self)

    def getPressure(self):
        """
        getPressure(HP20X self) -> float

        Parameters:
            self: upm::HP20X *


        float getPressure()

        Returns the pressure in millibars

        Pressure 
        """
        return _pyupm_hp20x.HP20X_getPressure(self)

    def getAltitude(self):
        """
        getAltitude(HP20X self) -> float

        Parameters:
            self: upm::HP20X *


        float getAltitude()

        Returns the computed altitude in meters

        Altitude 
        """
        return _pyupm_hp20x.HP20X_getAltitude(self)

    def compensationEnable(self, *args):
        """
        compensationEnable(HP20X self, bool enable)

        Parameters:
            enable: bool


        void
        compensationEnable(bool enable)

        Enables or disables the on-chip compensator. This allows the chip to
        filter and clean up the output data.

        Parameters:
        -----------

        enable:  True to enable, false otherwise 
        """
        return _pyupm_hp20x.HP20X_compensationEnable(self, *args)

    def setInterruptEnable(self, *args):
        """
        setInterruptEnable(HP20X self, uint8_t bits) -> bool

        Parameters:
            bits: uint8_t


        bool
        setInterruptEnable(uint8_t bits)

        Sets up the interrupt enable register. This register defines which
        events can cause a hardware interrupt pin to be pulled high (active).

        Parameters:
        -----------

        bits:  One or more of the INT_EN_BITS_T bits

        True if successful, false otherwise 
        """
        return _pyupm_hp20x.HP20X_setInterruptEnable(self, *args)

    def setInterruptConfig(self, *args):
        """
        setInterruptConfig(HP20X self, uint8_t bits) -> bool

        Parameters:
            bits: uint8_t


        bool
        setInterruptConfig(uint8_t bits)

        Sets up the interrupt configuration register. This register defines
        which events can cause an interrupt to be indicated.

        Parameters:
        -----------

        bits:  One or more of the INT_EN_BITS_T bits

        True if successful, false otherwise 
        """
        return _pyupm_hp20x.HP20X_setInterruptConfig(self, *args)

    def getInterruptSource(self):
        """
        getInterruptSource(HP20X self) -> uint8_t

        Parameters:
            self: upm::HP20X *


        uint8_t
        getInterruptSource()

        Gets the interrupt source register. This register indicates which
        interrupts have been triggered. In addition, it indicates when certain
        operations have been completed.

        One of more of the INT_SRC_BITS_T values 
        """
        return _pyupm_hp20x.HP20X_getInterruptSource(self)

    def setDSR(self, *args):
        """
        setDSR(HP20X self, upm::HP20X::DSR_BITS_T dsr)

        Parameters:
            dsr: enum upm::HP20X::DSR_BITS_T


        void setDSR(DSR_BITS_T
        dsr)

        Sets the data sampling rate. Higher rates are more precise, but take
        more time per measurement.

        Parameters:
        -----------

        dsr:  One of the DSR_BITS_T values 
        """
        return _pyupm_hp20x.HP20X_setDSR(self, *args)

    def recalibrateInternal(self):
        """
        recalibrateInternal(HP20X self)

        Parameters:
            self: upm::HP20X *


        void
        recalibrateInternal()

        Starts an internal recalibration of analog blocks. This is faster than
        a soft reset. 
        """
        return _pyupm_hp20x.HP20X_recalibrateInternal(self)

    def softReset(self):
        """
        softReset(HP20X self)

        Parameters:
            self: upm::HP20X *


        void softReset()

        Executes a soft reset. All register values are reset to power-on
        defaults. This function returns when the reset is complete and the
        device reports it is ready. 
        """
        return _pyupm_hp20x.HP20X_softReset(self)

    def setAltitudeOffset(self, *args):
        """
        setAltitudeOffset(HP20X self, int16_t off)

        Parameters:
            off: int16_t


        void
        setAltitudeOffset(int16_t off)

        Sets the altitude offset for your region. See the datasheet for more
        details. Setting this correctly for your region is required for
        accurate altitude data.

        Parameters:
        -----------

        off:  Offset 
        """
        return _pyupm_hp20x.HP20X_setAltitudeOffset(self, *args)

    def setPAThreshholds(self, *args):
        """
        setPAThreshholds(HP20X self, int16_t low, int16_t med, int16_t high)

        Parameters:
            low: int16_t
            med: int16_t
            high: int16_t


        void
        setPAThreshholds(int16_t low, int16_t med, int16_t high)

        Sets pressure/altitude thresholds for interrupt generation

        Parameters:
        -----------

        low:  Low threshold to generate an interrupt

        med:  Medium threshold to generate an interrupt

        high:  High threshold to generate an interrupt 
        """
        return _pyupm_hp20x.HP20X_setPAThreshholds(self, *args)

    def setTemperatureThreshholds(self, *args):
        """
        setTemperatureThreshholds(HP20X self, int8_t low, int8_t med, int8_t high)

        Parameters:
            low: int8_t
            med: int8_t
            high: int8_t


        void
        setTemperatureThreshholds(int8_t low, int8_t med, int8_t high)

        Sets temperature thresholds for interrupt generation

        Parameters:
        -----------

        low:  Low threshold to generate an interrupt

        med:  Medium threshold to generate an interrupt

        high:  High threshold to generate an interrupt 
        """
        return _pyupm_hp20x.HP20X_setTemperatureThreshholds(self, *args)

HP20X_swigregister = _pyupm_hp20x.HP20X_swigregister
HP20X_swigregister(HP20X)

# This file is compatible with both classic and new-style classes.


