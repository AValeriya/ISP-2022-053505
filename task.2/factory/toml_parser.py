from serializer import *
import inspect
import qtoml
from factory.abs_parser import Parser


class Toml (Parser):

    def dump(self, obj, fp):
        with open(fp, 'w') as f:
            f.write(self.dumps(obj))
        return fp

    def dumps(self, obj):
        if inspect.isroutine(obj):
            obj = serialize(obj)

        return qtoml.dumps(obj, encode_none='None')

    def load(self, fp):
        with open(fp, 'r') as f:
            s = f.read()
        return qtoml.loads(s)

    def loads(self, s):
        return deserialize(qtoml.loads(s))