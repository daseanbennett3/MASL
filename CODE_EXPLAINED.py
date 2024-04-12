#import sys to validate the command-line arguments
import sys
#import csv to read and write to a csv file
import csv

def main():
    validate_info()

#python[] code.py[0] team_stats.csv[1] team_standings.csv[2]
def validate_info():
    output = []

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #the following refers to line #9  
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        #read the team_stats.csv file if the input has passed all of the above (lines #13 - #19)
        try:
            #open and read the input(team_stats.csv)
            with open(f"{sys.argv[1]}") as csvfile:
                reader = csv.DictReader(csvfile)
                #read through every row
                for each_row in reader:
                    #create a variable equal to a function that reads the win_loss stats from the team_stats.csv file
                    ratio = win_ratio(each_row["Win_Loss"])
                    #create a variable equal to a function that reads the goal differentials from the team_stats.csv file. 
                    differential = positive_or_negative(each_row["GoalDifferential"])
                    #add to the empty list the team name which is found in the Team Name row of team_stats.csv. Do the same for the Win/Loss and Goal Differential rows.  
                    output.append({"Team Name": each_row["TeamName"], " Win/Loss": ratio, " Goal Differential": differential})
        #exit the program if the CSV file cannot be read          
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
        else:
            #open and write to the new csv file (team_standings.csv)
            with open(sys.argv[2], "w") as CSVfile:
                #write to the CSV file with "Team Name", "Win/Loss" and "Goal Differential" as the headers
                writer = csv.DictWriter(CSVfile, fieldnames=["Team Name", " Win/Loss", " Goal Differential"])
                #write to the header
                writer.writeheader()
                #write to the file row by row
                for each_row in output:
                    writer.writerow(each_row)
                    
#use the function referenced in line #29 to convert to the "#/#" stats to "X Record"
def win_ratio(Win_Loss):
    #split the input on the "/" so you just work with the numbers
    x, y = Win_Loss.split("/")
    #convert the numbers to numbers that python can read ie integers
    numb_x = int(x)
    numb_y = int(y)
    #create a variable equal to quotient of the numbers that were just split
    try:
        percent = (numb_x/numb_y)
    #if dividing a number by 0 in pyhton, it is considered a Zero Division Error
    except(ZeroDivisionError):
        return " Perfect Record"
    if percent > 1:
        return " Winning Record"
    if percent < 1:
        return " Losing Record"
    else:
        return " Tying Record"

#use the function referenced in line #31 to convert the Goal Differential to either 'Positive' or 'Negative' with a 'Super' prefix if above or below 25 or -25 respectively
def positive_or_negative(GoalDifferential):
    #convert the Goal Differential to a readable number ie an integer
    if int(GoalDifferential) > 0 and int(GoalDifferential) <= 25:
        return " Positive"
    elif int(GoalDifferential) > 25:
        return " Super Positive"
    elif int(GoalDifferential) < 0 and int(GoalDifferential) >= -25:
        return " Negative"
    elif int(GoalDifferential) < -26:
        return " Super Negative"
    else:
        return " Neutral"

#always add this at the end
if __name__ == "__main__":
    main()
