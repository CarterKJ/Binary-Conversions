def StrToAscii(text):
    place = 0
    text = [char for char in text]
    for i in text:
        text[place] = ord(text[place])
        place += 1
    AsciiToBinary(text)

def AsciiToBinary(ascii):
    place = 0
    for i in ascii:
        ascii[place] = bin(ascii[place])
        place += 1
    print("Binary is", ascii)
    
while True:
    binInput = input("Enter String:")
    StrToAscii(binInput)
