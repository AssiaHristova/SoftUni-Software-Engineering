from abc import ABC, abstractmethod


def encrypted(func):

    def wrapper(self, text):
        return func(self, f'$$${text}$$$')

    return wrapper


class DataSource(ABC):
    @abstractmethod
    def write(self, text):
        pass


class FileDataSource(DataSource):
    def __init__(self, file_nme):
        self.file_nme = file_nme

    @encrypted
    def write(self, text):
        with open(self.file_nme, 'a') as file:
            file.write(text)
            file.write('\n')


class EncryptedFileDataSource(FileDataSource):
    def write(self, text):
        encrypted_text = f'____{text}____'
        return super().write(encrypted_text)


fds = FileDataSource('./logs.txt')
fds.write('It works')

efds = EncryptedFileDataSource('./logs.txt')
efds.write('It works')


