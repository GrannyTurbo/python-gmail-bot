from simplegmail import Gmail
from duckduckgo_search import DDGS
from simplegmail.query import construct_query

gmail = Gmail()


def search(query):
    with DDGS() as ddgs:
        results = []
        for r in ddgs.text(
            "giraffe", region="uk-en", safesearch="Moderate", timelimit="y"
        ):
            results.append(r)
        result = []
        result.append(results[0]["body"])
        result.append(results[0]["href"])
        return result


def get_queried_inbox(query):
    messages = gmail.get_unread_inbox()
    messages = messages = gmail.get_messages(query=construct_query(query))
    return messages


def trim_sender(sender):
    sender = str(sender)
    sender = sender.split("<")
    sender = sender[1]
    sender = sender.split(">")
    sender = sender[0]
    return sender


def generate_message(prompt):
    results = search(prompt)
    message = f"{results[0]}\n{results[1]}"
    return message

def main():
    messages = get_queried_inbox(
        query={
            "sender": [
                #"teilolangford@gmail.com",
                "iforidh@gmail.com"
            ],
            "unread": True,
        }
    )

    for message in messages:

        try:

            sender = trim_sender(message.sender)

            message_str = str(message.plain)
            reply = generate_message(message_str)

            if reply.strip() != '':
                print(reply)
                params = {
                    "to": sender,
                    "sender": "iforidh@gmail.com",
                    "subject": "Automated reply",
                    "msg_plain": str(reply),
                    "msg_html": f"<p>{reply}</p>",
                    "signature": True,
                }

                message = gmail.send_message(**params)

                # message.mark_as_read()

        except IndexError:
            pass


if __name__ == "__main__":
    main()
