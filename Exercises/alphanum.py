if __name__ == '__main__':
    s = input()
    for i in range(len(s)):
        char = s[i]
        if char.isalnum():
            return True
        if char.isalpha():
            return True
        if char.isdigit():
            return True
        if char.islower():
            return True
        if char.isupper():
            return True
        return False
            
        