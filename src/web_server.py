from http.server import BaseHTTPRequestHandler
from typing import Dict

from src.responses.bad_request_handler import BadRequestHandler
from src.responses.json_handler import JsonHandler
from src.responses.request_handler import RequestHandler
from src.routes.main import routes


class WebServer(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path in routes:
            handler = JsonHandler()
            length = self.headers.get("content-length")
            try:
                nbytes = int(length)
            except (TypeError, ValueError):
                nbytes = 0
            if nbytes > 0:
                data = self.rfile.read(nbytes)
                handler.process(data)
            else:
                handler = BadRequestHandler("No body provided.", 400)
        else:
            handler = BadRequestHandler("Endpoint doesn't exist", 404)

        self.respond({"handler": handler})

    def handle_http(self, handler: RequestHandler) -> bytes:
        status_code = handler.get_status()

        self.send_response(status_code)

        content = handler.get_content()
        self.send_header("Content-type", handler.get_content_type())

        self.end_headers()

        return bytes(content, "UTF-8")

    def respond(self, opts: Dict[str, RequestHandler]):
        response = self.handle_http(opts["handler"])
        self.wfile.write(response)
