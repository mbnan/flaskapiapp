FROM python
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
EXPOSE 5000
CMD ["python", "./app.py"]
