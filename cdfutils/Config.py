#
#   Module:     Config
#   Platform:   Python 2.7, 3.7
#
#   A generic configuration class that persists values in a file.
#
#   Copyright Craig Farrow, 2010 - 2019
#

import configparser

# ------------------------------------------------------------------

class ConfigStore(object):
    """
    A generic configuration class that persists the values in a text file.
    - A file name can be specified in the constructor, otherwise the
      default name "config.ini" is used.
    - Values are simply accessed as members of the class, e.g.:
           Config = ConfigStore()
           Config.username = "Fred"
           Config.email = "fred@rubble.com"
           DoSomething(Config.username, Config.email)
    - Undefined values default to None:
           >>> type(Config.notusedbefore)
           <type 'NoneType'>
    - Supports any native Python type.
    Limitations:
    - Values can be modified by assignment operations only. E.g.:
            Config.int += 1             # Works
            Config.list.append("new")   # Doesn't work
    """
    def __init__(self, fileName="config.ini"):
        object.__setattr__(self, "__FNAME", fileName)
        cp = configparser.ConfigParser(interpolation=None,
                                       allow_no_value=True)
        object.__setattr__(self, "__cp", cp)
        cp.read(object.__getattribute__(self, "__FNAME"))

    def __setattr__(self, key, value):
        cp = object.__getattribute__(self, "__cp")
        cp.set(configparser.DEFAULTSECT, key, repr(value))

    def __getattr__(self, key):
        if key.startswith("__"):
            return object.__getattribute__(self, key)
        cp = object.__getattribute__(self, "__cp")
        if not cp.has_option(configparser.DEFAULTSECT, key):
            cp.set(configparser.DEFAULTSECT, key, None)
        val = cp.get(configparser.DEFAULTSECT, key)
        if val is None:
            return None
        else:
            return eval(val)

    def __delattr__(self, key):
        cp = object.__getattribute__(self, "__cp")
        if cp.has_option(configparser.DEFAULTSECT, key):
            cp.remove_option(configparser.DEFAULTSECT, key)

    def items(self):
        """
        Get all the (item, value) pairs.
        """
        cp = object.__getattribute__(self, "__cp")
        return cp.items(configparser.DEFAULTSECT)

    def __del__(self):
        f = open(object.__getattribute__(self, "__FNAME"), "w")
        cp = object.__getattribute__(self, "__cp")
        cp.write(f)
        f.close()
