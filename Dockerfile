FROM python:3.8.2
# Set the working directory to /app
WORKDIR /app
#Copy local contents into the container
ADD . /app
#Install all required dependencies
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD ["./app/myapp.py"]
