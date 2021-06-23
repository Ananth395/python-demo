FROM python:alpine3.7 
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 
EXPOSE 5001
EXPOSE 9200
ENTRYPOINT [ "python" ] 
CMD [ "app.py" ]