import re
for i in range(int(input())):
    inVal = input()
    inVal2 = input()

    patternA = re.sub("_", "[A-Z]", inVal)
    patternB = re.sub("_", "", inVal)
    mA = re.fullmatch(patternA, inVal2)
    mB = re.fullmatch(patternB, inVal2)

    if not mA:
        print("!")
    elif mB:
        print("_")
    else:
        for i in range(26):
            c = chr(ord('A')+i)
            patternRST = re.sub("_", c, inVal)
            if re.fullmatch(patternRST, inVal2):
                print(c)