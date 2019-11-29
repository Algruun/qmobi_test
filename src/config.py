import os

HOST_NAME = (
    "localhost" if "HOST_NAME" not in os.environ else os.environ.get("HOST_NAME")
)
PORT = 8000 if "PORT" not in os.environ else os.environ.get("PORT")
