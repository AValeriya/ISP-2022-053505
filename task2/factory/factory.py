from factory.Yaml_parser import Yaml
from factory.Toml_parser import Toml
from factory.Json_parser import Json

PARSERS = {
    'json': Json,
    'yml': Yaml,
    'toml': Toml
}


class Factory(object):
    @staticmethod
    def create_serializer(file_format: str):
        if file_format=='json':
            parser = Json
        if file_format=='toml':
            parser = Toml
        if file_format=='yaml':
            parser = Yaml
        return parser()