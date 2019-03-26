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
            fp, pathname, description = imp.find_module('_pyupm_mq303a', [dirname(__file__)])
        except ImportError:
            import _pyupm_mq303a
            return _pyupm_mq303a
        if fp is not None:
            try:
                _mod = imp.load_module('_pyupm_mq303a', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyupm_mq303a = swig_import_helper()
    del swig_import_helper
else:
    import _pyupm_mq303a
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


class MQ303A(_object):
    """
    API for the MQ303A Alcohol Sensor.

    ID: mq303a

    Name: MQ303A Alcohol Sensor

    Other Names: Grove Alcohol Sensor

    Category: gaseous

    Manufacturer: seeed

    Link:http://www.seeedstudio.com/wiki/Grove_-_Alcohol_Sensor

    Connection: analog gpio

    Kit: tsk  UPM module for the MQ303A alcohol sensor. This sensor needs
    to be warmed up before stable results are obtained. The higher the
    value returned from value(), the higher the amount of alcohol
    detected.

    C++ includes: mq303a.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MQ303A, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MQ303A, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(upm::MQ303A self, int pin, int heaterPin) -> MQ303A

        Parameters:
            pin: int
            heaterPin: int


        MQ303A(int pin, int
        heaterPin)

        MQ303A constructor

        Parameters:
        -----------

        pin:  Analog pin to use

        heaterPin:  Digital pin mapped to the analog pin to use 
        """
        this = _pyupm_mq303a.new_MQ303A(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyupm_mq303a.delete_MQ303A
    __del__ = lambda self : None;
    def value(self):
        """
        value(MQ303A self) -> int

        Parameters:
            self: upm::MQ303A *


        int value()

        Gets the alcohol reading from the sensor. The value read from the
        analog pin is inverted. A higher returned value means a higher amount
        of alcohol detected.

        Alcohol reading 
        """
        return _pyupm_mq303a.MQ303A_value(self)

    def heaterEnable(self, *args):
        """
        heaterEnable(MQ303A self, bool enable)

        Parameters:
            enable: bool


        void
        heaterEnable(bool enable)

        Enables the heater

        Parameters:
        -----------

        enable:  Enables the heater if true; otherwise, disables it 
        """
        return _pyupm_mq303a.MQ303A_heaterEnable(self, *args)

MQ303A_swigregister = _pyupm_mq303a.MQ303A_swigregister
MQ303A_swigregister(MQ303A)

# This file is compatible with both classic and new-style classes.


