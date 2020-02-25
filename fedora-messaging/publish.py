from fedora_messaging.api import publish, Message
from fedora_messaging.config import conf
global msg
while True:
    msg = input("\n\nEnter the Message (Ctrl-C to exit): ")
    conf.setup_logging()
    message = Message(
        body={"message": msg}
    )
    publish(message)
