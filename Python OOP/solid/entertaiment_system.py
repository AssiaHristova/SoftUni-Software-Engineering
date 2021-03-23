from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def plug_in_power(self):
        pass


class HDMIConnectable:
    def connect_via_hdmi(self, device):
        pass


class RCAConnectable:
    def connect_via_rca(self, device):
        pass


class EthernetConnectable:
    def connect_via_ethernet_cable(self, device):
        pass


class TV(Device, HDMIConnectable, RCAConnectable):
    def connect_to_DVD_player(self, dvd_player):
        self.connect_via_rca(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_via_hdmi(game_console)

    def plug_in_power(self):
        return 'Plugged in'


class DVDPlayer(Device, HDMIConnectable):
    def connect_to_tv(self, device):
        self.connect_via_hdmi(device)

    def plug_in_power(self):
        return 'Plugged in'


class GameConsole(Device, EthernetConnectable, HDMIConnectable):
    def connect_to_tv(self, device):
        self.connect_via_hdmi(device)

    def connect_to_router(self, device):
        self.connect_via_ethernet_cable(device)

    def plug_in_power(self):
        return 'Plugged in'


class Router(Device, EthernetConnectable):
    def connect_to_tv(self, device):
        self.connect_via_ethernet_cable(device)

    def connect_to_dvd_player(self, device):
        self.connect_via_ethernet_cable(device)


tv = TV()
tv.plug_in_power()
dvd = DVDPlayer()
tv.connect_via_hdmi(dvd)

