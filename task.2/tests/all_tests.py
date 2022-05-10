import unittest
from unittest import TestCase
import json
import qtoml
import yaml
import os
from factory.factory import *
from factory.json_parser import Json
from factory.yaml_parser import Yaml
from factory.toml_parser import Toml
from tests.obj import *
from serializer import *
import math


class Tests (TestCase):

    def test_dumps(self):
        coctail = Cocktail('strawberry', 350).__dict__
        json_parser = Json()
        self.assertEqual(json_parser.dumps(coctail), json.dumps(coctail))

    def test_func_dumps(self):
        json_parser = Json()
        sr = serialize(f)
        foo = deserialize(sr)
        self.assertEqual(foo(5), f(5))

    def test_loads(self):
        coctail = Cocktail('strawberry', 350).__dict__
        json_parser = Json()
        s = json_parser.dumps(coctail)
        self.assertEqual(json_parser.loads(s), json.loads(s))

    def test_toml_dumps(self):
        coctail = Cocktail('strawberry', 350).__dict__
        toml_parser = Toml()
        self.assertEqual(toml_parser.dumps(coctail), qtoml.dumps(coctail))

    def test_toml_dump(self):
        parser = Factory.create_serializer('toml')
        coctail = Cocktail('strawberry', 350).__dict__
        parser.dump(coctail, 'test1.toml')
        with open('test1.toml', 'r') as file:
            s1 = file.read()
        with open('test2.toml', 'w') as file:
            qtoml.dump(coctail, file)
        with open('test2.toml', 'r') as file:
            s2 = file.read()
        os.remove('test1.toml')
        os.remove('test2.toml')
        self.assertEqual(s1, s2)

    def tests_toml_load(self):
        parser = Factory.create_serializer('toml')
        coctail = Cocktail('strawberry', 350).__dict__
        sr = parser.dump(coctail, 'test1.toml')
        obj1 = parser.load('test1.toml')
        with open('test2.toml', 'w') as file:
            qtoml.dump(coctail, file)
        with open('test2.toml', 'r') as file:
            obj2 = qtoml.load(file)
        os.remove('test1.toml')
        os.remove('test2.toml')
        self.assertEqual(obj1, obj2)

    def test_toml_loads(self):
        coctail = Cocktail('strawberry', 350).__dict__
        toml_parser = Toml()
        s = toml_parser.dumps(coctail)
        self.assertEqual(toml_parser.loads(s), qtoml.loads(s))

    def tests_json_load(self):
        parser = Factory.create_serializer('json')
        coctail = Cocktail('strawberry', 350).__dict__
        sr = parser.dump(coctail, 'test1.json')
        obj1 = parser.load('test1.json')
        with open('test2.json', 'w') as file:
            json.dump(coctail, file)
        with open('test2.json', 'r') as file:
            obj2 = json.load(file)
        os.remove('test1.json')
        os.remove('test2.json')
        self.assertEqual(obj1, obj2)

    def tests_yaml_load(self):
        parser = Factory.create_serializer('yaml')
        coctail = Cocktail('strawberry', 350).__dict__
        sr = parser.dump(coctail, 'test1.yaml')
        obj1 = parser.load('test1.yaml')
        with open('test2.yaml', 'w') as file:
            yaml.dump(coctail, file)
        with open('test2.yaml') as file:
            obj2 = yaml.load(file, Loader=yaml.FullLoader)
        os.remove('test1.yaml')
        os.remove('test2.yaml')
        self.assertEqual(obj1, obj2)

    def tests_yaml_dump(self):
        coctail = Cocktail('strawberry', 350).__dict__
        parser = Factory.create_serializer('yaml')
        parser.dump(coctail, 'test1.yaml')
        with open('test2.yaml', 'w') as file:
            yaml.dump(coctail, file)

        with open('test1.yaml', 'r') as file:
            s1 = file.read()
        with open('test2.yaml', 'r') as file:
            s2 = file.read()
        os.remove('test1.yaml')
        os.remove('test2.yaml')
        self.assertEqual(s1, s2)


if __name__ == '__main__':
    unittest.main()