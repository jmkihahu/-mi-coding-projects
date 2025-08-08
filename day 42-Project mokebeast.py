import time,os
mokedex = {"name":None,"type":None,"spm":None,"HP":None,"MP":None}
print("\t\t 🎮 === MOKEBEASTS === 🎮")
print()
nama = input("Enter the character's name:\n").strip().capitalize()
typa = input("Enter the character's type i.e fire water earth air:\n").strip().lower()
ultima_move = input("Enter the character's ultimate move:\n").strip().capitalize()
health = int(input("Enter your character's starting health:\n"))
mana = int(input("Enter your character's mana points:\n"))
mokedex.update({"name":nama,"type":typa,"spm":ultima_move,"HP":health,"MP":mana})
time.sleep(2)
os.system("cls")
for name,char in mokedex.items():
    if typa == "fire":
        print(f" \t\t \033[31m {name}: {char}",)
    elif typa == "water":
        print(f" \t\t \033[36m {name}: {char}",)
    elif typa == "earth":
        print(f"\t\t \033[32m {name}: {char}",)
    elif typa == "air":
        print(f"\t\t \033[37m {name}: {char}",)









