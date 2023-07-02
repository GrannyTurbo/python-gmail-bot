from simplegmail import Gmail
from duckduckgo_search import DDGS
from simplegmail.query import construct_query

gmail = Gmail()

def search(query):
    with DDGS() as ddgs:
        results = []
        for r in ddgs.text('giraffe', region='uk-en', safesearch='Moderate', timelimit='y'):
            results.append(r)
        result = []
        result.append(results[0]['body'])
        result.append(results.append[0]['href'])
        return result

def get_queried_inbox(query):
    messages = gmail.get_unread_inbox()
    messages = messages = gmail.get_messages(
        query=construct_query(query)
    )
    return messages

def trim_sender(sender):
    sender = str(sender)
    sender = sender.split('<')
    sender = sender[1]
    sender = sender.split('>')
    sender = sender[0]
    return sender

def generate_message(prompt):
    search = search(prompt)
    message = f"{search[0]}\n{search[1]}"

def main():

    messages = get_queried_inbox(
        query = {
            'sender': [
                'teilolangford@gmail.com',
                'iforidh@gmail.com'
            ],
            'unread':True
        }
    )

    for message in messages:

        sender = trim_sender(message.sender)

        message_str = str(message.plain)
        reply = generate_message(message_str)

        params = {
            "to": sender,
            "sender": "iforidh@gmail.com",
            "subject": "Automated reply",
            "msg_plain": reply,
            "signature": True
            }

        message = gmail.send_message(**params)

        #message.mark_as_read()

if __name__ == '__main__':
    main()
