# Use a general Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    curl unzip

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install


# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Fetch the models from S3
RUN aws s3 cp s3://background-removal-flask/saved_models/u2net_human_seg.pth ./saved_models/
RUN aws s3 cp s3://background-removal-flask/saved_models/u2net_portrait.pth ./saved_models/

# Copy the rest of your application
COPY . .

# Command to run gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]
