import json
import csv
file_path = "C:/Users/LAXMI SAI KUMAR/OneDrive/Documents/Desktop/Output.csv"


try:
    with open(file_path, "r") as file:
#       content = file.read()                               #for tst.files
#       content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line[1])
#            print(content["Name"])
except FileNotFoundError:
    print("That file was not found")
    
except PermissionError:
    print("You do not have permission to read that file")
    


