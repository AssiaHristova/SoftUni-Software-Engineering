class Hardware:
    def __init__(self, name: str, type: str, capacity: int, memory: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    @property
    def available_memory(self):
        return self.memory - sum([s.memory_consumption for s in self.software_components])

    @property
    def available_capacity(self):
        return self.capacity - sum([s.capacity_consumption for s in self.software_components])

    def install(self, software):
        if self.available_capacity < software.capacity_consumption or self.available_memory < software.memory_consumption:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software):
        if software in self.software_components:
            self.software_components.remove(software)


