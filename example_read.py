from simplegmail import Gmail

gmail = Gmail()

# Unread messages in your inbox
messages = gmail.get_unread_inbox()

# Starred messages
#messages = gmail.get_starred_messages()

# ...and many more easy to use functions can be found in gmail.py!

# Print them out!
for message in messages:
    #print("To: " + message.recipient)
    print(message.sender)
    #print("Subject: " + message.subject)
    #print("Date: " + message.date)
    #print("Preview: " + message.snippet)

    #try:
        #print("Message Body: " + message.plain)  # or message.html
    #except TypeError:
        #print("A TypeError occured. There may have been an image in the email.")
