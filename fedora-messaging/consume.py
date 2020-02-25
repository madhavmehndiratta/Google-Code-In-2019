from fedora_messaging.api import consume
from fedora_messaging.config import conf

conf.setup_logging()

def print_message(message):
    print(message)

if __name__ == "__main__":
    conf.setup_logging()
    consume(print_message)
