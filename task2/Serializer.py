import inspect
import types
import builtins
import importlib


def serialize(obj):

    def serialize_func(item):
        parts = []
        result = {}
        for i in inspect.getmembers(item):
            if i[0].startswith('co'):
                if i[0] == 'co_lines':
                    continue
                else:
                    parts.append(i)

        for i in parts:
            result[serialize(i[0])] = serialize(i[1])
        return result

    if isinstance(obj, (int, str, float, bool)):
        return obj

    if isinstance(obj, dict):
        temp = {}                              #slovar
        for key, value in obj.items():
            temp[serialize(key)] = serialize(value)
        return {'dict': temp}

    if isinstance(obj, (list, tuple)):
        temp = {}
        key = "list"                       #kluch is slovo list
        temp[key] = []
        for value in obj:
            temp[key].append(serialize(value))
        return temp

    if isinstance(obj, tuple):
        temp = {}
        key = "tuple"
        temp[key] = []
        for value in obj:
            temp[key].append(serialize(value))
        return tuple(temp)

    if isinstance(obj, types.FunctionType):
        key = "func"
        return {key: serialize(obj.__code__)}

    if isinstance(obj, types.CodeType):
        key = "code"
        return {key: serialize_func(obj)}

    if isinstance(obj, bytes):
        key = "bytes"
        return {key: obj.hex()}


def deserialize(obj):
    temp_dict = {}
    if isinstance(obj, (int, str, float)):
        return obj
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if key == 'func':
                import __main__
                globals().update(__main__.__dict__)
                def func(): pass
                func.__code__ = deserialize(value)
                return func
            elif key == 'list':
                return deserialize(value)
            elif key == 'bytes':
                return bytes.fromhex(value)
            elif key == 'code':
                code_names = deserialize(value["co_names"])

                for name in code_names:
                    if builtins.__dict__.get(name, 42) == 42:
                        try:
                            builtins.__dict__[name] = importlib.import_module(name)
                        except ModuleNotFoundError:
                            builtins.__dict__[name] = 42
                return types.CodeType(
                    deserialize(value["co_argcount"]),
                    deserialize(value["co_posonlyargcount"]),
                    deserialize(value["co_kwonlyargcount"]),
                    deserialize(value["co_nlocals"]),
                    deserialize(value["co_stacksize"]),
                    deserialize(value["co_flags"]),
                    deserialize(value["co_code"]),
                    tuple(deserialize(value["co_consts"])),
                    tuple(code_names),
                    tuple(deserialize(value["co_varnames"])),
                    deserialize(value["co_filename"]),
                    deserialize(value["co_name"]),
                    deserialize(value["co_firstlineno"]),
                    deserialize(value["co_lnotab"]),
                    tuple(deserialize(value["co_freevars"])),
                    tuple(deserialize(value["co_cellvars"]))
                )
            else:
                temp_dict[deserialize(key)] = deserialize(value)

    elif isinstance(obj, list):
        temp_list = []
        for item in obj:
            temp_list.append(deserialize(item))
        return temp_list

    elif isinstance(obj, tuple):
        temp_list = []
        for item in obj:
            temp_list.append(deserialize(item))
        return tuple(temp_list)

    return temp_dict