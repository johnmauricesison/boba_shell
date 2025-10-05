# My Boba Shell
# John Maurice P. Sison

import os    #python library that allows to have access on operating system functions like cd, mkdir, etc.
from typing import List   #typing hint for the HISTORY list.

HISTORY: List[str] = [] # this list saves all the commands that the users entered.


#This is a string that contains an information about the commands that can be use in BobaShell.
HELP = """\
Commands:
  help                     Show this help
  exit                     Quit the shell
  pwd                      Print working directory
  ls                       List files and folders
  mkdir <name>             Make a directory in the current folder
  cd <path>                Change directory (.. to go up)
  createfile <filename>    Create an empty file (like 'touch')
  process                  Show the commands you have run (history)

"""

def run(cmd: str) -> str:     #function to process the command that the user enters.
    cmd = cmd.strip()         #remove space at the start/end of the user input.
    if not cmd:
        return "skip"         #the process will be skipped if the user just hit the enter button without input


    print(f"→ {cmd}")         #the command that the user entered will print so that the user can see or confirm.
    HISTORY.append(cmd)       #after that, it will save to the History list

    parts = cmd.split()       #splits the input into words
    name = parts[0].lower()   #first word is the command
    args = parts[1:]          #remaining words are arguments


    try:
        if name == "help":    
            print(HELP)         #the information will be displayed if the user entered the 'help' command

        elif name == "exit":    
            return "exit"       #the program will exit immediately from the BobaShell.

        elif name == "pwd":
            print(os.getcwd())  #if the command is 'pwd', it will print the current working directory path

        elif name == "ls":
            for item in sorted(os.listdir()):   #if the command is 'ls', it will list all the files/folders 
                                                #in the current folder in alphabetical order
                print(item)

        elif name == "mkdir":                       #if the command is 'mkdir', it will create the directory with
            if not args:                            #the given name, if not, then no folder name will be given
                print("Usage: mkdir <dirname>")
            else:
                os.mkdir(args[0])
                print(f"📂 Created '{args[0]}'")

        elif name == "cd":                          #if the command is 'cd', it will change directory path
            if not args:
                print("Usage: cd <path>")
            else:
                os.chdir(args[0])
                print(f"📍 Now in {os.getcwd()}")

        elif name == "createfile":                  #if the command is 'createfile <filename>', it will create
            if not args:                            #an empty file.
                print("Usage: createfile <filename>")
            else:

                open(args[0], "a").close()
                print(f"📝 Created '{args[0]}'")

        elif name == "process" or name == "history":    #if the command is 'process'/'history', it will print all
            if not HISTORY:                             #the commands that the user entered in order with number.
                print("No steps yet.")
            else:
                for i, h in enumerate(HISTORY, 1):
                    print(f"{i:02d}. {h}")

        else:
            print(f"Unknown command: {name}. Type 'help'.") #if invalid command entered

    except FileExistsError:             #this shows when trying to make directory that already exists.
        print("That already exists.")   
    except FileNotFoundError:           #this shows when the path or file is not found.
        print("Path or file not found.")
    except PermissionError:             #this shows when the OS denied the access.
        print("Permission denied.")
    except Exception as e:              #this shows if theres any other error.
        print(f"Error: {e}")

    return "ok"                         #normal return if the command was handled.

def main():
    #this prints a welcome/introductory message
    print("Welcome to Boba🧋 Shell  — type 'help' to see commands. Type 'exit' to quit.")
    while True:     #a loop until the user exits
        try:
            cwd = os.getcwd().replace("\\", "/")            #this get the current directory
            line = input(f"🧋bobashell:{cwd} > ").strip()   #this shows the prompt and get the users input
            status = run(line)                              #this process the inputs entered by calling the run function
            if status == "exit":                            #this end the shell if the user inputs 'exit' command
                print("👋 Goodbye!")
                return
        except KeyboardInterrupt:                           #this end the shell if the user press the ctrl+c 
            print("\n(press Ctrl+D or type 'exit' to quit)")
        except EOFError:                                    #this end the shell if the user press the ctrl+d
            print("\n👋 Goodbye!")
            return

if __name__ == "__main__":                                  
    main()  #calls the main loop
