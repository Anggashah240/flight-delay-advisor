FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "-c", "print('=== FLIGHT DELAY & EU 261 ADVISOR CONTAINER READY ===')"]
