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

# Explicitly copy the models and the Haar Cascade XML
COPY saved_models/u2net_human_seg.pth saved_models/u2net_human_seg.pth
COPY saved_models/u2net_portrait.pth saved_models/u2net_portrait.pth
COPY saved_models/haarcascade_frontalface_default.xml saved_models/haarcascade_frontalface_default.xml

# Copy the rest of your application
COPY . .

# Command to run Flask's development server
CMD ["python", "run.py"]
