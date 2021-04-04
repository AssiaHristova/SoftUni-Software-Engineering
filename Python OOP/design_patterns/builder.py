from abc import ABC, abstractmethod
import os


class Logger(ABC):
    @abstractmethod
    def log(self, obj):
        pass


class FileLogger(Logger):
    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, obj):
        with open(self.file_path, 'a') as file:
            file.write(obj)
            file.write('\n')


class StdoutLogger(Logger):
    def log(self, obj):
        print(obj)


class LoggersBuilder:
    def __init__(self):
        self.file_path = None
        self.environment = 'dev'

    @property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, value):
        self.__environment = value

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value

#    def set_file_path(self, file_path):
 #       self.file_path = file_path
  #      self.environment = 'prod'

    def build(self):
        if self.environment == 'prod':
            return FileLogger(self.file_path)
        else:
            return StdoutLogger()


loggers_builder = LoggersBuilder()
#loggers_builder.set_file_path('./logs_2.txt')
loggers_builder.file_path = './logs_2.txt'
loggers_builder.environment = 'prod'
loggers_builder.build().log('It works with builders and properties')
