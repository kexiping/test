filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("what's your name?")
    if name == 'quit':
        break
    else:
        with open (filename, 'a', encoding = 'utf-8') as f:
            f.write(f"{name.title()}\n")
        print(f"Hi {name.title()}, you have been added to the guest book")