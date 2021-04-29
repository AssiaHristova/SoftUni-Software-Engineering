from project_3.software.software import Software


class LightSoftware(Software):
    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super(LightSoftware, self).__init__(name, "Light", int(capacity_consumption * 1.5), int(memory_consumption * 0.5))
