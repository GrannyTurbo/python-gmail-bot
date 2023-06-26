from simplegmail import Gmail
import requests

gmail = Gmail()

flagged_senders = [
    "Teilo Lang Ford <teilolangford@gmail.com>"
    "Ifor Hepton <iforidh@gmail.com>"
]


def main():

    messages = gmail.get_unread_inbox()

    for message in messages:

        if str(message.sender) in flagged_senders:

            try:
                message = str(message.plain)

                request = requests.get(
                    "https://api.duckduckgo.com",
                    params = {"q": message,"format": "json"}
                    )

                data = request.json()
                
                print(data["Abstract"])


                '''
                params = {
                    "to": message.sender,
                    "sender": "iforidh@gmail.com.com",
                    "subject": f"reply to {message.subject}",
                    "msg_plain": data,
                    "signature": True
                    }
                '''
                #message.mark_as_read()
            except TypeError:
                print("A TypeError occured. There may have been an image in the email.")

if __name__ == '__main__':
    main()
