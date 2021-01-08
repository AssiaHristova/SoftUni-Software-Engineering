class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes


comment_1 = Comment('user_1', 'I like this book')
print(comment_1.username)
print(comment_1.content)
print(comment_1.likes)
