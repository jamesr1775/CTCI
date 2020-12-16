import sys

def IsPalindromePermutation(string):
    wordCount = {}
    oddCount = 0
    for c in string:
        if c in wordCount:
            wordCount[c] += 1
        else:
            wordCount[c] = 1
        if wordCount[c]%2 != 0:
            oddCount += 1
        else:
            oddCount -= 1
    return True if oddCount <= 1 else False

def main():
    print(IsPalindromePermutation(sys.argv[1])) 

if __name__ == "__main__":
    main()

