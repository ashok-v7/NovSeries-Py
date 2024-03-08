def isVowel(ch):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return True
    else:
        return False


def countVowel(s):
    count = 0
    for i in str:
        if isVowel(i):
            count += 1
    return count


str = "alice"
print("count of vowels:", countVowel(str))
