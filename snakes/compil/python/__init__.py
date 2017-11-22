import types, traceback, sys, importlib
from snakes.compil import CompilationError, BaseDeclare

from . import codegen as codegen
from .rename import rename

NONETYPE = True
BOOL = "bool"
EXT = ".py"
INMEM = True

class Declare (BaseDeclare) :
    pass

def build (ast, src, name) :
    if isinstance(src, str) :
        src = open(src)
    ctx = {}
    try :
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
    except Exception as err :
        c, v, t = sys.exc_info()
        msg = traceback.format_exception_only(c, v)
        if hasattr(err, "lineno") and hasattr(err, "offset") :
            loc = (err.lineno - 1, err.offset -1)
        else :
            tb = t
            while tb.tb_next :
                tb = tb.tb_next
            loc = tb.tb_lineno
        raise CompilationError(ast, name, msg[-1], loc, "".join(msg).rstrip())
    return mod
