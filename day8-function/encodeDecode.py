alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
NewAlphabet=[]
def encode(text , shift):
    katabaru=""
    for a in range(len(alphabet)-1,-1,-1):

        if(a>=shift):
            NewAlphabet.insert(0,alphabet[a])
        else:
            NewAlphabet.append(alphabet[a])
    for i in range(len(text)):
        for j in range(len(NewAlphabet)):
            if(alphabet[j]==text[i]):
                katabaru+=NewAlphabet[j]
    print(f"Here's the {text} result: {katabaru}")
def decode(text,shift):
    katabaru=""
    for a in range(len(alphabet)-1,-1,-1):
        if(a>=shift):
            NewAlphabet.insert(0,alphabet[a])
        else:
            NewAlphabet.append(alphabet[a])
    for i in range(len(text)):
        for j in range(len(NewAlphabet)):
            if(NewAlphabet[j]==text[i]):
                katabaru+=alphabet[j]
    print(f"Here's the decoded result:{katabaru}")
while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if(direction=='decode'):
        decode(text,shift)
    else:
        encode(text,shift)
    status=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if(status=='no'):
        print("goodbye")
        break
