import tkinter as tk
import tkinter as ttk
from tkinter import Text, Entry, Scrollbar,END,Tk,Frame,Button
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character

class GameGUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Text-Based Adventure Game")
        self.geometry("800x600")
        self.setup_gui()
        self.game = game
        self.game.set_game_gui(self)  # Set the GUI instance for the game

    def setup_gui(self):
        self.output_text = Text(self, wrap=tk.WORD, height=20, width=80)
        self.output_text.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.line = tk.Frame(self, height=2, bd=1, relief=tk.SUNKEN)
        self.line.pack(fill=tk.X, pady=5)

        self.input_entry = Entry(self, width=80)
        self.input_entry.pack(side=tk.TOP, fill=tk.X)
        self.input_entry.bind("<Return>", self.process_command)

        # Add a Process Command button
        self.process_button = Button(self, text="Process Command", command=self.process_command)
        self.process_button.pack(side=tk.TOP, pady=(5, 10))

        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.output_text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.output_text.yview)

    def print_welcome(self):
        welcome_message = (
            "Bienvenue dans ce jeu d'aventure !\n"
            "Entrez 'help' si vous avez besoin d'aide.\n"
            "Vous êtes actuellement dans une pièce mystérieuse."
        )
        self.print_to_output(welcome_message)

    def print_to_output(self, message):
        self.output_text.insert(tk.END, message + "\n")
        self.output_text.yview(tk.END)
        self.update()

    def process_command(self, event=None):
        command_string = self.input_entry.get()
        result = self.game.process_command(command_string)
        self.display_message(result)
        self.input_entry.delete(0, tk.END)

    def display_message(self, message):
        if message is not None and not isinstance(message, bool):
            self.output_text.insert(tk.END, str(message) + "\n")
            self.output_text.yview(tk.END)

    def run(self):
        self.mainloop()
class Game:
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.characters = []
        self.gui = None
        self.player = None


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

        aéroport = Room("aéroport","dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(aéroport)
        Beyrouth = Room("Beyrouth", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(Beyrouth)
        Venice = Room("Venice", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(Venice)
        Istanbul = Room("Istanbul",
                        "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(Istanbul)
        NewYork = Room("NewYork", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(NewYork)
        Tokyo = Room("Tokyo",
                     "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Tokyo)
        Barcelone = Room("Barcelone","dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Barcelone)
        Moscou = Room("Moscou","dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Moscou)
        Paris = Room("Paris","dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Paris)
        Caire = Room("Paris","dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Caire)
        statutdeliberte = Room("statutdeliberte",
                               "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(statutdeliberte)
        gondole = Room("gondole",
                       "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(gondole)
        pyramide = Room("pyramide",
                        "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(pyramide)
        Fuji = Room("fuji",
                    "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(Fuji)

        # Créer des PNJ
        npc1 = Character("NPC1", "Un personnage non joueur mystérieux.", aéroport,
                         ["Bonjour, aventurier.", "Je peux vous donner des conseils."])
        self.characters.append(npc1)
        npc2 = Character("NPC2", "Un autre personnage non joueur énigmatique.", Istanbul,
                         ["Bienvenue dans ce monde fantastique.", "Vous êtes courageux de voyager seul."])
        self.characters.append(npc2)
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

        aéroport.exits = {"N": Paris, "E": Beyrouth, "S": Barcelone, "O": NewYork, "U": None, "D": None}
        Paris.exits = {"N": None, "E": Moscou, "S": aéroport, "O": None, "U": None, "D": None}
        Barcelone.exits = {"N": aéroport, "E": Venice, "S": None, "O": None, "U": None, "D": None}
        Venice.exits = {"N": None, "E": None, "S": None, "O": Barcelone, "D": gondole, "U": None}
        Beyrouth.exits = {"N": Istanbul, "E": Tokyo, "S": Caire, "O": aéroport, "U": None, "D": None}
        Istanbul.exits = {"N": Moscou, "E": None, "S": Beyrouth, "O": None, "U": None, "D": None}
        Moscou.exits = {"N": None, "E": None, "S": Istanbul, "O": Paris, "U": None, "D": None}
        NewYork.exits = {"N": None, "E": aéroport, "S": None, "O": Tokyo, "U": statutdeliberte, "D": None}
        Tokyo.exits = {"N": None, "E": NewYork, "S": None, "O": Paris, "U": Fuji, "D": None}
        Caire.exits = {"N": Beyrouth, "E": None, "S": None, "O": None, "U": None, "D": pyramide}
        statutdeliberte.exits = {"U": None, "D": NewYork, "N": None, "E": None, "S": None, "O": None}
        gondole.exits = {"D": None, "U": Venice, "N": None, "E": None, "S": None, "O": None}
        pyramide.exits = {"D": None, "U": Caire, "N": None, "E": None, "S": None, "O": None}
        Fuji.exits = {"N": None, "E": None, "S": None, "O": None, "U": None, "D": Tokyo}

        # Setup player and starting room
        self.player = Player("Player")  # No need to ask for player name in the console
        self.player.current_room = aéroport

    def get_room_by_name(self, room_name):
        for room in self.rooms:
            if room.name == room_name:
                return room
        return None

    def set_game_gui(self, gui):
        self.gui = gui
    def process_command(self, command_string):
        list_of_words = command_string.split()
        command_word = list_of_words[0]

        if command_word not in self.commands:
            return f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n"
        else:
            command = self.commands[command_word]
            return command.action(self, list_of_words[1:])

    def print_welcome(self):
        welcome_message = (
            f"\nBienvenue {self.player.name} dans ce jeu d'aventure !\n"
            "Entrez 'help' si vous avez besoin d'aide.\n"
            f"{self.player.current_room.get_long_description()}"
        )
        self.gui.print_to_output(welcome_message)


def main():
    game = Game()
    gui = GameGUI(game)
    game.set_game_gui(gui)  # Set the GUI instance for the game
    game.setup()
    gui.print_welcome()
    gui.run()


if __name__ == "__main__":
    main()