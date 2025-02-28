# Stage 1: Build stage
FROM python:3.9-slim AS build

# Set the working directory
WORKDIR /home/data

# Install dependencies (if necessary)
RUN pip install --no-cache-dir --upgrade pip

# Copy the script and other necessary files
COPY script.py /home/data/
COPY AlwaysRememberUsThisWay-1.txt /home/data/
COPY IF-1.txt /home/data/

# Stage 2: Final image
FROM python:3.9-alpine

# Set the working directory
WORKDIR /home/data

# Copy the built files from the previous stage
COPY --from=build /home/data /home/data/

# Install necessary dependencies in a slim Alpine image
RUN apk add --no-cache python3 py3-pip

# Run the script
CMD ["python3", "script.py"]
