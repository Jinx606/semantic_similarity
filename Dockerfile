# Use the official PyPy base image
FROM pypy:latest

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install project dependencies
RUN pip install -r requirements.txt

# Run your Python script using PyPy
CMD ["pypy", "semantics.py"]
