FROM --platform=linux/amd64 python:3.10
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY src src
CMD ["uvicorn", "src.main:app","--host","0.0.0.0" ,"--port", "80"]
