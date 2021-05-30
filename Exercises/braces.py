

def braces(statement):
    open = []
    close = []
    check = []
    for i in statement:
        if i == '(' or i == '{' or i == '[':
            open.append(i)
        if i == ')' or i == '}' or i == ']':
            close.append(i)
    
    if len(open) != len(close):
        return False
    else:
        i = 0
        close = close[::-1]
        print (open, close)
        while i < len(open):
            if open[i] == '(' and close[i] == ')':
                check.append(True)
                i += 1
                continue
            if open[i] == '{' and close[i] == '}':
                check.append(True)
                i += 1
                continue
            if open[i] == '[' and close[i] == ']':
                check.append(True)
                i += 1
                continue
            else:
                check.append(False)
            i += 1
    return check

def check(my_string):
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
            print(my_string)
    return not my_string        
    
statement = '({[]})'
statement2 = '{][}'
statement3 = '[{]}'

print(check(statement3))
#print(braces(statement2))

    

