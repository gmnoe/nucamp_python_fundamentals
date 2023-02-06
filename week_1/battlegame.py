wizard = "Wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 180

wizard_damage = 150
elf_damage = 100
human_damage = 20
orc_damage = 30

dragon_hp = 300
dragon_damage = 50

while True:
    print("1)", wizard)
    print("2)", elf)
    print("3)" , human)
    print("4)", orc)
    print("5) Exit")
    character = input("Choose your character: ")
    if character == "1" or character.casefold() == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character.casefold() == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character.casefold() == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character == "4" or character.casefold() == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    elif character == "5" or character.casefold() == "exit":
        exit("Exited Game")
    else:
        print("Unknown Character")
        break
print("You have chosen the character: ", character)
print("Health ", my_hp)
print("Damage: ", my_damage)

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hitpoints are now: ", dragon_hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    my_hp = my_hp - dragon_damage
    print("The Dragon strikes back at the", character)
    print("The", character + "'s hitpoints are now: ", my_hp)
    if my_hp <= 0:
        print("The", character, "has lost the battle")
        break