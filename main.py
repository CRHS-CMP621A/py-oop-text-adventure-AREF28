from room import Room
# You would also import the Item class here once created (e.g., from item import Item)

# Create the room objects
kitchen = Room("Kitchen")
dining_hall = Room("Dining Hall")
ballroom = Room("Ballroom")

# Set descriptions for the rooms
kitchen.set_description("A dank and dirty room buzzing with flies.")
dining_hall.set_description("A large room with ornate golden decorations on every wall.")
ballroom.set_description("A vast room with a shiny wooden floor.")

# Link the rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Main game loop
current_room = kitchen
while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)
