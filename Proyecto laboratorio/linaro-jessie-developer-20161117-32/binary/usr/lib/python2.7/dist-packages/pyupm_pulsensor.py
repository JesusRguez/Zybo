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
            fp, pathname, description = imp.find_module('_pyupm_pulsensor', [dirname(__file__)])
        except ImportError:
            import _pyupm_pulsensor
            return _pyupm_pulsensor
        if fp is not None:
            try:
                _mod = imp.load_module('_pyupm_pulsensor', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pyupm_pulsensor = swig_import_helper()
    del swig_import_helper
else:
    import _pyupm_pulsensor
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


HIGH = _pyupm_pulsensor.HIGH
LOW = _pyupm_pulsensor.LOW
TRUE = _pyupm_pulsensor.TRUE
FALSE = _pyupm_pulsensor.FALSE
class clbk_data(_object):
    """
    Callback data struct

    C++ includes: pulsensor.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, clbk_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, clbk_data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["is_heart_beat"] = _pyupm_pulsensor.clbk_data_is_heart_beat_set
    __swig_getmethods__["is_heart_beat"] = _pyupm_pulsensor.clbk_data_is_heart_beat_get
    if _newclass:is_heart_beat = _swig_property(_pyupm_pulsensor.clbk_data_is_heart_beat_get, _pyupm_pulsensor.clbk_data_is_heart_beat_set)
    def __init__(self): 
        """
        __init__(clbk_data self) -> clbk_data

        Callback data struct

        C++ includes: pulsensor.h 
        """
        this = _pyupm_pulsensor.new_clbk_data()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pyupm_pulsensor.delete_clbk_data
    __del__ = lambda self : None;
clbk_data_swigregister = _pyupm_pulsensor.clbk_data_swigregister
clbk_data_swigregister(clbk_data)

class Pulsensor(_object):
    """
    C++ API for the 3-Wire Pulse Sensor.

    ID: pulsensor

    Name: Pulse Sensor

    Category: medical

    Manufacturer: seeed

    Link:http://www.adafruit.com/products/1093

    Connection: analog  This is a library for a 3-wire pulse sensor sold
    by several manufacturers. Usually, you can identify the sensor based
    on the round breakout and the distinctive heart symbol.

    C++ includes: pulsensor.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Pulsensor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Pulsensor, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(upm::Pulsensor self, callback_handler handler) -> Pulsensor

        Parameters:
            handler: callback_handler


        Pulsensor(callback_handler handler) 
        """
        this = _pyupm_pulsensor.new_Pulsensor(*args)
        try: self.this.append(this)
        except: self.this = this
    def start_sampler(self):
        """
        start_sampler(Pulsensor self)

        Parameters:
            self: upm::Pulsensor *


        void
        start_sampler() 
        """
        return _pyupm_pulsensor.Pulsensor_start_sampler(self)

    def stop_sampler(self):
        """
        stop_sampler(Pulsensor self)

        Parameters:
            self: upm::Pulsensor *


        void
        stop_sampler() 
        """
        return _pyupm_pulsensor.Pulsensor_stop_sampler(self)

    __swig_destroy__ = _pyupm_pulsensor.delete_Pulsensor
    __del__ = lambda self : None;
Pulsensor_swigregister = _pyupm_pulsensor.Pulsensor_swigregister
Pulsensor_swigregister(Pulsensor)

# This file is compatible with both classic and new-style classes.


