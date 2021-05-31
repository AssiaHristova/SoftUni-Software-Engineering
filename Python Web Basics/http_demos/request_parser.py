END_COMMAND = 'END'


def read_paths():
    paths = {
        'GET': [],
        'POST': []
    }
    while True:
        line = input()
        if line == END_COMMAND:
            break
        path= line[:line.rindex('/')]
        method = line[line.rindex('/') + 1:]
        paths[method.upper()].append(path)
    return paths


def read_request():
    method, path, *_ = input().split()
    return {'method': method,
            'path': path}


def make_request(paths, request):
    valid_paths_for_method = paths[request['method']]

    if request['path'] in valid_paths_for_method:
        return f'''HTTP/1.1 200 OK
Content-Length: 2
Content-Type: text/plain

OK
'''
    else:
        return f''''HTTP/1.1 404 Not Found
Content-Length: 9
Content-Type: text/plain

Not Found
'''


def solve():
    paths = read_paths()
    request = read_request()
    result = make_request(paths, request)
    print(result)


solve()

