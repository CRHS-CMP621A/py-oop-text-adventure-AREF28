class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.all_items = {}

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def add_item(self, item_obj, item_name):
        self.all_items[item_name] = item_obj

    def remove_item(self, item_name):
        del self.all_items[item_name]

    def get_details(self):
        print("\n" + self.name)
        print("-------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)
        for item_name in self.all_items:
            item_obj = self.all_items[item_name]
            print("There is a " + item_name + ":" + item_obj.description)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        elif direction in self.all_items:
            item_obj = self.all_items[direction]
            # Add code here to 'do stuff' with the item
            print(item_obj.description)
            return self
        else:
            print("You can't go that way")
            return self
