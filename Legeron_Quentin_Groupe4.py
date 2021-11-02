from random import *
tuple_heroes = (
    {"name": "Truand", "life": 12, "loss": 3, "gain": 1, "war_cry": "'Le roi des roublard c'est moi!'"},
    {"name": "Sage", "life": 15, "loss": 2, "gain": 1, "war_cry": "'Je suis le meilleur chasseur! "
                                                                  "J'ai combattu sans répis ! \n"
                                                                  "J'ai réussi à être vainqueur !\n"
                                                                  "J'ai gagné les défis ! \n"
                                                                  "J'ai parcourru la terre entierre !\n"
                                                                  "Traquant avec espoir !\n"
                                                                  "J'ai attrapé tous les trésors et leurs mystères!\n"
                                                                  "Je connais le secret de leurs pouvoirs !'"},
    {"name": "Goblin", "life": 20, "loss": 1, "gain": 3, "war_cry": "'Mon précieux ! "
                                                                    "Gnahaha je vais le garder avec moi!\n"
                                                                    "Oh non je ressemble de plus en plus à papi !\n"
                                                                    "Vite il faut que je sorte d'ici!!'"}
)

tuple_monsters = (
    {"name": "Fée", "good_spirit": True, "power": 1},
    {"name": "lutin", "good_spirit": True, "power": 1},
    {"name": "Elf", "good_spirit": True, "power": 1},
    {"name": "Nain", "good_spirit": True, "power": 2},
    {"name": "Zeldo", "good_spirit": True, "power": 3},
    {"name": "Phénix", "good_spirit": True, "power": 3},
    {"name": "Licorne", "good_spirit": True, "power": 4},
    {"name": "Déesse", "good_spirit": True, "power": 5},
    {"name": "Tavernier", "good_spirit": True, "power": 6},
    {"name": "Squelette", "good_spirit": False, "power": 1},
    {"name": "Zombie", "good_spirit": False, "power": 1},
    {"name": "Larbin", "good_spirit": False, "power": 1},
    {"name": "Momie", "good_spirit": False, "power": 2},
    {"name": "Sorcière", "good_spirit": False, "power": 3},
    {"name": "Lyche", "good_spirit": False, "power": 3},
    {"name": "Orc", "good_spirit": False, "power": 4},
    {"name": "Craken", "good_spirit": False, "power": 5},
    {"name": "Dragon", "good_spirit": False, "power": 6}
)

print("\nBienvenu à la cité des mages! Ici tous tes rêves peuvent se réaliser.\n")
print("Je vois que tu as envie d'en découdre et de réaliser tes rêves. \nMais ça ne va pas être facile crois moi.\n")
player_name = input("Avant que tu ne partes dis moi, quel est ton nom ? (c'est pour les registres à la douane ) \n")

print("Tu ne m'as toujours pas dis, où est-ce que tu te rends?")
difficulty = int(input(f"Dans l'ordre de difficulté tu as :\n"
                       f"1 : La grande bibliothèque et ses nombreuses salles énigmatiques\n"
                       f"2 : La tour principale des mages, avec son lot d'artefacts en tout genre\n"
                       f"3 : La porte des ames (la légende dirait que la fontaine de jouvence se trouve là-bas)\n"
                       f"Donne moi le chiffre qui correspond à ta destination"))

i = 0

while i != 1:

    if difficulty > 3 or difficulty < 1:
        difficulty = int(input(f"Non tu n'as pas compris il faut choisir 1, 2 ou 3. "))
        continue

    elif difficulty == 1:
        difficulty = 8
        break

    elif difficulty == 2:
        difficulty = 12
        break

    else:
        difficulty = 18
        break

print("\nAttend! Avant que tu ne partes j'ai encore besoin d'information (la douane tu connais)")
print("Parmis ces classes de heros laquel est-tu ?")

for hero in tuple_heroes:
    print(f" {hero['name']}")

type_hero = input("Ecrit ici le nom de ta classe : ")

while i != 1:

    if "tr" in type_hero.lower():
        type_hero = tuple_heroes[0]
        break

    elif "sa" in type_hero.lower():
        type_hero = tuple_heroes[1]
        break

    elif "go" in type_hero.lower():
        type_hero = tuple_heroes[2]
        break

    else:
        type_hero = input(f"Non tu n'as pas compris il faut choisir un des type que j'ai proposé. ")
        continue


def newdoor():

    new_monster = choice(tuple_monsters)
    other_monster = choice(tuple_monsters)

    print(f"Il te reste encore {type_hero['life']} vies.")
    door_choice = input("\nA toi de choisir. Tu veux prendre la porte de gauche ou la porte de droite ? ")

    i = 0

    while i != 1:

        if "dr" in door_choice.lower() or "ga" in door_choice.lower():
            print(f"\nIl y a des bruits qui proviennent de l'autre porte.\n"
                  f"Tu entends des bruits de {other_monster['name']}\n"
                  f"Mais tout ceci ne te ragardes pas. Peux être dans une autre vie.\n")
            break

        else:
            door_choice = input(f"Non tu n'as pas compris il faut choisir droite ou gauche. ")
            continue

    print(f"Tu tombe sur une nouvelle créature !\n Il s'agit de {new_monster['name']}")

    while new_monster["good_spirit"] == True:

        print(f"Ouf on a encore eu de la chance.\n"
              f"{new_monster['name']} te redonnes {new_monster['power'] + type_hero['gain']} points de vies.")
        type_hero['life'] = type_hero['life'] + new_monster['power'] + type_hero['gain']

        if type_hero['life'] > 20:
            print("Oh non tu ne peux pas avoir plus que 20 points de vies.\n"
                  "Tu as été obligé de te séparer du surplus.")
            type_hero['life'] = 20

        break

    while new_monster["good_spirit"] == False:

        print(f"Oh nooon ! Tu viens de tomber sur un monstre.\n"
              f"{new_monster['name']} te blesse et t'enlève {new_monster['power'] + type_hero['loss']} points de vies.")
        type_hero['life'] = type_hero['life'] - new_monster['power'] - type_hero['loss']

        break


for i in range(1, difficulty):
    if type_hero['life'] == 0:
        print("\nTu est tombé au sol. Inerte sans vie. Personne ne se souviendra de toi.\n\nGame Over\n\n")
        print(f"{player_name}, tu as perdu cette fois mais gagnerais-tu si tu faisais d'autres choix ?")
        break
    else:
        newdoor()

if type_hero['life'] != 0:
    print(f"\n\nBravo tu a trouvé le grand trésor de la vie!"
          f"\n Avec ce trésor tu sens que tu pourrais conquérire le monde !\n"
          f"Je vois que tu veux t'exprimer. Que veux-tu me dire ?\n\n"
          f"{type_hero['war_cry']}\n\n"
          f"Ah oui quand même ça fais beaucoup là, non ?\n\n"
          f"{player_name} félicitation peu de héros sont arrivé jusque là.\n"
          f"Est-ce qu'une nouvelle aventure te tenterais ?\n"
          f"Si oui tu n'as qu'à relancer une partie ;)")
