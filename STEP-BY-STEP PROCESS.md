1. Create The Input: a CSV file named TEAM_STATS.csv with three columns named "TeamName", "Win_Loss", and "GoalDifferential" with TeamName formatted any way, Win_Loss formatted n/n, and GoalDifferential formatted +/-n
2. Import The Modules: import sys becuase we will be using command-line arguments as a validatpr and import csv because we will be reading and writing into a CSV file.
3. Define The Main Function: def main with just one function that we will be used to validate the command-line argument that the user will type in.
4. Understanding The Function in the Main Function: We first want the user to type "python" followed by "code.py" in the [0] spot because that the name of the file to be ran. In the [1] spot wewant the name of the CSV file created as input ie  a file named "TEAM_STATS.csv" that we will be reading and in the [2] spot we want the name of the CSV file "TEAM_STANDINGS.csv" that we will be writing to.
5. Define The Function in the Main Function (Create a List): Start by creating an empty list
6. Check The Length if the CMD-Line Arg: If the LENgth of the SYStem.ARGVment (the input of the user in the command prompt) is less 3 then SYStem.EXIT() with a message. Do the same elif its greater than 3 since we want exactly 3 arguments after the user types "python"
7. Does [1] and [2] End in .CSV?: Continue the if-else statement with elif not the SYS.ARGVument in the [1] OR the [2] spot ENDSWITH ".CSV" then SYStem.EXIT() with a message.
8. END the IF-ELSE Statment with a TRY: Finish the IF-ELSE statement with the "catch all" ie the ELSE being availvale if the previous 3 condtions have passed.
9. TRY in the ELSE: Start the TRY WITH OPENing up the the input in the [1] as an F string that will be read AS a CSVFILE
10. Read the CSV File That Was Just Created: created a variable equal to a csv.DictReader that takes in the CSVFILE as its parameter
11. Read Through Every Row: Read through each_row in the variable that was created as the csv.DictReader
12. Read The Row From The Input: Create a variable equal to the desired new row name (row name to write to) that has each_row and ["the row to read"] as the parameters
13. Do The Same For The Next Column: 
