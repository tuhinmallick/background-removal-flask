# Use an official Python runtime as the parent image
FROM public.ecr.aws/lambda/python:3.11

# Set the working directory in the container to /app
WORKDIR /app

# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Upgrade pip first
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory (project_root/) contents into the container at /app
COPY . .

# Set the CMD to your handler (this will vary depending on your Flask setup)
CMD ["app.run.lambda_handler"]
