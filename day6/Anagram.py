#Q6.
#Write a python function, check_anagram() which accepts two strings
#and returns True, if one string is an anagram of another string.
#Otherwise returns False. The two strings are considered to be an anagram
#if they contain repeating characters but none of the characters repeat at the same position.
#The length of the strings should be the same.

def check_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        char_counts = {}
        for i in range(len(str1)):
            if str1[i] in char_counts:
                if char_counts[str1[i]] != i:
                    return False
            else:
                char_counts[str1[i]] = i
        for i in range(len(str2)):
            if str2[i] in char_counts:
                if char_counts[str2[i]] != i:
                    return False
            else:
                return False
        return True

str1 = "racecar"
str2 = "carrace"

if check_anagram(str1, str2):
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")
