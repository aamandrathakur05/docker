# Use a lightweight base image (Python 3.9 Slim)
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /home/data

# Copy the Python script and text files into the container
COPY script.py /home/data/
COPY IF-1.txt /home/data/
COPY AlwaysRememberUsThisWay-1.txt /home/data/

# Install required dependencies
RUN pip install --no-cache-dir nltk

# Run the Python script when the container starts
CMD ["python", "/home/data/script.py"]
 
