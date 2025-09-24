def greetUser(name):
    def greet(time):
        print(f"Good {time}, {name}")
    return greet

def main():
    # greet = greetUser("Abish")("Morning") -> Another Way of Assigning
    # greetUser() returns an Function Object stored in greet which requires another argument : time
    greet = greetUser("Abish")
    greet("Morning")


if __name__=="__main__":
    main()