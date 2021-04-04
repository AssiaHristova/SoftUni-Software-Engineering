import json
from abc import ABC, abstractmethod


class ServiceResult:
    def __init__(self, is_valid, errors):
        self.is_valid = is_valid
        self.errors = errors

    @classmethod
    def valid(cls):
        return cls(True, None)
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_with_name(cls, name):
        return cls(name, 0)


class Parser(ABC):
    @abstractmethod
    def parse(self, obj):
        pass


class JsonParser(Parser):
    def parse(self, obj):
        return json.dumps(obj.__dict__)


class CsvParser(Parser):
    def parse(self, obj):
        header = obj.__dict__.keys()
        header_2 = obj.__dict__.values()
        result = [', '.join(header), ', '.join([str(x) for x in header_2])]
        return '\n'.join(result)


class StringParser(Parser):
    def parse(self, obj):
        return str(obj)


class ParserFactory:
    def get_parser(self, format):
        if format == 'json':
            return JsonParser()
        elif format == 'csv':
            return CsvParser()
        else:
            return StringParser()


class ParserSimpleFactory:
    def get_csv(self):
        return CsvParser()

    def get_json(self):
        return JsonParser()


person = Person('Pesho', 11)
parser_factory = ParserFactory()

format = input()

parser = parser_factory.get_parser(format)
result = parser.parse(person)

print(result)
