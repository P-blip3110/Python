def count_substring(string, sub_string):
    count = 0
    sb = sub_string
    s = string
    if sb in string:
        start = string.find(sb[0])
        end = string.find(sb[len(sb)-1])
        string = string[:start] + string[end:]
        count +=1

    return count 

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)