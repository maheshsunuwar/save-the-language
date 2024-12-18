# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /save_the_language

# Copy the current directory contents into the container at /app
COPY . /save_the_language

# # Install system dependencies
RUN apt-get update -y && \
    apt-get install -y curl caddy unzip && \
    rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8082

# Run app.py when the container launches
CMD ["reflex", "run", "--env", "prod","--frontend-only", "--frontend-port", "8082"]
