# Define the Room class.
from item import Item
from PIL import Image, ImageTk
import os
class Room:

    # Define the constructor. 
    def __init__(self, name, description,image_path =None):
        self.name = name
        self.description = description
        self.exits = {}
        self.characters = []
        self.inventory =[]
        self.image_path = image_path
    # Define the get_exit method.
    def get_exit(self, direction):
        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None

    def look(self):
        print(f"On voit dans {self.name}:")
        for item in self.items:
            print(f"    - {item}")
        for character in self.characters:
            print(f"    - {character}")

    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.

    def get_long_description(self):
        description = f"\n{self.name}\n{self.description}\n\n{self.get_exit_string()}\n"
        return description

    def display_inventory(self):
        items_string = "\n".join(item.name for item in self.inventory) if self.inventory else "Il n'y a rien ici."
        npcs_string = "\nPersonnages présents : " + ", ".join(npc.name for npc in self.characters) if self.characters else ""
        return f"Items in {self.name}:\n{items_string}\n{npcs_string}" if self.inventory or self.characters else "Il n'y a rien ici."


    def get_image(self):
        if self.image_path:
            image = Image.open(self.image_path)
            return ImageTk.PhotoImage(image)
        return None

