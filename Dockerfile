# Use an official Python runtime as the parent image
FROM public.ecr.aws/lambda/python:3.8

RUN python -m pip install shadow passwd

# Create a non-root user and switch to it
RUN addgroup --system appuser && adduser --system --gid appuser appuser
USER appuser

# Set the working directory in the container to /app
WORKDIR /app

# Copy just the requirements.txt first to leverage Docker cache
COPY --chown=appuser requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory (project_root/) contents into the container at /app
COPY --chown=appuser . .

# Set the CMD to your handler (this will vary depending on your Flask setup)
CMD ["app.lambda_handler"]
