# Use a general Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Copy the rest of your application
COPY . .

# Command to run Flask's development server
CMD ["python", "run.py"]
