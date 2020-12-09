import sys

def IsPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    charArray = [0]*128
    for char in str1:
        charArray[ord(char)] += 1
    for char in str2:
        charArray[ord(char)] -= 1
        if charArray[ord(char)] < 0:
            return False
    return True

def main():
    IsPermutation(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
