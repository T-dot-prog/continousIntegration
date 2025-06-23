# Use an official Python 3.10 image from Docker Hub
FROM python:3.10-slim-buster

# Set the working directory
WORKDIR /app

# Copy your application code
COPY . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8501

# Command to run the FastAPI app
CMD ["streamlit" ,"run", "app.py"]