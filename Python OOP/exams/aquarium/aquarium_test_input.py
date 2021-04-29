

controller = Controller()
print(controller.add_aquarium('SaltwaterAquarium', 'salt'))
print(controller.add_decoration('Plant'))
print(controller.insert_decoration('salt', 'Plant'))
print(controller.add_fish('salt', 'SaltwaterFish', 'dorry', 'saltfish', 20))
print(controller.feed_fish('salt'))
print(controller.calculate_value('salt'))
print(controller.report())

