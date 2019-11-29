FROM python:3.8
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH="${PYTHONPATH}:/app/src"

WORKDIR app/
COPY src/ src/

CMD ["python", "./src/server_runner.py"]