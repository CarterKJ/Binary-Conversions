def BinaryToInt(binary):
    curVal = 0
    binary = [char for char in binary]
    num = 0
    count = 0
    num = len(binary)-1
    for i in binary:
        if  binary[num] == "1":
            curVal += 2**count
        num -= 1
        count += 1
    return curVal

    
while True:
    binInput = input("Enter Binary:")
    print("Int is", BinaryToInt(binInput))
