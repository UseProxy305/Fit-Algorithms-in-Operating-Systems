# Fit-Algorithms-in-Operating-Systems
This repo includes all codes for the OS program that calculates with a given algorithm (First, Best and Worst).

How to run this script:
You have to run cmd (or powershell) in the folder where source codes are downloaded.
Run the main code in that command line with a python (version should be higher than 3.0)


## PROJECT DESCRIPTON
1) After you run the command python main.py, It will give you a welcome message and asks you to select Operating System Size
2) Select your desired algorithm (Lowercase or uppercase does not matter)
  *Example: Invalid Input Example for Selection of Algorithm*
![C__Windows_System32_cmd exe 2022-08-30 21-31-00](https://user-images.githubusercontent.com/61635625/187517014-7ed54c46-a378-4171-a18b-e8cf8dcf1936.gif)

3) After you adjusted bases of your OS, it will go to main menu. In that menu, there are 6 different options.

## Options
### 1)Display the OS Space   
&emsp;&emsp;It gives you a current situtation of OS.
<p align="center" width="100%">
    <img width="33%" src="https://user-images.githubusercontent.com/61635625/187523306-f16018fa-641c-4d10-a2eb-d9d2d8acee6f.png">
</p>


### 2)Add a program
   &emsp;&emsp;It provides user to add a new program into location that is determined by the choosen algorithm. The name and size is asken to user also. However, __user can give the program name as a just one letter.:exclamation:__ If there is no possible location, the system will recommend you to do compaction (option 4).
   
   
*Example: Adding a new program*   
<p align="center" width="100%">
    
  <img width="100%" src="https://user-images.githubusercontent.com/61635625/187523751-453b0d80-9624-4a42-874b-4938a8fc05ff.gif">
</p>


### 3)Remove a program


&emsp;&emsp;It helps users to delete a existing program in the OS. Script will ask user to enter the program name that user wants to delete. If OS does not have a program with that spesified name, it will give an warning message and return to main menu.

*Example: Removing a non-existing and existing programs*
<p align="center" width="100%">
    <img width="100%" src="https://user-images.githubusercontent.com/61635625/187529935-b6ba153a-a635-4ab8-a9e5-9b5c9a22fadc.gif">
</p>


### 4)Compaction

*Compaction is a technique to collect all the free memory present in form of fragments into one large chunk of free memory, which can be used to run other processes.* Retrieved from [GeeksforGeeks](https://www.geeksforgeeks.org/compaction-in-operating-system/#:~:text=Compaction%20is%20a%20technique%20to,used%20to%20run%20other%20processes.)

&emsp;&emsp;You can use same link ([GeeksforGeeks](https://www.geeksforgeeks.org/compaction-in-operating-system/#:~:text=Compaction%20is%20a%20technique%20to,used%20to%20run%20other%20processes.)) for further information about compaction.

*Example: Compaction*
<p align="center" width="100%">
    <img width="100%" src="https://user-images.githubusercontent.com/61635625/187537482-600d2c75-6e78-449e-ab16-754b881ef2ed.gif">
</p>


### 5)Clear all programs

   &emsp;&emsp;It will reset whole OS by deleting all programs. However, you can not change capacity of OS or fitting algorithm.

*Example: Reseting OS*
<p align="center" width="100%">
    <img width="100%" src="https://user-images.githubusercontent.com/61635625/187537897-ec8da98c-90d3-4c6a-b124-44fd19d1b191.gif">
</p>

  6)Quit the Program
  
  &emsp;&emsp;It provides users to quit the program.

*Example: Quiting*
<p align="center" width="100%">
    <img width="100%" src="https://user-images.githubusercontent.com/61635625/187538248-699e3ccd-ec5e-4bdf-b8fd-c53910c93c6c.gif">
</p>

