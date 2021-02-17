def func_print(*args):
    for name in args:
        print(name)


def func_kwarg(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


names = ["Neeraj", "Rahul", "Ajay", "Harry"]
func_print(*names)

dicoo = {"Neeraj": "Student", "Rahul": "Boy", "Rohan": "LOL"}
func_kwarg(**dicoo)
