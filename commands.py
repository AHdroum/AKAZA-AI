import datetime

def about():
    print("""
    FRIDAY v1.0

    Created by Ahmed 
    
    """)


def say_time():
    now = datetime.datetime.now()
    print(f"FRIDAY: Current time is {now.hour}:{now.minute}")
def say_hello():
    print("friday:hello boss")

def say_goodbye():
    print("friday:goodbye boos")
    
def show_help():
    print("""
===== AVAILABLE COMMANDS =====

hello
bye
time
help
exit
""")