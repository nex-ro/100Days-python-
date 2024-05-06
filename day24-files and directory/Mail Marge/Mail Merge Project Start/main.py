#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./Input/Names/invited_names.txt") as name:
    allNames=(name.readlines())
    with open("./Input/Letters/starting_letter.txt") as letter:
        textContain = letter.read()
        for i in range (len(allNames)):
            name=allNames[i].strip('\n')
            with open(f"./Output/Invitation_letters_{name}",mode='w')as file:
                file.write(textContain.replace("[name]",name))














