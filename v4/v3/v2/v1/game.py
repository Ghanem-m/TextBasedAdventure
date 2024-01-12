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
        self.player = None
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

        aéroport = Room("aéroport", "à l'aéroport : un carrefour mondial, où des histoires commencent et se terminent.")
        self.rooms.append(aéroport)
        Beyrouth = Room("Beyrouth", "à Beyrouth dans un restaurant animé: lieu festif, mélange de saveurs, de musique et de rires. ")
        self.rooms.append(Beyrouth)
        Venice = Room("Venice", "à Venise sur le pont du Rialto: arc architectural élégant sur le Grand Canal, témoin de la splendeur vénitienne. ")
        self.rooms.append(Venice)
        Istanbul = Room("Istanbul", "à Istambul dans un souk: labyrinthe coloré, vibrant de la vie d'Istanbul, où chaque coin raconte une histoire marchande. ")
        self.rooms.append(Istanbul)
        NewYork = Room("NewYork", "à New York dans Times Square: nœud animé de lumières, de mouvements et d'activités au cœur de la Grosse Pomme.")
        self.rooms.append(NewYork)
        Tokyo = Room("Tokyo", "à Tokyo dans un temple: un sanctuaire silencieux, gardien de traditions millénaires, où les samouraïs illustrent l'harmonie entre le passé et le présent.")
        self.rooms.append(Tokyo)
        Barcelone = Room("Barcelone", "à Barcelone dans un bar à tapas: ambiance vibrante, épicentre des saveurs espagnoles, où les tapas se partagent joyeusement.")
        self.rooms.append(Barcelone)
        Moscou = Room("Moscou", "à Moscou sur la place Rouge: centre historique entouré d'architecture imposante et de traditions russes.")
        self.rooms.append(Moscou)
        Paris = Room("Paris", "à Paris dans une boulangerie d'un grand pâtissier: doux refuge de délices parisiens, où les senteurs du pain fraîchement cuit enrobent l'air.")
        self.rooms.append(Paris)
        Caire = Room("Caire", "au Caire dans le désert : étendue infinie de sable, berceau des pyramides, enveloppée dans un silence ancien. ")
        self.rooms.append(Caire)
        statutdeliberte = Room("Statue de la liberté", "sur la statue de la Liberté: majestueuse sentinelle de la liberté, levant fièrement sa torche au cœur de New York. ")
        self.rooms.append(statutdeliberte)
        gondole = Room("gondole", "dans une gondole: embarcation élégante sillonnant les canaux de Venise, portant avec elle l'esprit romantique de la ville.")
        self.rooms.append(gondole)
        pyramide = Room("pyramide", "dans une pyramide: un labyrinthe mystique d'antichambres secrètes et de passages cachés, où les échos du passé résonnent et les hiéroglyphes racontent des légendes oubliées.")
        self.rooms.append(pyramide)
        Fuji = Room("Mont Fuji", "au Mont Fuji: pic majestueux dominant le paysage japonais, source d'inspiration artistique et spirituelle depuis des siècles.")
        self.rooms.append(Fuji)
        # Setup characters qui donnent indices
        le_chat_bleu = Character("Le Chat Bleu", "un chat mystérieux", aéroport, ["Bienvenue à toi jeune voyageur! Tu a été choisi pour une quête extraordinaire. Tu devras récupérer six fragments à travers le monde pour forger une clef. Chaque fragment que tu découvriras te rapprochera du trésor final, un mystérieux coffre scellé. Cependant, le chemin vers le coffre reste caché, c’est à toi seul de le trouver. A chaque endroit où se trouve un fragment, une personne du pays te donnera un indice qui t’amènera au fragment suivant. Voici ton premier indice : ton périple commence là où la flamme de la liberté danse face au vent. Trouve l'île où les rêves s'envolent vers le ciel pour découvrir le premier fragment. Bonne chance, aventurier ! Que l'aventure commence!"])

        Will = Character("Will", "l’américain", NewYork, ["Hello ! Cherche le lieu où l'aube caresse des sommets majestueux, comme si elle éveillait des vagues de montagnes. Là-bas, dans cette terre où les sakuras fleurissent, tu découvriras le fragment suivant, caché sous l'ombre d’une majesté silencieuse."])
        Xiao = Character("Xiao", "le japonais", Tokyo, ["Konnichiwa! Pour poursuivre ta quête, envole-toi vers la ville où l'amour flotte dans l'air, et les lumières de la tour brillent de mille feux. C'est là que le prochain fragment t'attend. "])
        Léa = Character("Léa", "la française", Paris, ["Bonjour! Cherche le lieu où l'Orient rencontre l'Occident. Trouve la porte vers l'Est méditerranéen où les saveurs exotiques dansent avec les parfums de l'histoire ancienne et tu découvriras le chemin vers le prochain fragment."])
        Elias = Character("Elias", "le libanais", Beyrouth, [" Ahlan wa sahlan ! Pour approcher le prochain fragment, suis la trace des civilisations anciennes. Cherche le lieu où les mystères du passé te guideront vers une terre ensoleillée où des constructions millénaires se dressent comme des énigmes à dévoiler. Là-bas, au cœur de l'antiquité, ton voyage continuera dans les profondeurs des secrets bien gardés."])
        Cleo = Character("Cleo", "l’égyptienne", Caire, ["Marhaban ! Au cœur de ce désert rempli d’histoire, ta quête touche à sa fin. Cherche le lieu où les ombres du passé convergent vers une terre hispanique de passion et de fête, où les œuvres humaines rivalisent avec la grandeur des étoiles. Ton ultime fragment t'attend dans une cité célèbre pour son architecture extraordinaire et son ambiance vibrante. "])
        Camille=Character("Camille","l'exploratrice intrépide",Fuji,["Salutations ! Si vous cherchez le prochain indice, aventurez-vous là où les brises légères caressent les cerisiers en fleurs. Dans cette terre où les sakuras s'épanouissent, vous découvrirez le fragment caché sous l'ombre d'une majesté silencieuse."])
        # Setup characters qui bougent dans la map
        Maria = Character("Maria", "l’espagnole", Barcelone, ["Hola ! Soy Maria, une Barcelonaise passionnée de cuisine. Mes journées sont rythmées par le parfum des tapas, les couleurs du marché de La Boqueria et les doux sons du flamenco. J'adore me promener le long de la plage et savourer une bonne paella. Si tu veux des conseils pour dénicher les meilleures saveurs de Barcelone, n'hésite pas !"])
        Mario = Character("Mario", "l’italien", Venice, ["Ciao! Sono Mario, un Vénitien naviguant à travers les canaux de cette ville magnifique. Mes journées sont remplies de gondoles, de masques vénitiens et d'une bonne dose de café italien. J'adore partager les histoires de cette ville unique et secrète. Si tu veux savoir où trouver les meilleurs cicchetti ou simplement discuter, sono qui!"])
        Volodimir = Character("Volodimir", "le russe", Moscou, ["Privet ! Je suis Volodimir, un amoureux de l'histoire de ma ville. Mes journées se déroulent au son des cloches des églises et parmi les pages de livres anciens. Né à Moscou, j'aime me promener dans les vastes parcs et profiter de l'architecture impressionnante. Si tu veux en savoir plus sur la vie à Moscou, n'hésite pas à me demander!"])
        Ozan = Character("Ozan", "le turc", Istanbul, ["Merhaba! Je suis Ozan, un passionné de musique et d'aventure. Mes journées sont une symphonie entre les ruelles animées du Grand Bazar, les rives du Bosphore et les sons envoûtants du saz. Né à Istanbul, je trouve toujours de nouvelles mélodies dans cette ville fascinante. Si tu veux partager des histoires ou simplement discuter, je suis là pour toi!"])

        aéroport.characters.append(le_chat_bleu)
        Istanbul.characters.append(Ozan)
        Fuji.characters.append(Camille)
        Moscou.characters.append(Volodimir)
        Barcelone.characters.append(Maria)
        Beyrouth.characters.append(Elias)
        NewYork.characters.append(Will)
        Caire.characters.append(Cleo)
        Tokyo.characters.append(Xiao)
        Paris.characters.append(Léa)
        Venice.characters.append(Mario)
        # Setup Items

        # NeW York
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
        lampe_d_Aladin = Item("Lampe d’Aladin", "Une lampe magique, prête à exaucer des vœux .")
        # Pyramide
        fragment5 = Item("Fragment5", "Morceau mystérieux")
        momie = Item("Momie", "Une momie ancienne, gardienne de secrets enfouis depuis des siècles. ")
        trésor = Item("Trésor", "Un coffre au trésor scellé, promettant richesse et aventures.")
        amulette = Item("Amulette", "Un talisman mystique, porteur de bonnes énergies et de protections. ")
        # Barcelone
        fragment6 = Item("Fragment6", "Morceau mystérieux")
        paella = Item("Paella", "Un plat espagnol traditionnel, riche en saveurs et en couleurs.")
        churros_con_chocolate = Item("Churros con chocolate","Délicieux beignets espagnols accompagnés d'une riche sauce au chocolat. ")
        tapas = Item("Tapas", "Une variété de petites bouchées espagnoles, offrant une explosion de saveurs.")
        # Venise
        masque_vénitien = Item("Masque vénitien","Un masque élaboré, utilisé lors du carnaval vénitien, porteur de mystère et de grâce.")
        chapeau = Item("Chapeau", "Un chapeau élégant, reflétant le style et la personnalité de son porteur.")
        # Gondole
        coffre = Item("Coffre", "Un coffre mystérieux, renfermant des secrets et des richesses inconnues.")
        pagaie = Item("Pagaie", "Une pagaie, prête à être utilisée pour naviguer sur des eaux inexplorées. ")
        # Moscou
        poupées_russe = Item("Poupées russe", "Une série de poupées emboîtées, cachant des surprises à chaque ouverture. ")
        chapka = Item("Chapka", "Un chapeau russe traditionnel, conçu pour affronter les hivers rigoureux.")
        # Istanbul
        loukoum = Item("Loukoum", "Des délices turcs, doux et parfumés, éveillant les papilles.")
        vase_ancien = Item("Vase ancien", "Un vase orné d'artefacts anciens, racontant des histoires du passé. ")
        bijoux = Item("Bijoux", "Des parures étincelantes, témoins de l'élégance et de la richesse.")
        assiettes = Item("Assiettes", "Des assiettes décoratives, portant des motifs artistiques et culturels. ")
        #Tokyo
        ramen_bowl = Item("Bol de Ramen", "Un bol débordant de ramen délicieusement parfumé, une spécialité tokyoïte.")
        manga_collection = Item("Collection de Manga","Une collection variée de mangas, représentant la richesse de la culture pop à Tokyo.")
        sakura_bonsai = Item("Bonsaï de Sakura","Un magnifique bonsaï de sakura en fleurs, capturant l'essence de la saison des cerisiers en fleurs.")
        tech_gadget = Item("Gadget Technologique","Un gadget high-tech dernier cri, symbole de l'innovation constante de Tokyo.")

        # Add items to specific rooms
        aéroport.inventory.append(coffre)
        aéroport.inventory.append(pagaie)
        Beyrouth.inventory.append(fragment4)
        Beyrouth.inventory.append(darbouka)
        Beyrouth.inventory.append(baklava)
        Venice.inventory.append(masque_vénitien)
        Venice.inventory.append(chapeau)
        Istanbul.inventory.append(loukoum)
        Istanbul.inventory.append(bijoux)
        Istanbul.inventory.append(assiettes)
        Istanbul.inventory.append(vase_ancien)
        Caire.inventory.append(scorpion)
        Caire.inventory.append(serpent)
        pyramide.inventory.append(momie)
        pyramide.inventory.append(trésor)
        pyramide.inventory.append(amulette)
        Tokyo.inventory.append(sakura_bonsai)
        Tokyo.inventory.append(tech_gadget)
        Paris.inventory.append(baguette)
        Paris.inventory.append(croissant)
        Paris.inventory.append(macaron)
        Paris.inventory.append(fragment3)
        NewYork.inventory.append(fragment1)
        NewYork.inventory.append(flambeau)
        Barcelone.inventory.append(paella)
        Barcelone.inventory.append(churros_con_chocolate)
        Barcelone.inventory.append(tapas)
        Barcelone.inventory.append(fragment6)
        Moscou.inventory.append(poupées_russe)
        Moscou.inventory.append(chapka)
        Fuji.inventory.append(fragment2)
        Fuji.inventory.append(fleur_de_sakura)
        pyramide.inventory.append(fragment5)
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
            response = command.action(self, list_of_words[1:])
            if self.game_over:
                response += "\nLe jeu est terminé. Vous avez échoué à ouvrir le coffre."
            return response

    def print_welcome(self):
        airport_description = self.player.current_room.get_long_description()
        welcome_message = f"Bienvenue dans ce jeu d'aventure ! {airport_description}\n"

        welcome_message += "Entrez 'help' si vous avez besoin d'aide."
        self.gui.print_to_output(welcome_message)
