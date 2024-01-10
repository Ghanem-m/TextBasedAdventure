# Description: Game class

# Import modules

import tkinter as tk
from tkinter import Scrollbar, Text, Entry, Button, END
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.character =[]

    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, D, U)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : revenir à la pièce précédente", Actions.back, 0)
        self.commands["back"] = back
        talk = Command("talk", " <character_name>: parler avec un personnage non joueur", Actions.talk, 1)
        self.commands["talk"] = talk
        take = Command("take", " <item>: prendre un objet de la pièce", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " <item>: déposer un objet de votre inventaire", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : vérifier votre inventaire", Actions.check, 0)
        self.commands["check"] = check
        look= Command("look", " : observer la pièce actuelle", Actions.look, 0)
        self.commands["look"] = look
        # Setup rooms

        aéroport = Room("aéroport", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(aéroport)
        Beyrouth = Room("Beyrouth", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(Beyrouth)
        Venice = Room("Venice", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(Venice)
        Istanbul = Room("Istanbul", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(Istanbul)
        NewYork = Room("NewYork", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(NewYork)
        Tokyo = Room("Tokyo", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Tokyo)
        Barcelone = Room("Barcelone", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Barcelone)
        Moscou = Room("Moscou", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Moscou)
        Paris = Room("Paris", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Paris)
        Caire = Room("Paris", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Caire)
        statutdeliberte = Room("statutdeliberte", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(statutdeliberte) 
        gondole = Room("gondole", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(gondole) 
        pyramide = Room("pyramide", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(pyramide) 
        Fuji = Room("fuji", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Fuji)





        # Créer des PNJ
        npc1 = Character("NPC1", "Un personnage non joueur mystérieux.",aéroport,["Bonjour, aventurier.","Je peux vous donner des conseils."])
        self.character.append(npc1)
        npc2 = Character("NPC2", "Un autre personnage non joueur énigmatique.", Istanbul,["Bienvenue dans ce monde fantastique.", "Vous êtes courageux de voyager seul."])
        self.character.append(npc2)
        # Ajouter des PNJ à certaines pièces
        aéroport.characters.append(npc1)
        Istanbul.characters.append(npc2)


        # Initialize items
        sword = Item("sword", "A sharp sword.")
        key = Item("key", "A small key.")
        potion = Item("potion", "A healing potion.")

        # Add items to specific rooms
        aéroport.inventory.append(sword)
        Beyrouth.inventory.append(key)
        Venice.inventory.append(potion)

        # Create exits for rooms

        aéroport.exits = {"N" : Paris, "E" : Beyrouth, "S" : Barcelone, "O" : NewYork, "U":None, "D" :None}
        Paris.exits = {"N" : None, "E" : Moscou, "S" : aéroport, "O" : None, "U":None, "D" :None}
        Barcelone.exits = {"N" : aéroport, "E" : Venice, "S" : None, "O" : None,"U":None, "D" :None}
        Venice.exits = {"N" : None, "E" : None, "S" : None, "O" : Barcelone, "D": gondole, "U":None}
        Beyrouth.exits = {"N" : Istanbul, "E" : Tokyo, "S" : Caire, "O" : aéroport, "U":None, "D" :None}
        Istanbul.exits = {"N" : Moscou, "E" : None, "S" : Beyrouth, "O" : None, "U":None, "D" :None}
        Moscou.exits = {"N" : None, "E" : None, "S" : Istanbul, "O" : Paris,"U":None, "D" :None}
        NewYork.exits = {"N" : None, "E" : aéroport, "S" : None, "O" : Tokyo, "U": statutdeliberte, "D": None}
        Tokyo.exits = {"N" : None, "E" : NewYork, "S" : None, "O" : Paris, "U":Fuji, "D" :None}
        Caire.exits = {"N" : Beyrouth, "E" : None, "S" : None,"O":None, "U":None, "D" :pyramide}
        statutdeliberte.exits= {"U": None, "D": NewYork, "N" : None, "E" : None, "S" : None, "O" : None}
        gondole.exits={"D": None, "U": Venice, "N" : None, "E" : None, "S" : None, "O" : None}
        pyramide.exits={"D": None, "U":Caire, "N" : None, "E" : None, "S" : None, "O" : None}
        Fuji.exits={"N" : None, "E" : None, "S" : None, "O" : None, "U" : None,"D":Tokyo}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = aéroport

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None


    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    def player_talk(self, list_of_words) -> None:
        # Vérifiez si le joueur a spécifié un PNJ
        if len(list_of_words) > 1:
            character_name = list_of_words[1]
            # Recherchez le PNJ dans la pièce actuelle
            character = self.find_character_in_room(character_name)
            if character:
                character.talk()
            else:
                print(f"\nLe personnage '{character_name}' n'est pas présent dans cette pièce.\n")
        else:
            print("\nVeuillez spécifier le nom du personnage avec lequel vous souhaitez parler.\n")

    # Fonction pour rechercher un PNJ dans la pièce actuelle
    def find_character_in_room(self, character_name):
        current_room = self.player.current_room
        for character in current_room.pnjs:
            if character.name.lower() == character_name.lower():
                return character
        return None

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
