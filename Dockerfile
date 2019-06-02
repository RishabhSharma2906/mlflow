FROM python:3.6
COPY ./requirements.txt /build/requirements.txt
WORKDIR /build
RUN pip install -r requirements.txt
COPY MLService /build
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD ["app.py"]