FROM affectanalytics/server:latest

COPY ./tmp/ /app/
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["main-unittest.py"]
