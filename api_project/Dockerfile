FROM python:3.8-slim-buster

# Set up the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project into the container
COPY . .

# Expose the port used by the Django development server
EXPOSE 8004

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8004"]
