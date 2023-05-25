FROM python:3.11.0
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]