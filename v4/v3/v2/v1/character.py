import random

class Character:
    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        return f"{self.name} : {self.description}"

    def move(self):
        # Le PNJ a une chance sur deux de se déplacer
        if random.choice([True, False]):
            # Choisissez une pièce adjacente au hasard (vous devez définir cette logique)
            # Assurez-vous de mettre à jour la référence du lieu dans self.current_room
            pass

    def get_msg(self):
        if self.msgs:
            msg = self.msgs.pop(0)  # Utilisez pop(0) pour obtenir et supprimer le premier message
            print(msg)
            self.msgs.append(msg)  # Ajoutez le message à la fin pour la rotation cyclique
        else:
            print("Je n'ai rien à dire.")


    def talk(self):
        # Check if there are messages
        if self.msgs:
            # Return the current message without removing it from the list
            return self.msgs[0]
        else:
            return "Je n'ai rien à dire."