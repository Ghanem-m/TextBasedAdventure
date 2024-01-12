# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name, starting_room=None):
        self.name = name
        self.current_room = starting_room
        self.starting_room = starting_room
        self.history = []
        self.inventory =[]
        self.fragments_collected=[]



    def move(self, direction):
           # Vérifiez si la direction est valide
        if direction not in self.current_room.exits or self.current_room.exits[direction] is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Sauvegardez la pièce actuelle avant de se déplacer
        previous_room = self.current_room

        # Déplacez le joueur vers la nouvelle pièce
        self.current_room = self.current_room.exits[direction]
        print(self.current_room.get_long_description())

        # Ajoutez la pièce précédente à l'historique après le déplacement
        if previous_room != self.starting_room:
            self.history.append(previous_room)

        # Affichez l'historique
        return self.get_history()

    def open(game, parameters):
        player = game.player

        # Check if the player has fragments in their inventory
        expected_fragments = ["Fragment1", "Fragment2", "Fragment3", "Fragment4", "Fragment5", "Fragment6"]

        collected_fragments = [item.name for item in player.inventory]

        if all(fragment in collected_fragments for fragment in expected_fragments):
            player.current_room.chest_unlocked = True
            # Unlock the chest and provide rewards
            return "Vous avez ouvert le coffre et trouvé une récompense !"
        else:
            return "Le coffre est verrouillé. Vous avez besoin des fragments en ordre pour l'ouvrir."
        
    
    def get_history(self):
        # Créez une chaîne de caractères représentant l'historique
        history_str = "Vous avez déjà visité les pièces suivantes:\n"
        history_str += "\n".join("- " + room.name for room in self.history if room is not None)
        return history_str
    
    def back(self):
        if len(self.history) > 0:  # Vérifie s'il y a une pièce précédente dans l'historique
            self.current_room = self.history.pop()
        # Since we're going back, the current room should be added to the history again
        # This allows the user to go forward to the room they just came from
            print("\nVous êtes revenu à la pièce précédente: {self.current_room.name}\n")
            return True
        else:
            print("Vous êtes déjà à la position de départ, impossible de revenir en arrière.")
            return False

    def take(self, item_name):
        """
        Take an item from the current room and add it to the player's inventory.

        Args:
            item_name (str): The name of the item to take.

        Returns:
            bool: True if the item was successfully taken, False otherwise.
        """
        # Check if the item exists in the current room.
        if item_name in [item.name.lower() for item in self.current_room.inventory]:
            # Find the item in the room
            item = next(item for item in self.current_room.inventory if item.name.lower() == item_name)
            # Add the item to the player's inventory
            self.inventory.append(item)
            # Remove the item from the room's inventory
            self.current_room.inventory.remove(item)
            return True
        else:
            return False

    def drop(self, item_name):
        """
        Drop an item from the player's inventory into the current room.

        Args:
            item_name (str): The name of the item to drop.

        Returns:
            bool: True if the item was successfully dropped, False otherwise.
        """
        # Check if the item exists in the player's inventory.
        if item_name in [item.name.lower() for item in self.inventory]:
            # Find the item in the inventory
            item = next(item for item in self.inventory if item.name.lower() == item_name)
            # Add the item to the room's inventory
            self.current_room.inventory.append(item)
            # Remove the item from the player's inventory
            self.inventory.remove(item)
            return True
        else:
            return False

    def check_inventory(self):
        if self.inventory:
            print("\nVotre inventaire contient les objets suivants:")
            for item in self.inventory:
                print(f"    - {item}")
        else:
            print("\nVotre inventaire est vide.\n")