import tkinter as tk
import tkinter as ttk
from tkinter import *
from PIL import Image, ImageTk
import os
import customtkinter
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry, CTkTextbox, CTkTabview, CTkOptionMenu, CTkComboBox, CTkInputDialog, CTkRadioButton, CTkProgressBar, CTkSlider, CTkSegmentedButton, CTkSwitch, CTkScrollableFrame, CTkCheckBox, CTkFont
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from game import Game
from functools import partial


class GameGUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.title("Text-Based Adventure Game")
        self.geometry("800x600")
        self.setup_gui()
        self.game = game
        self.game.set_game_gui(self)



    def move_north(self):
        # Envoyez la commande "go N" au jeu pour aller vers le Nord
        response = self.game.process_command("go N")
        # Affichez la réponse du jeu dans la fenêtre de sortie
        self.display_message(response)

    def move_east(self):
        # Envoyez la commande "go N" au jeu pour aller vers le Nord
        response = self.game.process_command("go E")
        # Affichez la réponse du jeu dans la fenêtre de sortie
        self.display_message(response)

    def move_south(self):
        # Envoyez la commande "go N" au jeu pour aller vers le Nord
        response = self.game.process_command("go S")
        # Affichez la réponse du jeu dans la fenêtre de sortie
        self.display_message(response)

    def move_west(self):
        # Envoyez la commande "go N" au jeu pour aller vers le Nord
        response = self.game.process_command("go O")
        # Affichez la réponse du jeu dans la fenêtre de sortie
        self.display_message(response)

    def move_up(self):
        # Envoyez la commande "go N" au jeu pour aller vers le Nord
        response = self.game.process_command("go U")
        # Affichez la réponse du jeu dans la fenêtre de sortie
        self.display_message(response)
    def goback(self):
        # Envoyez la commande "go N" au jeu pour aller vers le Nord
        response = self.game.process_command("back")
        # Affichez la réponse du jeu dans la fenêtre de sortie
        self.display_message(response)

    def move_down(self):
        # Envoyez la commande "go N" au jeu pour aller vers le Nord
        response = self.game.process_command("go D")
        # Affichez la réponse du jeu dans la fenêtre de sortie
        self.display_message(response)

    def look_command(self):
        response = self.game.process_command("look")
        self.display_message(response)

    def check_command(self):
        response = self.game.process_command("check")
        self.display_message(response)

    def collect_fragment(self, fragment):
        self.player.fragments_collected.append(fragment)

    def has_all_fragments_in_order(self):
        expected_fragments = ["Fragment1", "Fragment2", "Frqgment3", "Fragment4", "Fragment5", "Frqgment6"]
        return self.player.fragments_collected == expected_fragments


    def setup_gui(self):
        self.output_text = CTkTextbox(self, wrap="word", height=50, width=80)
        self.output_text.pack(side="top", fill="both", expand=True)

        self.line = CTkFrame(self, height=2)
        self.line.pack(fill="x", pady=5)

        self.input_entry = CTkEntry(self, width=80)
        self.input_entry.pack(side="top", fill="x")
        self.input_entry.bind("<Return>", self.process_command)

        self.process_button = CTkButton(self, text="Process Command", command=self.process_command)
        self.process_button.pack(side="top", pady=(5, 10))

        self.scrollbar = customtkinter.CTkScrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.output_text.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.output_text.yview)

        button_north = Button(self, text="Nord", command=self.move_north, width=10, height=2)
        button_east = Button(self, text="Est", command=self.move_east, width=10, height=2)
        button_south = Button(self, text="Sud", command=self.move_south, width=10, height=2)
        button_west = Button(self, text="Ouest", command=self.move_west, width=10, height=2)
        button_back = Button(self, text="Back", command=self.goback, width=10, height=2)


        # Ajoutez des boutons pour les directions verticales
        button_up = Button(self, text="Haut", command=self.move_up, width=10, height=2)
        button_down = Button(self, text="Bas", command=self.move_down, width=10, height=2)
        # Create buttons for "look" and "check" commands
        button_look = Button(self, text="Look", command=self.look_command)
        button_check = Button(self, text="Check", command=self.check_command)

        # Pack the "look" and "check" buttons
        button_look.pack(side=tk.LEFT)
        button_check.pack(side=tk.LEFT)

        # Placez les boutons à l'emplacement souhaité
        button_north.pack(side=tk.RIGHT)
        button_east.pack(side=tk.RIGHT)
        button_south.pack(side=tk.RIGHT, anchor="center")
        button_west.pack(side=tk.RIGHT, anchor="w")
        button_up.pack(side=tk.RIGHT)
        button_down.pack(side=tk.RIGHT)
        button_back.pack(side=tk.RIGHT)

    def print_welcome(self):
        self.display_current_room_image()
        airport_description = self.game.player.current_room.get_long_description()
        welcome_message = f"Bienvenue dans ce jeu d'aventure ! {airport_description}\n"

        welcome_message += "Entrez 'help' si vous avez besoin d'aide."
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

    def display_history(self):
        history_message = self.get_history()
        self.game_gui.print_to_output(history_message)

    def run(self):
        self.mainloop()

    def display_current_room_image(self):
        current_room = self.game.player.current_room
        image = current_room.get_image()

def main():
    game = Game()
    gui = GameGUI(game)
    game.set_game_gui(gui)  # Set the GUI instance for the game
    game.setup()
    game.print_welcome()
    gui.run()

if __name__ == "__main__":
    main()