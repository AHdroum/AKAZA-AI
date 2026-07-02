import commands

print ("       ==== AKAZA ====      ")


##commands.say_hello()
##commands.say_goodbye()
 
while True:
    command = input("YOU: ").lower()

    if command == "hello":
        commands.say_hello()

    elif command =="help":
        commands.show_help()
    elif command == "time":
        commands.say_time()

    elif command == "about":
        commands.about()

    elif command == "bye":
        commands.say_goodbye()

    elif command == "remember":
        commands.remember()

    elif command == "whoami":
        commands.whoami()

    elif command == "exit":
        print ("AKAZA SHUTTING DOWN.....")
        break
    else:
        print ("unknow command")
