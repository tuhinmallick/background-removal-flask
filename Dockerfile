# Use a general Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    curl \
    unzip

# Accept AWS Credentials and Region as build arguments
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG AWS_REGION

# Set the AWS Credentials and Region as environment variables for the AWS CLI
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV AWS_REGION=$AWS_REGION

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    sudo ./aws/install

# Use AWS CLI to copy the models from S3
RUN aws s3 cp s3://background-removal-flask/saved_models/u2net_human_seg.pth saved_models/u2net_human_seg.pth && \
    aws s3 cp s3://background-removal-flask/saved_models/u2net_portrait.pth saved_models/u2net_portrait.pth

# Unset AWS Credentials and Region for security
RUN unset AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_REGION

# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Copy the Haar Cascade XML (assuming it's not in S3)
COPY saved_models/haarcascade_frontalface_default.xml saved_models/haarcascade_frontalface_default.xml

# Copy the rest of your application
COPY . .

# Command to run Flask's development server
CMD ["python", "run.py"]
