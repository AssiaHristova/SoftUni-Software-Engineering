title = input()
content = input()
comments = input()

print(f'<h1>\n    {title}\n</h1>')
print(f'<article>\n    {content}\n</article>')

while not comments == "end of comments":
    print(f'<div>\n    {comments}\n</div>')
    comments = input()

