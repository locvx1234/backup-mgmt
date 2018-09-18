#FROM ubuntu:16.04
FROM python:3.6

MAINTAINER Ginkgo<nguyenhuyentrang1996@gmail.com>

RUN apt-get update && apt-get install -y supervisor

RUN mkdir /code

RUN mkdir -p /var/log/supervisor
COPY ./supervisor/supervisord.conf /etc/supervisor/conf.d/

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install gunicorn psycopg2

ADD . /code/

#RUN pip install gunicorn psycopg2
#RUN apt-get install -y python-gevent

# COPY start.sh /code

# RUN chmod a+x /code/start.sh

# ENTRYPOINT ["/code/start.sh"]

# EXPOSE 8008

# RUN cd backup

CMD ["/usr/bin/supervisord"]

#CMD ["gunicorn -b 0.0.0.0:8000 backup.wsgi:application --reload"]

#CMD ["python3 manage.py runserver 0.0.0.0:8008"]
