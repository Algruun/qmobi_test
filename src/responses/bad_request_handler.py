import json
import logging

from src.responses.json_handler import JsonHandler

logger = logging.getLogger(__name__)


class BadRequestHandler(JsonHandler):
    def __init__(self, message: str, code: int):
        super().__init__()
        self.set_status(code)
        self.content = json.dumps({"status": "error", "error": message})
        logger.debug(f"Preparing error response {self.get_status()} {self.content}")
