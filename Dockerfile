FROM python:3.9-slim-buster

# inside the container
WORKDIR /azurecontainerappsdemo


# source destination
COPY  ./requirements.txt /azurecontainerappsdemo/

# run pip install -r requirements.txt
RUN pip install -r requirements.txt

# source in local to destination in container
COPY ./main_app/ /azurecontainerappsdemo/

COPY ./.env /azurecontainerappsdemo/

EXPOSE 5000

# Use Gunicorn to run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "flask_test:app"]