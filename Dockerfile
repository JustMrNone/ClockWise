# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock /app/

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Install dependencies using Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the Django development server
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
