import sys
import csv

def main():
    validate_info()

def validate_info():
    output = []

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(f"{sys.argv[1]}") as csvfile:
                reader = csv.DictReader(csvfile)
                for each_row in reader:
                    ratio = win_ratio(each_row["Win_Loss"])
                    differential = positive_or_negative(each_row["GoalDifferential"])
                    output.append({"Team Name": each_row["TeamName"], " Win/Loss": ratio, " Goal Differential": differential})
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
        else:
            with open(sys.argv[2], "w") as CSVfile:
                writer = csv.DictWriter(CSVfile, fieldnames=["Team Name", " Win/Loss", " Goal Differential"])
                writer.writeheader()
                for each_row in output:
                    writer.writerow(each_row)

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
