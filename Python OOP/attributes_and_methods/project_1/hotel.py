from project_1.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        filtered_rooms = [room for room in self.rooms if room.number == room_number]
        if filtered_rooms:
            room = filtered_rooms[0]
            guests = room.take_room(people)
            if not guests == f"Room number {room.number} cannot be taken":
                self.guests += guests

    def free_room(self, room_number):
        filtered_rooms = [room for room in self.rooms if room.number == room_number]
        if filtered_rooms:
            room = filtered_rooms[0]
            guests_to_leave = room.free_room()
            if not guests_to_leave == f"Room number {room.number} is not taken":
                self.guests -= guests_to_leave

    def print_status(self):
        free_rooms = [room for room in self.rooms if not room.is_taken]
        free_room_numbers = ', '.join(str(room.number) for room in free_rooms)
        taken_rooms = [room for room in self.rooms if room.is_taken]
        taken_room_numbers = ', '.join(str(room.number) for room in taken_rooms)
        result = f'Hotel {self.name} has {self.guests} total guests\nFree rooms: {free_room_numbers}\nTaken rooms: {taken_room_numbers}'
        print(result)
