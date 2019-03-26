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
            fp, pathname, description = imp.find_module('_pyupm_teams', [dirname(__file__)])
        except ImportError:
            import _pyupm_teams
            return _pyupm_teams
        if fp is not None:
            try:
                _mod = imp.load_module('_pyupm_teams', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyupm_teams = swig_import_helper()
    del swig_import_helper
else:
    import _pyupm_teams
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


TEAMS_DEFAULT_AREF = _pyupm_teams.TEAMS_DEFAULT_AREF
class TEAMS(_object):
    """
    API for the Veris TEAMS Temperature Transmitter.

    ID: teams

    Name: Veris TEAMS Temperature Transmitter

    Category: temp

    Manufacturer: veris

    Connection: ainput

    Link:http://www.veris.com/Item/TEAMS.aspx  The Veris TEAMS temperature
    sensor provides it's output via a 4-20ma current loop. The supported
    temperature range is 10C to 35C.

    This sensor was developed with a Cooking Hacks (Libelium) 4-channel
    4-20ma Arduino interface shield. For this interface, the receiver
    resistance (rResistor) was specified as 165.0 ohms.

    When using a 4-20ma current loop interface which scales the sensors'
    values to a 0-5vdc range, you can supply 0.0 as the rResistor value in
    the constructor (default), and it will act just like a normal analog
    input.

    C++ includes: teams.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TEAMS, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TEAMS, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(upm::TEAMS self, int tPin, float rResistor=0.0, float aref=5.0) -> TEAMS

        Parameters:
            tPin: int
            rResistor: float
            aref: float

        __init__(upm::TEAMS self, int tPin, float rResistor=0.0) -> TEAMS

        Parameters:
            tPin: int
            rResistor: float

        __init__(upm::TEAMS self, int tPin) -> TEAMS

        Parameters:
            tPin: int


        TEAMS(int tPin, float
        rResistor=0.0, float aref=TEAMS_DEFAULT_AREF)

        TEAMS object constructor

        Parameters:
        -----------

        tPin:  Analog pin to use for temperature.

        rResistor:  The receiver resistance in ohms, when using a 4-20ma
        current loop interface. When specified, this value will be used in
        computing the current based on the voltage read when scaling the
        return values. Default is 0.0, for standard scaling based on voltage
        output rather than current (4-20ma mode).

        aref:  The analog reference voltage, default 5.0 
        """
        this = _pyupm_teams.new_TEAMS(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyupm_teams.delete_TEAMS
    __del__ = lambda self : None;
    def update(self):
        """
        update(TEAMS self)

        Parameters:
            self: upm::TEAMS *


        void update()

        Read current values from the sensor and update internal stored values.
        This method must be called prior to querying any values, such as
        temperature. 
        """
        return _pyupm_teams.TEAMS_update(self)

    def getTemperature(self, fahrenheit=False):
        """
        getTemperature(TEAMS self, bool fahrenheit=False) -> float

        Parameters:
            fahrenheit: bool

        getTemperature(TEAMS self) -> float

        Parameters:
            self: upm::TEAMS *


        float
        getTemperature(bool fahrenheit=false)

        Get the current temperature. update() must have been called prior to
        calling this method.

        Parameters:
        -----------

        fahrenheit:  true to return the temperature in degrees fahrenheit,
        false to return the temperature in degrees celcius. The default is
        false (degrees Celcius).

        The last temperature reading in Celcius or Fahrenheit 
        """
        return _pyupm_teams.TEAMS_getTemperature(self, fahrenheit)

    def isConnected(self):
        """
        isConnected(TEAMS self) -> bool

        Parameters:
            self: upm::TEAMS *


        bool isConnected()

        When using a direct 4-20ma interface (rResistor supplied in the
        constructor is >0.0), this function will return false when the
        computed milliamps falls below 4ma, indicating that the sensor is not
        connected. If rResistor was specified as 0.0 in the constructor, this
        function will always return true.

        true if the sensor is connected, false otherwise. 
        """
        return _pyupm_teams.TEAMS_isConnected(self)

    def getRawMilliamps(self):
        """
        getRawMilliamps(TEAMS self) -> float

        Parameters:
            self: upm::TEAMS *


        float
        getRawMilliamps()

        When using a direct 4-20ma interface (rResistor supplied in the
        constructor is >0.0), this function will return the computed milliamps
        (after the offset has been applied). If rResistor was specified as 0.0
        in the constructor, this function will always return 0.0.

        The last measured current in milliamps after any offset has been
        applied. 
        """
        return _pyupm_teams.TEAMS_getRawMilliamps(self)

    def setOffsetMilliamps(self, *args):
        """
        setOffsetMilliamps(TEAMS self, float offset)

        Parameters:
            offset: float


        void
        setOffsetMilliamps(float offset)

        Specify an offset in milliamps to be applied to the computed current
        prior to scaling and conversion. This can be used to 'adjust' the
        computed value. If rResistor was specified as 0.0 in the constructor,
        this function will have no effect.

        Parameters:
        -----------

        offset:  a positive or negative value that will be applied to the
        computed current measured. 
        """
        return _pyupm_teams.TEAMS_setOffsetMilliamps(self, *args)

TEAMS_swigregister = _pyupm_teams.TEAMS_swigregister
TEAMS_swigregister(TEAMS)

# This file is compatible with both classic and new-style classes.


