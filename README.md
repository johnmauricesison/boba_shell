# 🧋 Boba Interactive Shell Program (BobaShell)

## 📝 Program Description
The **Boba Interactive Shell Program (BobaShell)** is a Python-based interactive command-line program that runs locally on your computer.  
It simulates a simple shell where users can perform basic file system operations such as changing directories, listing directory contents, creating folders, and creating files.

When executed, the shell starts a **continuous loop waiting for user commands**.  
It displays output after each operation and continues running until you type the command **`exit`**, which terminates the shell immediately without confirmation.

---

## 🧩 Command Behavior and Rules

- Each input/line is a **single command only**.  
  **Chaining multiple commands in one line is not supported.**

- The main sequence of operations consists of:
  - Changing the directory (`cd`)
  - Showing directory contents (`ls`)
  - Creating directories (`mkdir`)
  - Creating files (`createfile`)

- Additional commands such as `pwd`, `help`, `process`, and `exit` are included for better usability.

- The `ls` command shows all files and folders in **alphabetical order**.

- The `help` command displays all available commands as plain text; it is **not interactive**.

- The `exit` command ends the program **immediately**—no prompt or confirmation.

- Every command you type (except `exit`) is recorded in a **HISTORY log**.  
  When you type **`process`**, the program prints all commands entered in the current session, in order, excluding the `exit` command.

---

## 🏗️ Infrastructure and Design

### Flow Summary
The design of **BobaShell** follows a simple and clear loop:

1. **Start Program** → User runs the Python file.  
2. **Input Stage** → The user enters a command.  
3. **Decision Stage** → The program determines which command to execute.  
4. **Processing Stage** → Executes the desired operation.  
5. **Output Stage** → Displays the result to the user.  
6. **Loop** → Returns to the input stage for the next command.  

This cycle continues until the **`exit`** command is executed, which breaks the loop and stops the shell.

---

## 💻 Command Operations

| Command | Description |
|----------|--------------|
| **help** | Shows all available commands and their descriptions. |
| **exit** | Terminates the program immediately. |
| **pwd** | Prints the current working directory. |
| **ls** | Lists all files and folders in the current directory (alphabetically). |
| **mkdir `<name>`** | Creates a new directory with the given name. |
| **cd `<path>`** | Changes the working directory to the given path. |
| **createfile `<filename>`** | Creates an empty file in the current directory. |
| **process** | Displays all commands executed in this session, excluding `exit`. |

---

## 🧠 Functional Explanation

- **Single command per line:** The shell accepts one command at a time and executes it directly.  
- **Alphabetical listing:** The `ls` command sorts and displays all directory contents alphabetically.  
- **Static help:** The `help` command is a fixed text output listing available commands.  
- **Immediate exit:** The `exit` command stops the program with no further confirmation.  
- **Command history:** Each command (except `exit`) is appended to a list. The `process` command displays that list.

---

## 🧾 Example Usage

```bash
> pwd
C:\Users\John\Documents

> mkdir Projects
Directory 'Projects' created.

> cd Projects
Changed directory to 'Projects'.

> createfile notes.txt
File 'notes.txt' created successfully.

> ls
notes.txt

> process
Command History:
1. pwd
2. mkdir Projects
3. cd Projects
4. createfile notes.txt
5. ls

> exit
Exiting BobaShell...
