import logging
from http.server import HTTPServer

from src.config import HOST_NAME, PORT
from src.web_server import WebServer

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    httpd = HTTPServer((HOST_NAME, int(PORT)), WebServer)
    logger = logging.getLogger(__name__)
    logger.debug(f"Server Starts - {HOST_NAME}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logger.debug(f"Server Stops - {HOST_NAME}:{PORT}")
