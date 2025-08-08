import time

students = []

def preprint():
    print()
    for row in students:
        for value in row.values():
            print(f"  {value:^10}",end = " | ")
        print()
    print()


def write():
        print('Creating a new file')

        name = input('Enter a name for your file: ')+'.txt'  # Name of text file coerced with +.txt

        try:
            file = open(name,'w')   # Trying to create a new file or open one
            file.close()

        except:
            print('Something went wrong! Cannot tell what?')
             # quit Python


name = ""
ages = ""
gender = ""
hobby = "" 

entry = True

while entry :
    name = input("enter your name: ").lower().strip()
    ages= input("enter your age: ").strip()
    gender = input("enter your gender: ").lower().strip()
    hobby = input("enter your hobby: ").lower().strip()

    students_info = {"name":name,
                 "age":ages,
                 "gender":gender,
                 "hobbies":hobby}

    students.append(students_info)

    add = input("Would you lke to add more students : ").lower().strip()

    if add  != "yes"or add[0] != "y":
        entry = False

time.sleep(1)

write()

time.sleep(1)

preprint()