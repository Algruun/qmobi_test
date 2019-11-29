import os

HOST_NAME = (
    "localhost" if "HOST_NAME" not in os.environ else os.environ.get("HOST_NAME")
)
PORT = 8000 if "PORT" not in os.environ else os.environ.get("PORT")
CURRENCIES_API_KEY = (
    "b4eae1e78311f3a23590"
    if "CURRENCIES_API_KEY" not in os.environ
    else os.environ.get("CURRENCIES_API_KEY")
)
