FROM python:3.6.1

COPY ./tmp/ /app/
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT python main.py -t $TOKEN -r $REPOS ${DELAY:+-d $DELAY} ${DEBUG:+-l}
