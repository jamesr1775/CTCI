import sys

def IsUnique(input_str):
    char_dict_count = {}
    for c in input_str:
        if c in char_dict_count:
            print("Not All Unique Chars Detected")
            return False
        else:
            char_dict_count[c] = True
    print("All Unique Chars Detected")
    return True

def main():
    print("argv:", sys.argv[1])
    IsUnique(sys.argv[1])
    
if __name__ == "__main__":
    main()
