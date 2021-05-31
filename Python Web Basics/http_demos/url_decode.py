from urllib import parse

urls = [
    ('http://www.google.bg/search?q=C%23', 'http://www.google.bg/search?q=C#'),
    ('https://mysite.com/show?n%40m3=p3%24h0', 'https://mysite.com/show?n@m3=p3$h0'),
    ('http://url-decoder.com/i%23de%25?id=23', 'http://url-decoder.com/i#de%?id=23'),
    ('http://url-decoder.com/name=Assia%20Hristova', 'http://url-decoder.com/name=Assia Hristova')
]

for (url, expected) in urls:
    actual = parse.unquote(url)
    print(f'{expected==actual}: {expected}, {actual}')
