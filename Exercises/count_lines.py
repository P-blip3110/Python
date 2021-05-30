count = 0
with open('C:\\Users\prde3\OneDrive\Learn\Python\Exercises\\txt_file.txt', 'r') as f:
    reader = f.readlines()
    for i in reader:
        count += 1
print(count)