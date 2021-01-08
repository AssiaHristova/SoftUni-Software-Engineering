def add(emails, username):
    if username in emails:
        print(f'{username} is already registered')
    else:
        emails[username] = []
    return emails


def send(emails, username, email):
    if username in emails:
        emails[username].append(email)
    return emails


def delete(emails, username):
    if username in emails:
        emails.pop(username)
    else:
        print(f'{username} not found!')
    return emails

line = input()

emails = {}

while not line == 'Statistics':
    command = line.split('->')
    if command[0] == 'Add':
        username = command[1]
        emails = add(emails, username)
    elif command[0] == 'Send':
        username = command[1]
        email = command[2]
        emails = send(emails, username, email)
    elif command[0] == 'Delete':
        username = command[1]
        emails = delete(emails, username)

    line = input()

sorted_emails = sorted(emails.items(), key=lambda x: (-len(x[1]), x[0]))

print(f'Users count: {len(emails)}')
for username in sorted_emails:
    print(f'{username[0]}')
    print(' - ', end='')
    print(f"\n{' - '.join(username[1])}")

