import logging
from typing import Dict, Tuple

from src.market_api import get_course

logger = logging.getLogger(__name__)


def convert(data: Dict[str, float]) -> Tuple[float, float]:
    amount = data["USD"]
    course = get_course()
    logger.info(f"Converting {amount} USD to RUB")
    return amount, amount * course
