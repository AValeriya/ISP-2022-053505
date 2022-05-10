from factory.abs_parser import Parser
from Serializer import *
from ast import literal_eval


class Json(Parser):

    def dump(self, obj, fp):
        s = self.dumps(obj)
        with open(fp, 'w') as f:
            f.write(s)
        return fp

    def dumps(self, obj):
        s = serialize(obj)

        def my_dumps(s):
            text = ""
            if isinstance(s, dict):
                for key, val in s.items():
                    if key == 'dict':
                        text += "{"
                        text += my_dumps(val)
                        text = text.rstrip(text[-1])
                        text = text.rstrip(text[-1])
                        text += "}"
                    elif key == 'list':
                        text += '['
                        if len(val) != 0:
                            for item in val:
                                if item is None:
                                    text += 'None, '
                                    continue
                                else:
                                    text += my_dumps(item) + ', '
                            text = text.rstrip(text[-1])
                            text = text.rstrip(text[-1])
                        text += ']'
                    elif key == 'func':
                        text += "{"
                        text += my_dumps(key) + ": " + my_dumps(val) + ', '
                        text = text.rstrip(text[-1])
                        text = text.rstrip(text[-1])
                        text += '}'
                    elif key == 'code':
                        text += "{"
                        text += my_dumps(key) + ": " + '{' + my_dumps(val)
                        text = text.rstrip(text[-1])
                        text = text.rstrip(text[-1])
                        text += '}'
                        text += '}'
                    elif key == 'bytes':
                        text += '{' + my_dumps(key) + ': ' + my_dumps(val) + '}'
                    else:
                        text += my_dumps(key) + ": " + my_dumps(val) + ", "

            elif isinstance(s, str):
                text += '\"' + str(s) + '\"'

            elif isinstance(s, (int, float)):
                text += str(s)

            elif isinstance(s, list):
                if len(s) != 0:
                    for item in s:
                        text += my_dumps(item) + ', '
                    text = text.rstrip(text[-1])
                    text = text.rstrip(text[-1])

            return text       #метод возвращает json строку
        return my_dumps(s)

    def load(self, fp):
        with open(fp, 'r') as f:
            s = f.read()
        return self.loads(s)

    def loads(self, s):
        s_dict = literal_eval(s)
        return deserialize(s_dict)