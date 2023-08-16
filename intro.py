def introduce_self(name: str, age: int) -> None:
    print("My name is " + name + "\n" + "My age is " + str(age))

def introduce_with_prompt():
    introduce_self(input("What is your name?"), input("What is your age?"))

introduce_with_prompt()