import json
import logging
from json import JSONDecodeError

from src.converter import convert
from src.responses.request_handler import RequestHandler

logger = logging.getLogger(__name__)


class JsonHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self.content_type = "application/json"

    def process(self, payload):
        try:
            payload = json.loads(payload)
            requested_value, result = convert(payload)
            result = {
                "status": "OK",
                "resulted_currency": "RUB",
                "resulted_value": result,
                "requested_currency": "USD",
                "requested_value": requested_value,
            }
            self.content = json.dumps(result)
            self.set_status(200)
            logger.info(
                f"Preparing success response {self.get_status()} {self.content}"
            )
        except JSONDecodeError:
            self.content = json.dumps({"status": "error", "error": "Not a valid JSON."})
            self.set_status(400)
            logger.debug(f"Preparing error response {self.get_status()} {self.content}")
        except TypeError:
            self.content = json.dumps(
                {"status": "error", "error": "USD value must be int or float."}
            )
            self.set_status(400)
            logger.debug(f"Preparing error response {self.get_status()} {self.content}")
        except KeyError:
            self.content = json.dumps(
                {"status": "error", "error": 'Missing required "USD" parameter.'}
            )
            self.set_status(400)
            logger.debug(f"Preparing error response {self.get_status()} {self.content}")
        except Exception as e:
            self.content = json.dumps({"status": "error", "error": "Unknown error."})
            self.set_status(500)
            logger.error(e)
