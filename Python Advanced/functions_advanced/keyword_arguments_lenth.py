def kwargs_length(**kwargs):
    keywords = []
    for key in kwargs.keys():
        keywords.append(key)
    return len(keywords)


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))
