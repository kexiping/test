filename = 'learning_python.txt'

print("---Reading in the entire file:")
with open(filename, encoding = 'utf-8') as f:
    contents = f.read()
print(contents)

print("\n---Looping over the lines:")
with open(filename,encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())

print("\n---Storing the lines in a list:")
with open(filename, encoding = 'utf-8') as f:
    lines = f.readlines()
    
for line in lines:
    print(line.rstrip())