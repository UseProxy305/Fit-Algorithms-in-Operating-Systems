from OS import OS
def printHelloMessage():
    print("Welcome to OS simulation for simulation...")
    print("Before starting, let me know some information about OS...")
if __name__=="__main__":
    printHelloMessage()
    size=int(input("Enter the OS size "))
    method=input("Select one of the OS fitting methods (F for First/ B for Best/ W for Worst): ").capitalize()
    while(True):            
        if(method in ["F","B","W"]):
            break
        method=input("Please enter F,B, or W: ").capitalize()

    bi=OS(size,method)
    while(True):
        opt=input("\nSelect an option:(1,2,3,4,5,6)\n\n{:<25}{:<25}\n{:<25}{:<25}\n{:<25}{:<25}\n\n".format("1)Display the OS Space","4)Compaction","2)Add a program","5)Clear all programs","3)Remove a program","6)Quit the Program"))
        print("\n---------------------------------------------------------------\n")
        if(opt=="1"):
            bi.printArrays()
        elif(opt=="2"):
            programSize=int(input("Enter the program size "))
            programName=input("Enter the program name ")
            bi.fit(programSize,programName)
        elif(opt=="3"):
            programName=input("Enter the program name ")
            bi.deleteProgram(programName)
        elif(opt=="4"):
            bi.compaction()
        elif(opt=="5"):
            bi=OS(size,method)
        elif(opt=="6"):
            opt=input("Do you want to quit?...(y/N)")
            if(opt=="y"):
                break
        else:
            print("Unknown option...")
        print("\n---------------------------------------------------------------\n")