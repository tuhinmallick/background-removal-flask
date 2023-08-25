# Use a general Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy just the requirements.txt first to leverage Docker cache
COPY requirements.txt .
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Copy the rest of your application
COPY . .

# Command to run gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "run:app"]
