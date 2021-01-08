class Party:
    def __init__(self, people):
        self.people = []


names = input()
party = Party(names)

while not names == "End":
    party.people.append(names)
    names = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
