import json
import logging
from urllib.parse import urlencode
from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)


def get_course() -> float:
    url = "https://free.currconv.com/api/v7/convert?"
    params = {"q": "USD_RUB", "compact": "ultra", "apiKey": "b4eae1e78311f3a23590"}
    params = urlencode(params)
    request = Request(f"{url}{params}", method="GET")
    logger.info(f"Making request {request.full_url}")
    with urlopen(request) as response:
        response = response.read()
        response = json.loads(response)
        logger.info(f"Received response {response}")
    return response.get("USD_RUB")
