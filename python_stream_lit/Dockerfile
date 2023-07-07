# Use the official Python 3.8.12 image as the base image
FROM python:3.8.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Set the default command to run the project using Streamlit
CMD ["streamlit", "run", "streamlit.py"]
