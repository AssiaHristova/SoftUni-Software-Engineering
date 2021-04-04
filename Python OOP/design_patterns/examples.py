class JsonParser:
    def parse(self, obj):
        return f'json: {str(obj)}'


parser = JsonParser()
parser_1 = JsonParser()

print(id(parser))
print(id(parser_1))

