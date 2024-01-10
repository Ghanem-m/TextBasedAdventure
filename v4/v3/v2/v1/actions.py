# actions.py

class Actions:

    @staticmethod
    def go(game, parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            parameters (list): The list of parameters in the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        player = game.player

        # If there are extra parameters, print an error message and return False.
        if len(parameters) != 1:
            print("La commande 'go' ne prend qu'une direction comme paramètre.")
            return False

        # Get the direction from the parameters.
        direction = parameters[0].upper()

        # Handle aliases for directions
        if direction in ["O", "OUEST"]:
            direction = "O"
        elif direction in ["E", "EST"]:
            direction = "E"
        elif direction in ["S", "SUD"]:
            direction = "S"
        elif direction in ["N", "NORD"]:
            direction = "N"
        elif direction in ["U", "UP"]:
            direction = "U"
        elif direction in ["D", "DOWN"]:
            direction = "D"

        # Validate the direction
        valid_directions = ['N', 'E', 'S', 'O', 'D', 'U', 'OUEST', 'NORD', 'EST', 'SUD', 'back']
        if direction not in [d.upper() for d in valid_directions]:
            print("Direction invalide. Veuillez entrer une direction valide (N, E, S, O, D, U).")
            return False

        # Get the current room and the destination room
        current_room = player.current_room
        destination_room = current_room.get_exit(direction)

        # Check if the destination room is valid
        if destination_room is not None:
            # Move the player to the destination room
            player.move(direction)

            # Update the GUI with the new room description
            game.gui.display_message(player.current_room.get_long_description())
            return True
        else:
            print("Il n'y a pas de sortie dans cette direction.")
            return False

    @staticmethod
    def quit(game, parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            parameters (list): The list of parameters in the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If there are extra parameters, print an error message and return False.
        if len(parameters) != 0:
            print("La commande 'quit' ne prend aucun paramètre.")
            return False

        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, parameters):
        """
        Print the list of available commands.

        Args:
            game (Game): The game object.
            parameters (list): The list of parameters in the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If there are extra parameters, print an error message and return False.
        if len(parameters) != 0:
            print("La commande 'help' ne prend aucun paramètre.")
            return False

        # Print the list of available commands to the GUI
        commands_list = "\nVoici les commandes disponibles:\n"
        for command in game.commands.values():
            commands_list += f"\t- {command}\n"
        game.gui.display_message(commands_list)
        return True

    @staticmethod
    def back(game, parameters):
        player = game.player

        # If there are extra parameters, print an error message and return False.
        if len(parameters) != 0:
            print("La commande 'back' ne prend aucun paramètre.")
            return False

        # If there is no history of previous rooms, print an error message and return False.
        if len(player.history) < 1:
            print("\nIl n'y a pas de pièce précédente à laquelle revenir.\n")
            return False

        # Move the player to the previous room.
        previous_room = player.history.pop()  # Get the last room from the history, which is now the previous room
        player.current_room = previous_room

        # Update the GUI with the new room description
        game.gui.display_message(f"\nVous êtes revenu à la pièce précédente: {previous_room.name}\n")
        return True

    @staticmethod
    def talk(game, parameters):
        # Check if there are messages
        if game.player.current_room.characters:
            messages = []
            for character in game.player.current_room.characters:
                message = character.talk()
                if message is not None:
                    messages.append(message)
            return "\n".join(messages)
        else:
            return "Il n'y a personne avec qui parler ici."

    @staticmethod
    def take(game, parameters):
        player = game.player

        # If there are extra parameters, print an error message and return False.
        if len(parameters) != 1:
            print("La commande 'take' prend exactement 1 paramètre.")
            return False

        # Get the item name from the parameters.
        item_name = parameters[0].lower()

        # Check if the item is in the current room's inventory.
        if item_name in [item.name.lower() for item in player.current_room.inventory]:
            # Move the item from the room's inventory to the player's inventory.
            item = next(item for item in player.current_room.inventory if item.name.lower() == item_name)
            player.inventory.append(item)
            player.current_room.inventory.remove(item)

            # Update the GUI with the message
            game.gui.display_message(f"\nVous avez pris : {item.name}\n")
            return True
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans cette pièce.\n")
            return False

    @staticmethod
    def drop(game, parameters):
        player = game.player

        # If there are extra parameters, print an error message and return False.
        if len(parameters) != 1:
            print("La commande 'drop' prend exactement 1 paramètre.")
            return False

        # Get the item name from the parameters.
        item_name = parameters[0].lower()

        # Check if the item is in the player's inventory.
        if item_name in [item.name.lower() for item in player.inventory]:
            # Move the item from the player's inventory to the current room's inventory.
            item = next(item for item in player.inventory if item.name.lower() == item_name)
            player.current_room.inventory.append(item)
            player.inventory.remove(item)

            # Update the GUI with the message
            game.gui.display_message(f"\nVous avez déposé : {item.name}\n")
            return True
        else:
            print(f"\nL'objet '{item_name}' n'est pas dans votre inventaire.\n")
            return False

    @staticmethod
    def check(game, parameters):
        player = game.player

        # If there are extra parameters, print an error message and return False.
        if len(parameters) != 0:
            print("La commande 'check' ne prend aucun paramètre.")
            return False

        # Print the player's inventory to the GUI.
        if player.inventory:
            inventory_list = "\nVotre inventaire contient les objets suivants:\n"
            for item in player.inventory:
                inventory_list += f"- {item.name}\n"
            game.gui.display_message(inventory_list)
        else:
            game.gui.display_message("\nVotre inventaire est vide.\n")

        return True

    @staticmethod
    def look(game, parameters):
        """
        Print information about the current room.

        Args:
            game (Game): The game object.
            parameters (list): The list of parameters in the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.
        """
        # If there are extra parameters, print an error message and return False.
        if len(parameters) != 0:
            print("La commande 'look' ne prend aucun paramètre.")
            return False

        # Print information about the current room to the GUI
        game.gui.display_message(game.player.current_room.display_inventory())
        return True

