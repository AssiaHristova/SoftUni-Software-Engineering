from urllib import parse


def get_protocol(scheme):
    if scheme in ('http', 'https'):
        return scheme
    return None


def get_host_and_port(netloc, scheme):
    if '.' not in netloc:
        return None, None
    if ':' not in netloc:
        default_port = 80 if scheme == 'http' else 443
        netloc = f'{netloc}:{default_port}'
    host, port = netloc.split(':')
    return host, port


def get_path(path):
    return path or '/'


def get_fragment(fragment):
    return fragment


def get_query(query):
    return query


def validate_url(url):
    components = parse.urlparse(url)
    protocol = get_protocol(components.scheme)
    host, port = get_host_and_port(components.netloc, components.scheme)
    path = get_path(components.path)
    query = get_query(components.query)
    fragment = get_fragment(components.fragment)
    if None in (protocol, host, port, path):
        return f'''_____________
URL: {url}
Invalid URL'''
    return f'''_____________
URL: {url}
Protocol: {protocol}
Host: {host}
Port: {port}
Path: {path}
Query: {query}
Fragment: {fragment}'''

urls = [
    'http://softuni.bg/',
    'https://softuni.bg:447/search?Query=pesho&Users=true#go',
    'http://google:443/',
]

for url in urls:
    print(validate_url(url))
