FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY etl/ ./etl/
COPY pipeline.py .

# Create data directory
RUN mkdir -p data

# Run pipeline
CMD ["python", "pipeline.py"]