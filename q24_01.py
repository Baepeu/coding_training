def isAnagram(str1, str2):
    list_str1 = sorted(list(str1))
    list_str2 = sorted(list(str2))
    if len(str1) == len(str2) and (list_str1 == list_str2):
        return True
    return False

print("Enter two strings and I'll tell you if they are anagrams:")
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if isAnagram(str1,str2):
    print(f'"{str1}" and "{str2}" are anagrams.')