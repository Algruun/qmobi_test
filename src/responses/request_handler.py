class RequestHandler:
    def __init__(self):
        self.content_type = ""
        self.content = None
        self.status = 200

    def get_content(self):
        return self.content

    def read(self):
        return self.content

    def set_status(self, status: int):
        self.status = status

    def get_status(self) -> int:
        return self.status

    def get_content_type(self) -> str:
        return self.content_type
