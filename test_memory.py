name = input("AKAZA:What is your Name ?")


file = open("memory.txt","w")
file.write(name)
file.close()

file = open("memory.txt","r")
memory = file.read()
print ("hello", memory)
##print("AKAZA: Memory Saved!")