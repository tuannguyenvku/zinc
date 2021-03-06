import subprocess
from zinc.compil import CompilationError, BaseDeclare

from . import codegen as codegen
from .rename import rename

DESCRIPTION = "CoffeeScript backend (http://coffeescript.org)"
OPTIONS = {"libpath": ("path to ZINC's CoffeeScript library", "."),
           "main": ("whether to generate a main function", False)}

NONETYPE = True
BOOL = "Boolean"
EXT = ".coffee"
INMEM = False

def and_ (left, *others) :
    seen = set([left])
    done = [left]
    for right in others :
        if right not in seen :
            done.append(right)
            seen.add(right)
    return " and ".join("(%s)" % d for d in done)

def union (left, *other) :
    types = set((left,) + other)
    if len(types) == 1 :
        return next(iter(types))
    else :
        return "object"

class Declare (BaseDeclare) :
    pass

def build (ast, src, name, **options) :
    try :
        subprocess.check_output(["coffee", src], stderr=subprocess.STDOUT)
    except Exception as err :
        out = err.output.decode()
        TODO
        for line in out.splitlines() :
            try :
                path, lineno, message = line.split(":", 2)
                if path.endswith(src) :
                    raise CompilationError(ast, name, message.strip(), int(lineno), out)
            except ValueError :
                continue
        raise CompilationError(ast, name, out)
