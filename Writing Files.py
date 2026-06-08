#Writing Files (.txt, .json , .csv)
#txt_data = "I Like pizza"

#file_path = "C:/Users/LAXMI SAI KUMAR/OneDrive/Documents/Desktop/Output.txt"

#with open(file_path, "w") as file:                                              # w for Writing files
#    file.write(txt_data)
#    print(f"txt file '{file_path}' was created")

#try:
#    with open(file_path, "x") as file:                          #x for create mode   
#        file.write(txt_data)
#        print(f"txt file '{file_path}' was created")

#except FileExistsError:
#    print("That file already Exists!..")

#try:
#    with open(file_path, "a") as file:                          #x for add new information or data without deleting old data   
#        file.write("\n" + txt_data)
#        print(f"txt file added to '{file_path}'")

#except FileExistsError:
#    print("That file already Exists!..")


#Exercise on writing files

#empolyees = ["Saikumar", "RajaPriya", "Siri", "Anessa"]                                #for txt.file purpose

import json
empolyees = {
    "Name" : "Saikumar",
    "age"  : 30,
    "Role" : "Python developer"
}

file_path = "C:/Users/LAXMI SAI KUMAR/OneDrive/Documents/Desktop/Output.json"

try:
    with open(file_path, "w") as file:
#        for empolyee in empolyees:                            # for txtfile it should be iterates
#            file.write(empolyee + " ")
            json.dump(empolyees , file, indent=4)                                         #dump() method will convert our dictnory to json String
            print(f"json file '{file_path}' was created")
            
except FileExistsError:
    print("file already exists!...")
    
    