import sys

def IsOneWay(str1, str2):
    if len(str1) - len(str2) == 0:
        return oneEditReplace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return oneEditInsert(str1, str2)
    elif len(str1) - 1 == len(str2):
         return oneEditInsert(str2, str1)
    else:
        return False

def oneEditInsert(str1, str2):
    index_s1 = 0
    index_s2 = 0
    while index_s2 < len(str2) and index_s1 < len(str1):
        if str1[index_s1] != str2[index_s2]:
            if index_s1 != index_s2:
                return False
            index_s2 += 1
        else:
            index_s1 += 1
            index_s2 += 1
    return True

def oneEditReplace(str1, str2):
    diff_c = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff_c += 1
        if diff_c > 1:
            return False
    return True

def main():
    print("argv:", sys.argv[1], sys.argv[2])
    IsOneWay(sys.argv[1], sys.argv[2])
    
if __name__ == "__main__":
    main()
