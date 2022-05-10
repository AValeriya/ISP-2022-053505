from serializer import *
import inspect
import yaml
import os
from factory.abs_parser import Parser


class Yaml (Parser):

    def dump(self, obj, fp):
        if inspect.isroutine(obj):
            obj = serialize(obj)
        with open(fp, 'w') as f:
            yaml.dump(obj, f)
        return fp

    def dumps(self, obj):
        if inspect.isroutine(obj):
            obj = serialize(obj)
        fp = self.dump(obj, 'temp.json')
        with open(fp, 'r') as f:
            t = f.read()
        os.remove('temp.json')
        return t

    def load(self, fp):
        with open(fp, 'r') as f:
            t = yaml.load(f, Loader=yaml.FullLoader)
        return deserialize(t)

    def loads(self, s):
        with open('temp.json', 'w') as f:
            f.write(s)
        t = self.load('temp.json')

        os.remove('temp.json')
        return t