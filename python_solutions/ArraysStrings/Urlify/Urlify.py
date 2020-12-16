import sys

def Urlify(string, trueLength):
    numSpaces = 0
    string = list(string)
    for i in range(0, trueLength):
        if string[i] == " ":
            numSpaces += 1
    index = trueLength + numSpaces*2
    for i in range(trueLength-1, -1, -1):
        if string[i] == " ":
            string[index - 1] = "0"
            string[index - 2] = "2"
            string[index - 3] = "%"
            index = index - 3
        else:
            string[index - 1] = string[i]
            index -= 1
    return ''.join(string)

def main():
    print(Urlify(sys.argv[1], sys.argv[2]))

if __name__ == "__main__":
    main()

