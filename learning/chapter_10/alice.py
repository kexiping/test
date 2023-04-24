filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry, the file alice.txt does not exist.")
else:
    #计算该文件大概包含多少单词。
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")