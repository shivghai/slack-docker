# Use a lightweight base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install required dependencies
RUN pip install -r requirements.txt

# Copy the Python script to the container
COPY main.py /app/main.py

# Specify the command to run the script
CMD ["python", "/app/main.py"]
