FROM python:3.9-slim-buster

# inside the container
WORKDIR /azurecontainerappsdemo


# source destination
COPY  ./requirements.txt /azurecontainerappsdemo/

# run pip install -r requirements.txt
RUN pip install -r requirements.txt

COPY ./main_app/ /azurecontainerappsdemo/


ENV FLASK_APP new_app.py

EXPOSE 5000

CMD ["flask","run","--host=0.0.0.0"]