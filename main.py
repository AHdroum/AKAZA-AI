import commands

print ("==== FRIDAY ====")


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
    elif command == "exit":
        print ("FRIDAY SHUTTING DOWN.....")
        break
    else:
        print ("unknow command")