#Writing Files
txt_data = "I Like pizza"

file_path = "C:/Users/LAXMI SAI KUMAR/OneDrive/Documents/Desktop/Output.txt"

#with open(file_path, "w") as file:                                              # w for Writing files
#    file.write(txt_data)
#    print(f"txt file '{file_path}' was created")

#try:
#    with open(file_path, "x") as file:                          #x for create mode   
#        file.write(txt_data)
#        print(f"txt file '{file_path}' was created")

#except FileExistsError:
#    print("That file already Exists!..")

try:
    with open(file_path, "a") as file:                          #x for add new information or data without deleting old data   
        file.write("\n" + txt_data)
        print(f"txt file added to '{file_path}'")

except FileExistsError:
    print("That file already Exists!..")
    