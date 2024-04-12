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
            with open(sys.argv[2], "w") as CSVfile:
                writer = csv.DictWriter(CSVfile, fieldnames=["Team Name", " Win/Loss", " Goal Differential"])
                writer.writeheader()
                for each_row in output:
                    writer.writerow(each_row)

#similar to Fuel.py
def win_ratio(Win_Loss):
    x, y = Win_Loss.split("/")
    numb_x = int(x)
    numb_y = int(y)
    try:
        percent = (numb_x/numb_y)
    except(ZeroDivisionError):
        return " Perfect Record"
    if percent > 1:
        return " Winning Record"
    if percent < 1:
        return " Losing Record"
    else:
        return " Tying Record"

def positive_or_negative(GoalDifferential):
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

if __name__ == "__main__":
    main()

"""
Dallas Sidekicks,1/14,-50
Chihuahua Savage,8/7,25
Mesquite Outlaws,9/6,10
Monterrey Flash,15/0,100
Harrisburg Heat,3/12,-20
"""
