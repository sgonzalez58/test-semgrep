FROM python:3.9

WORKDIR /app
COPY requirements.txt .
RUN pip install --cache-no-dir -r requirements.txt
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]
