items = []

def preety_print():
    for row in items:
        for key,value in row.items():
            print(f"\t\t {key}:{value}",end = "|")

def entry():
    entry = True
    while entry:
        name_1 = input("Enter your name : ").strip().lower()
        money_1 = input("enter money : ").strip()

        product = {"name":name_1 , "money":money_1}
        items.append(product)    

        add = input("Would you like to add more[y/n]: ").strip().lower()
        if add != "yes" or add[0] != "y":
            entry = False

entry()
preety_print()