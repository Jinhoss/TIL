import sys
input = sys.stdin.readline
dic = {"ADD": 0, "ADDC": 1, "SUB": 2, "SUBC": 3, "MOV": 4, "MOVC": 5,
      "AND": 6, "ANDC": 7, "OR": 8, "ORC": 9, "NOT": 10, "MULT": 12,
      "MULTC": 13, "LSFTL": 14, "LSFTLC": 15, "LSFTR": 16, "LSFTRC": 17,
      "ASFTR": 18, "ASFTRC": 19, "RL": 20, "RLC": 21, "RR": 22, "RRC": 23}

for _ in range(int(input())):
    result = ''
    opcode, rD, rA, rB = input().split()
    result += bin(dic[opcode])[2:].zfill(5)+'0'
    result += bin(int(rD))[2:].zfill(3)
    result += bin(int(rA))[2:].zfill(3)
    if opcode[-1] == 'C':
        result += bin(int(rB))[2:].zfill(4)
    else:
        result += bin(int(rB))[2:].zfill(3)+'0'
    print(result)