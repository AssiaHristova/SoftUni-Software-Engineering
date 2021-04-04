def singleton(cls):
    instance = None

    def wrapper(*args, **kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args, **kwargs)
        return instance

    return wrapper


@singleton
class JsonParser2:
    def parse(self, obj):
        return f'json: {str(obj)}'


print(id(JsonParser2()))
print(id(JsonParser2()))
