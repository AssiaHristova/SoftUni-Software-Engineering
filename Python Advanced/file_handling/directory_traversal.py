import os
from os import listdir
from os.path import isfile, join


def create_directory(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        pass


def search_directory(directory):
    extensions = {}
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    for file in files:
        extension = file.split('.')[1]
        if extension in extensions:
            extensions[extension].append(file)
        else:
            extensions[extension] = [file]
    return extensions


def create_file(file_name):
    with open(file_name, 'w') as file:
        file.write('')


def report_of_files(extensions):
    with open('C:\\Users\Hp\Desktop\'report.txt', 'w') as file:
        for extension in extensions:
            file.write('.' + extension[0] + '\n')
            file.write('- - - ' + '\n- - - '.join(extension[1]) + '\n')


create_directory('example/')

create_file('example/index.html')
create_file('example/index.js')
create_file('example/python.py')
create_file('example/demo.pptx')
create_file('example/log.txt')
create_file('example/notes.txt')
create_file('example/program.py')

search_directory('example/')

extensions = search_directory('example/')

sorted_extensions = sorted(extensions.items(), key=lambda x: x[0])

report_of_files(sorted_extensions)
