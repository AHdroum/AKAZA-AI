import datetime

def about():
    print("""
    AKAZA v1.0

    Created by Ahmed 
    
    """)


def say_time():
    now = datetime.datetime.now()
    print(f"AKAZA: Current time is {now.hour}:{now.minute}")
def say_hello():
    print("AKAZA: hello boss how i can help you?")

def say_goodbye():
    print("AKAZA: goodbye boos")
    
def show_help():
    commands = ["hello","bye","time","exit","about","help", "remember"
                , "whoami"]
    print("AKAZA: Available commands:")
    for command in commands:
        print ("-", command)


def whoami():
    file = open("user_name.txt","r")
    name = file.read()
    file.close()
    print(f"Your name is {name}")

def remember():
    name = input("whats is your name?")
    file = open("user_name.txt","w")
    file.write(name)
    file.close()
    print(f"Nice to meet you, {name}. I will remember that.")
