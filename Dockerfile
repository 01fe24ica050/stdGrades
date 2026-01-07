# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy current directory contents into container
COPY . .

# Install dependencies if you have requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Command to run your script
ENTRYPOINT ["python", "student.py"]
