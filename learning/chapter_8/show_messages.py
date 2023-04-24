def show_messages(messages):
    """打印列表中的每条图文消息"""
    print("Showing all message:")
    for message in messages:
        print(message)
        
def send_messages(messages,sent_messages):
    """打印每条消息,再将其移到列表sent_messages中"""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)
    
messages = ["hello there", "how are you", ":)"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
