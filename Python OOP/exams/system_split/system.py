from project_3.hardware.heavy_hardware import HeavyHardware
from project_3.hardware.power_hardware import PowerHardware
from project_3.software.light_software import LightSoftware
from project_3.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name:str, capacity:int, memory:int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        searched_hardwares = [h for h in System._hardware if h.name == hardware_name]
        if not searched_hardwares:
            return "Hardware does not exist"
        searched_hardware = searched_hardwares[0]
        express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            searched_hardware.install(express_software)
            System._software.append(express_software)
        except Exception as exception:
            return str(exception)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        searched_hardwares = [h for h in System._hardware if h.name == hardware_name]
        if not searched_hardwares:
            return "Hardware does not exist"
        searched_hardware = searched_hardwares[0]
        light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            searched_hardware.install(light_software)
            System._software.append(light_software)
        except Exception as exception:
            return str(exception)

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        hardwares = [h for h in System._hardware if h.name == hardware_name]
        softwares = [s for s in System._software if s.name == software_name]
        if not hardwares or not softwares:
            return "Some of the components do not exist"
        hardware = hardwares[0]
        software = softwares[0]
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory = sum([h.memory for h in System._hardware])
        total_used_memory = sum([s.memory_consumption for s in System._software])
        total_capacity = sum([h.capacity for h in System._hardware])
        total_used_space = sum([s.capacity_consumption for s in System._software])
        result = 'System Analysis\n'
        result += f'Hardware Components: {len(System._hardware)}\n'
        result += f'Software Components: {len(System._software)}\n'
        result += f'Total Operational Memory: {total_used_memory} / {total_memory}\n'
        result += f'Total Capacity Taken: {total_used_space} / {total_capacity}'
        return result

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            express_software_components = [s for s in hardware.software_components if s.type == "Express"]
            light_software_components = [s for s in hardware.software_components if s.type == "Light"]
            software_components_names = [s.name for s in hardware.software_components]
            if not software_components_names:
                software_components_names = [None]
            result += f'Hardware Component - {hardware.name}\n'
            result += f'Express Software Components: {len(express_software_components)}\n'
            result += f'Light Software Components: {len(light_software_components)}\n'
            result += f'Memory Usage: {hardware.memory - hardware.available_memory} / {hardware.memory}\n'
            result += f'Capacity Usage: {hardware.capacity - hardware.available_capacity} / {hardware.capacity}\n'
            result += f'Type: {hardware.type}\n'
            result += f'Software Components: {", ".join(software_components_names)}'
        return result



System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
print(System.register_express_software("HDD", "Test2", 100, 100))
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)
print(System.analyze())
System.release_software_component("SSD", "Linux")
print(System.system_split())




