import csv
import io
from abc import ABC, abstractmethod
from pyfiglet import figlet_format


class Logger(ABC):
    @abstractmethod
    def log(self, obj):
        pass


class StdoutLogger(Logger):
    def log(self, obj):
        print(obj)


class PyFigletLogger(Logger):
    def __init__(self):
        self.logger = StdoutLogger()

    def log(self, obj):
        return self.logger.log(figlet_format(obj))


PyFigletLogger().log('It works!')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Parser(ABC):
    @abstractmethod
    def parse(self, obj):
        pass


class CsvParser(Parser):
    def parse(self, obj):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(obj.__dict__.keys())
        writer.writerow(obj.__dict__.values())
        return output.getvalue()


person = Person('Pesho', 11)
parser = CsvParser().parse(person)
print(parser)






