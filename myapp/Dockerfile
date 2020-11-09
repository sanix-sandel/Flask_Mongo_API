FROM python:3.8.2
# Set the working directory to /app
WORKDIR /myapp
#Copy local contents into the container
ADD . /myapp
#RUN python -m venv myenv
#Install all required dependencies
RUN pip3 install -r requirements.txt

EXPOSE 5000
 
CMD ["python", "run.py"] 
