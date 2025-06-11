FROM python:3.9-slim

WORKDIR /src

# Copy requirements from the project root into the container
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY . .

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
