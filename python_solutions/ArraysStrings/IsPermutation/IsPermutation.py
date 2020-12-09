import sys

def IsPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
    print(f"str1_sorted: {str1_sorted}")
    print(f"str1_sortee: {str2_sorted}")
    if str1_sorted != str2_sorted:
        return False
    return True

def main():
    IsPermutation(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()









