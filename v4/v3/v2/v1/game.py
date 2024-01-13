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
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.characters = []
        self.gui = None
        self.player =None
        self.game_over = False  # Add a game_over flag




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
        open_command = Command("open", " <item>: ouvrir un objet", Actions.open, 1)
        self.commands["open"]=open_command
        # Setup rooms

        aeroport = Room("aéroport","à l'aéroport : un carrefour mondial, où des histoires commencent et se terminent.\n"
                        "                      ___\n"
                        "                      \\\\ \\\n"
                        "                       \\\\ `\\\n"
                        "    ___                 \\\\  \\\n"
                        "   |    \\                \\\\  `\\\n"
                        "   |_____\\                \\    \\\n"
                        "   |______\\                \\    `\\\n"
                        "   |       \\                \\     \\\n"
                        "   |      __\\__---------------------------------._.\n"
                        " __|---~~~__o_o_o_o_o_o_o_o_o_o__[][\__   \n"
                        "|___                         /~      )                \\__\n"
                        "    ~~~---..._______________/      ,/_______/\n"
                        "                           /      /\n"
                        "                          /     ,/\n"
                        "                         /     ,/\n"
                        "                        /    ,/\n"
                        "                       /    /\n"
                        "                      //  ,/\n"
                        "                     //  /\n"
                        "                    // ,/\n"
                        "                   //_/\n")

        self.rooms.append(aeroport)
        beyrouth = Room("Beyrouth", "à Beyrouth dans un restaurant animé: lieu festif, mélange de saveurs, de musique et de rires. ")
        self.rooms.append(beyrouth)
        venice = Room("Venice",
                      "à Venise sur le pont du Rialto: arc architectural élégant sur le Grand Canal, témoin de la splendeur vénitienne. \n"
                      "                                                      ~.   \n"
                      "                       Ya...|_..aab     .   .         \n"
                      "                          Y88a  Y88o  Y88a   (     )        \n"
                      "                          Y88b  Y88b  Y88b   `.oo'\n"
                      "                          :888  :888  :888  ( (`-'\n"
                      "                  .---.    d88P  d88P  d88P   ..\n"
                      "               / .-._)  d8P----|----Y8P      ..   \n"
                      "               ( (`._) .-.  .-. |.-.  .-.  .-.   ) )   \n"
                      "               \ `---( O )( O )( O )( O )( O )-' /    \n"
                      "                   `.    `-'  `-'  `-'  `-'  `-'  .'    \n"
                      "               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~)\n")
        self.rooms.append(venice)
        istanbul = Room("Istanbul",
                        "à Istambul dans un souk: labyrinthe coloré, vibrant de la vie d'Istanbul, où chaque coin raconte une histoire marchande. \n"
                        "                                       @\_/@                        \n"
                        "                                     @|XXXXXXXX |                    \n"
                        "                                    @ |X||    X |                    \n"
                        "                                   @  |X||    X |                              \n"
                        "                                  @   |XXXXXXXX |\n"
                        "                                 @    |X||    X |             \n"
                        "                                @     |X||   .X |\n"
                        "                               @      |X||.  .X |                      \n"
                        "                              @      |%XXXXXXXX%||\n"
                        "                            @        |X||  . . X||\n"
                        "                                     |X||   .. X||                               @     @\n"
                        "                                     |X||  .   X||.                              ||====%\n"
                        "                                     |X|| .    X|| .                             ||    %\n"
                        "                                     |X||.     X||   .                           ||====%\n"
                        "                                    |XXXXXXXXXXXX||     .                        ||    %\n"
                        "                                    |XXXXXXXXXXXX||         .                 .  ||====% .\n"
                        "                                    |XX|        X||                .        .    ||    %  .\n"
                        "                                    |XX|        X||                   .          ||====%   .\n"
                        "                                    |XX|        X||              .          .    ||    %     .\n"
                        "                                    |XX|======= X||============================+ || .. %  ........\n"
                        "                                ===== /            X||                              ||    %\n"
                        "                                                X||           /)                 ||    %\n"
                        "                                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~)\n")
        self.rooms.append(istanbul)
        newyork = Room("NewYork",
                       "à New York dans Times Square: nœud animé de lumières, de mouvements et d'activités au cœur de la Grosse Pomme.\n"
                       "                                               \n "
                       "                         (_)                     \n "
                       "                         ###       .             \n "
                       "                        (#c    _\|/_           \n "
                       "                         #\     wWWWw            \n "
                       "                         \ \-. (/. .\)           \n "
                       "                         /\ /`\/\   /\           \n "
                       "                         |\/   \) (|            \n "
                       "                         `\.' ; ; ' ;\           \n "
                       "                         `\;  ;    .  ;/\          \n "
                       "                             `\;    ;  ;|  \       \n "
                       "                            ;   .'  ' ;  /         \n "
                       "                            |_.'   ;  | /)        \n "
                       "                             (     ''._;/`        \n "
                       "                            |    ' . ;            \n "
                       "                            |.-'   .:)            \n "
                       "                            |        |            \n "
                       "                            (  .'  : |            \n "
                       "                            |,-  .:: |           \n "
                       "                            | ,-'  .;|            \n "
                       "                           /,.:\_         \n "
                       "                           [I_I_I_I_I_I_]      \n "
                       "                           | __________ |    \n "
                       "                           | || |  | || |     \n "
                       "                          | |||||| |      \n "
                       "                         /=--------------=\    \n "
                       "                        /                  \    \n "
                       "                       |             \n ")
        self.rooms.append(newyork)
        tokyo = Room("Tokyo", "à Tokyo dans un temple: un sanctuaire silencieux, gardien de traditions millénaires, où les samouraïs illustrent l'harmonie entre le passé et le présent.")
        self.rooms.append(tokyo)
        barcelone = Room("Barcelone", "à Barcelone dans un bar à tapas: ambiance vibrante, épicentre des saveurs espagnoles, où les tapas se partagent joyeusement.")
        self.rooms.append(barcelone)
        moscou = Room("moscou", "à Moscou sur la place Rouge: centre historique entouré d'architecture imposante et de traditions russes.")
        self.rooms.append(moscou)
        paris = Room("Paris","à Paris dans une boulangerie d'un grand pâtissier: doux refuge de délices parisiens, où les senteurs du pain fraîchement cuit enrobent l'air. \n"
            "           ^\n"
            "           |\n"
            "           +\n"
            "           |\n"
            "           |\n"
            "           |\n"
            "           |\n"
            "           |\n"
            "          A\n"
            "         ===                               ________\n"
            "        /EEE\\                             |______|\n"
            "       //EEE\\\\                           |*(  )*|         \n"
            "___//_____\\\\_____________|O|  |O|_______\n")

        self.rooms.append(paris)

        caire = Room("Caire", "au Caire dans le désert : étendue infinie de sable, berceau des pyramides, enveloppée dans un silence ancien. \n"
                              "                 /=\\ \n"
                              "                /===\ \    \n"
                              "               /=====\' \    \n"
                              "              /=======\'' \  \n"
                              "             /=========\ ' '\   \n"
                              "            /===========\''   \     \n"
                              "           /=============\ ' '  \    \n"
                              "          /===============\   ''  \   \n"
                              "         /=================\' ' ' ' \     \n"
                              "        /===================\' ' '  ' \    \n"
                              "       /=====================\' '   ' ' \   \n"
                              "      /=======================\  '   ' /   \n"
                              "     /=========================\   ' /  \n"
                              "    /===========================\'  /    \n"
                              "   /=============================\/        \n")
        self.rooms.append(caire)
        statutdeliberte = Room("Statue de la liberté", "sur la statue de la Liberté: majestueuse sentinelle de la liberté, levant fièrement sa torche au cœur de New York.")
        self.rooms.append(statutdeliberte)
        gondole = Room("gondole", "dans une gondole: embarcation élégante sillonnant les canaux de Venise, portant avec elle l'esprit romantique de la ville.")
        self.rooms.append(gondole)
        pyramide = Room("pyramide", "dans une pyramide: un labyrinthe mystique d'antichambres secrètes et de passages cachés, où les échos du passé résonnent et les hiéroglyphes racontent des légendes oubliées.")
        self.rooms.append(pyramide)
        fuji = Room("Mont Fuji", "au Mont Fuji: pic majestueux dominant le paysage japonais, source d'inspiration artistique et spirituelle depuis des siècles.")
        self.rooms.append(fuji)
        # Setup characters qui donnent indices
        le_chat_bleu = Character("Le Chat Bleu", "un chat mystérieux", aeroport, ["Bienvenue à toi jeune voyageur! Tu a été choisi pour une quête extraordinaire. Tu devras récupérer six fragments à travers le monde pour forger une clef. Chaque fragment que tu découvriras te rapprochera du trésor final, un mystérieux coffre scellé. Cependant, le chemin vers le coffre reste caché, c’est à toi seul de le trouver. A chaque endroit où se trouve un fragment, une personne du pays te donnera un indice qui t’amènera au fragment suivant. Voici ton premier indice : ton périple commence là où la flamme de la liberté danse face au vent. Trouve l'île où les rêves s'envolent vers le ciel pour découvrir le premier fragment. Bonne chance, aventurier ! Que l'aventure commence!"])

        Will = Character("Will", "l’américain", newyork, ["Hello ! Cherche le lieu où l'aube caresse des sommets majestueux, comme si elle éveillait des vagues de montagnes. Là-bas, dans cette terre où les sakuras fleurissent, tu découvriras le fragment suivant, caché sous l'ombre d’une majesté silencieuse."])
        Xiao = Character("Xiao", "le japonais", tokyo, ["Konnichiwa! Pour poursuivre ta quête, envole-toi vers la ville où l'amour flotte dans l'air, et les lumières de la tour brillent de mille feux. C'est là que le prochain fragment t'attend. "])
        Léa = Character("Léa", "la française", paris, ["Bonjour! Cherche le lieu où l'Orient rencontre l'Occident. Trouve la porte vers l'Est méditerranéen où les saveurs exotiques dansent avec les parfums de l'histoire ancienne et tu découvriras le chemin vers le prochain fragment."])
        Elias = Character("Elias", "le libanais", beyrouth, [" Ahlan wa sahlan ! Pour approcher le prochain fragment, suis la trace des civilisations anciennes. Cherche le lieu où les mystères du passé te guideront vers une terre ensoleillée où des constructions millénaires se dressent comme des énigmes à dévoiler. Là-bas, au cœur de l'antiquité, ton voyage continuera dans les profondeurs des secrets bien gardés."])
        Cleo = Character("Cleo", "l’égyptienne", caire, ["Marhaban ! Au cœur de ce désert rempli d’histoire, ta quête touche à sa fin. Cherche le lieu où les ombres du passé convergent vers une terre hispanique de passion et de fête, où les œuvres humaines rivalisent avec la grandeur des étoiles. Ton ultime fragment t'attend dans une cité célèbre pour son architecture extraordinaire et son ambiance vibrante. "])
        Camille=Character("Camille","l'exploratrice intrépide",fuji,["Salutations ! Si vous cherchez le prochain indice, aventurez-vous là où les brises légères caressent les cerisiers en fleurs. Dans cette terre où les sakuras s'épanouissent, vous découvrirez le fragment caché sous l'ombre d'une majesté silencieuse."])
        # Setup characters qui bougent dans la map
        Maria = Character("Maria", "l’espagnole", barcelone, ["Hola ! Soy Maria, une Barcelonaise passionnée de cuisine. Mes journées sont rythmées par le parfum des tapas, les couleurs du marché de La Boqueria et les doux sons du flamenco. J'adore me promener le long de la plage et savourer une bonne paella. Si tu veux des conseils pour dénicher les meilleures saveurs de Barcelone, n'hésite pas !"])
        Mario = Character("Mario", "l’italien", venice, ["Ciao! Sono Mario, un Vénitien naviguant à travers les canaux de cette ville magnifique. Mes journées sont remplies de gondoles, de masques vénitiens et d'une bonne dose de café italien. J'adore partager les histoires de cette ville unique et secrète. Si tu veux savoir où trouver les meilleurs cicchetti ou simplement discuter, sono qui!"])
        Volodimir = Character("Volodimir", "le russe", moscou, ["Privet ! Je suis Volodimir, un amoureux de l'histoire de ma ville. Mes journées se déroulent au son des cloches des églises et parmi les pages de livres anciens. Né à Moscou, j'aime me promener dans les vastes parcs et profiter de l'architecture impressionnante. Si tu veux en savoir plus sur la vie à Moscou, n'hésite pas à me demander!"])
        Ozan = Character("Ozan", "le turc", istanbul, ["Merhaba! Je suis Ozan, un passionné de musique et d'aventure. Mes journées sont une symphonie entre les ruelles animées du Grand Bazar, les rives du Bosphore et les sons envoûtants du saz. Né à Istanbul, je trouve toujours de nouvelles mélodies dans cette ville fascinante. Si tu veux partager des histoires ou simplement discuter, je suis là pour toi!"])

        aeroport.characters.append(le_chat_bleu)
        istanbul.characters.append(Ozan)
        fuji.characters.append(Camille)
        moscou.characters.append(Volodimir)
        barcelone.characters.append(Maria)
        beyrouth.characters.append(Elias)
        newyork.characters.append(Will)
        caire.characters.append(Cleo)
        tokyo.characters.append(Xiao)
        paris.characters.append(Léa)
        venice.characters.append(Mario)
        # Setup Items

        # New York
        fragment1 = Item("Fragment1", "Morceau mystérieux")
        flambeau = Item("Flambeau","Torche emblématique de la Statue de la Liberté, symbole de lumière, liberté, et exploration ")
        # Mont Fuji
        fragment2 = Item("Fragment2", "Morceau mystérieux")
        fleur_de_sakura = Item("Fleur de Sakura","Une délicate fleur de cerisier, symbole de beauté éphémère et de renouveau. ")
        # Paris
        fragment3 = Item("Fragment3", "Morceau mystérieux")
        baguette = Item("Baguette","Pain emblématique de Paris, croustillant à souhait, transportant les aventuriers au cœur des rues parisiennes. ")
        croissant = Item("Croissant", "Un délicieux croissant, emblème de la pâtisserie française ")
        macaron = Item("Macaron", "Un macaron coloré, doux et délicieux, originaire de la pâtisserie française.")
        # Beyrouth
        fragment4 = Item("Fragment4", "Morceau mystérieux")
        darbouka = Item("Darbouka", "Un tambourin oriental, invitant à des rythmes envoûtants.")
        baklava = Item("Baklava", "Un délice sucré, composé de couches de pâte filo et de noix, imprégné de miel.")
        # LeCaire
        scorpion = Item("Scorpion", "Un petit scorpion, rappelant le désert et ses créatures mystérieuses.")
        serpent = Item("Serpent", "Un serpent, symbole de sagesse et de mystère.")
        # Pyramide
        fragment5 = Item("Fragment5", "Morceau mystérieux")
        momie = Item("Momie", "Une momie ancienne, gardienne de secrets enfouis depuis des siècles. ")
        amulette = Item("Amulette", "Un talisman mystique, porteur de bonnes énergies et de protections. ")
        # Barcelone
        fragment6 = Item("Fragment6", "Morceau mystérieux")
        paella = Item("Paella", "Un plat espagnol traditionnel, riche en saveurs et en couleurs.")
        churros_con_chocolate = Item("Churros con chocolate","Délicieux beignets espagnols accompagnés d'une riche sauce au chocolat. ")
        tapas = Item("Tapas", "Une variété de petites bouchées espagnoles, offrant une explosion de saveurs.")
        # Venise

        chapeau = Item("Chapeau", "Un chapeau élégant, reflétant le style et la personnalité de son porteur.")
        # Gondole
        coffre = Item("Coffre", "Un coffre mystérieux, renfermant des secrets et des richesses inconnues.")
        pagaie = Item("Pagaie", "Une pagaie, prête à être utilisée pour naviguer sur des eaux inexplorées. ")
        # Moscou
        chapka = Item("Chapka", "Un chapeau russe traditionnel, conçu pour affronter les hivers rigoureux.")
        # Istanbul
        loukoum = Item("Loukoum", "Des délices turcs, doux et parfumés, éveillant les papilles.")
        vase_ancien = Item("Vase ancien", "Un vase orné d'artefacts anciens, racontant des histoires du passé. ")
        bijoux = Item("Bijoux", "Des parures étincelantes, témoins de l'élégance et de la richesse.")
        assiettes = Item("Assiettes", "Des assiettes décoratives, portant des motifs artistiques et culturels. ")
        #Tokyo
        sakura_bonsai = Item("Bonsaï de Sakura","Un magnifique bonsaï de sakura en fleurs, capturant l'essence de la saison des cerisiers en fleurs.")
        tech_gadget = Item("Gadget Technologique","Un gadget high-tech dernier cri, symbole de l'innovation constante de Tokyo.")

        # Add items to specific rooms
        gondole.inventory.append(coffre)
        gondole.inventory.append(pagaie)
        beyrouth.inventory.append(fragment4)
        beyrouth.inventory.append(darbouka)
        beyrouth.inventory.append(baklava)
        venice.inventory.append(chapeau)
        istanbul.inventory.append(loukoum)
        istanbul.inventory.append(bijoux)
        istanbul.inventory.append(assiettes)
        istanbul.inventory.append(vase_ancien)
        caire.inventory.append(scorpion)
        caire.inventory.append(serpent)
        pyramide.inventory.append(momie)
        pyramide.inventory.append(amulette)
        tokyo.inventory.append(sakura_bonsai)
        tokyo.inventory.append(tech_gadget)
        paris.inventory.append(baguette)
        paris.inventory.append(croissant)
        paris.inventory.append(macaron)
        paris.inventory.append(fragment3)
        newyork.inventory.append(fragment1)
        newyork.inventory.append(flambeau)
        barcelone.inventory.append(paella)
        barcelone.inventory.append(churros_con_chocolate)
        barcelone.inventory.append(tapas)
        barcelone.inventory.append(fragment6)
        moscou.inventory.append(chapka)
        fuji.inventory.append(fragment2)
        fuji.inventory.append(fleur_de_sakura)
        pyramide.inventory.append(fragment5)
        # Create exits for rooms

        aeroport.exits = {"N": paris, "E": beyrouth, "S": barcelone, "O": newyork, "U": None, "D": None}
        paris.exits = {"N": None, "E": moscou, "S": aeroport, "O": None, "U": None, "D": None}
        barcelone.exits = {"N": aeroport, "E": venice, "S": None, "O": None, "U": None, "D": None}
        venice.exits = {"N": None, "E": None, "S": None, "O": barcelone, "D": gondole, "U": None}
        beyrouth.exits = {"N": istanbul, "E": tokyo, "S": caire, "O": aeroport, "U": None, "D": None}
        istanbul.exits = {"N": moscou, "E": None, "S": beyrouth, "O": None, "U": None, "D": None}
        moscou.exits = {"N": None, "E": None, "S": istanbul, "O": paris, "U": None, "D": None}
        newyork.exits = {"N": None, "E": aeroport, "S": None, "O": tokyo, "U": statutdeliberte, "D": None}
        tokyo.exits = {"N": None, "E": newyork, "S": None, "O": paris, "U": fuji, "D": None}
        caire.exits = {"N": beyrouth, "E": None, "S": None, "O": None, "U": None, "D": pyramide}
        statutdeliberte.exits = {"U": None, "D": newyork, "N": None, "E": None, "S": None, "O": None}
        gondole.exits = {"D": None, "U": venice, "N": None, "E": None, "S": None, "O": None}
        pyramide.exits = {"D": None, "U": caire, "N": None, "E": None, "S": None, "O": None}
        fuji.exits = {"N": None, "E": None, "S": None, "O": None, "U": None, "D": tokyo}

        # Setup player and starting room
        self.player = Player("Player")  # No need to ask for player name in the console
        self.player.current_room = aeroport

    def set_player_name(self, name):
        self.player.name = name
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
            response = command.action(self, list_of_words[1:])
            if self.game_over:
                response += "\nLe jeu est terminé. Vous avez échoué à ouvrir le coffre."
            return response

    def print_welcome(self):
        airport_description = self.player.current_room.get_long_description()
        welcome_message = f"Bienvenue dans ce jeu d'aventure ! {airport_description}\n"

        welcome_message += "Entrez 'help' si vous avez besoin d'aide."
        self.gui.print_to_output(welcome_message)
