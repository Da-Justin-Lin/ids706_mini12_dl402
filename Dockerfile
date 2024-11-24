# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install flask

# Expose port 5000 for the app
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]