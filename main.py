import json
import logging
from pprint import pformat
from requests_sse import EventSource

#from quixstreams import Application


def main():
    logging.info("START")
    
    with EventSource(
                "http://github-firehose.libraries.io/events",
                timeout=30,
        )as event_source:
            for event in event_source:
                value = json.loads(event.data)
                key = value["id"]
                logging.info("Got: %s", pformat(value))
    
if __name__ == "__main__":
    try:
            logging.basicConfig(level="DEBUG")
            main()
    except KeyboardInterrupt:
        pass