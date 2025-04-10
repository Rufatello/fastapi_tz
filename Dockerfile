FROM python:3.11.12-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]