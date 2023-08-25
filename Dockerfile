# Use an official Python runtime as the parent image
FROM public.ecr.aws/lambda/python:3.8

# Set to lambda user 
USER lambda

# Set the working directory in the container to /app
WORKDIR /app

# Copy just the requirements.txt first to leverage Docker cache
COPY --chown=lambda requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory (project_root/) contents into the container at /app
COPY --chown=lambda . .

# Set the CMD to your handler (this will vary depending on your Flask setup)
CMD ["app.lambda_handler"]
