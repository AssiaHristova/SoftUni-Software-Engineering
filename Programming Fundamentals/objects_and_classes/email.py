class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


command = input()
emails = []

while not command == "Stop":
    attributes = command.split()
    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

emails_to_send = list(map(int, input().split(', ')))

for i in emails_to_send:
    emails[i].send()

for email in emails:
    print(email.get_info())







