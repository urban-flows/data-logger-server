# This is a containerised environment to run the server for
# development and testing purposes.

FROM python:3.9-slim-bullseye

# Install Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install web app
COPY data_logger_server /opt

CMD ["/opt/data_logger_server/wsgi.py"]
