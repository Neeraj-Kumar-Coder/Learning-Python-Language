# Health Management System of Neeraj, Harry and Rahul

def getTime():  # Function to return current time (given in the question)
    """Returns the current system time"""
    import datetime
    return str(datetime.datetime.now())


choice = int(input("What do you want to perform\n1. Add routine\n2. Get routine\n: "))

if choice == 1:
    name = int(input("Whose data you want to add?\n1. Neeraj\n2. Harry\n3. Rahul\n: "))
    activity = int(input("Enter what you want to add:\n1. Excercise\n2. Diet\n: "))
    if name == 1 and activity == 1:
        f11 = open("Neeraj_Exercise.txt", "a")
        data = input("Enter the exercise data here: ")
        writedata = "["+getTime()+"]: "+data+"\n"
        f11.write(writedata)
        f11.close()
    elif name == 1 and activity == 2:
        f12 = open("Neeraj_Diet.txt", "a")
        data = input("Enter the diet data here: ")
        writedata = "["+getTime()+"]: "+data+"\n"
        f12.write(writedata)
        f12.close()
    elif name == 2 and activity == 1:
        f21 = open("Harry_Exercise.txt", "a")
        data = input("Enter the exercise data here: ")
        writedata = "["+getTime()+"]: "+data+"\n"
        f21.write(writedata)
        f21.close()
    elif name == 2 and activity == 2:
        f22 = open("Harry_Diet.txt", "a")
        data = input("Enter the diet data here: ")
        writedata = "["+getTime()+"]: "+data+"\n"
        f22.write(writedata)
        f22.close()
    elif name == 3 and activity == 1:
        f31 = open("Rahul_Exercise.txt", "a")
        data = input("Enter the exercise data here: ")
        writedata = "["+getTime()+"]: "+data+"\n"
        f31.write(writedata)
        f31.close()
    elif name == 3 and activity == 2:
        f32 = open("Rahul_Diet.txt", "a")
        data = input("Enter the diet data here: ")
        writedata = "["+getTime()+"]: "+data+"\n"
        f32.write(writedata)
        f32.close()
    else:
        print("Enter a valid input!")
elif choice == 2:
    name = int(input("Whose data you want to read?\n1. Neeraj\n2. Harry\n3. Rahul\n: "))
    activity = int(input("Enter what you want to read:\n1. Excercise\n2. Diet\n: "))
    if name == 1 and activity == 1:
        f11 = open("Neeraj_Exercise.txt", "r")
        data = f11.read()
        print(data)
        f11.close()
    elif name == 1 and activity == 2:
        f12 = open("Neeraj_Diet.txt", "r")
        data = f12.read()
        print(data)
        f12.close()
    elif name == 2 and activity == 1:
        f21 = open("Harry_Exercise.txt", "r")
        data = f21.read()
        print(data)
        f21.close()
    elif name == 2 and activity == 2:
        f22 = open("Harry_Diet.txt", "r")
        data = f22.read()
        print(data)
        f22.close()
    elif name == 3 and activity == 1:
        f31 = open("Rahul_Exercise.txt", "r")
        data = f31.read()
        print(data)
        f31.close()
    elif name == 3 and activity == 2:
        f32 = open("Rahul_Diet.txt", "r")
        data = f32.read()
        print(data)
        f32.close()
    else:
        print("Enter a valid input!")
else:
    print("Enter a valid input!")