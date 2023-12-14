# The following line is a prebuilt dockerfile taken from dockerhub registry. Alpine is for small docker images
FROM python:3.7-alpine

# This command creates a new folder called app and makes it the working directory
WORKDIR /app

#This command puts all the files into a new folder virtual application called app
COPY . /app

# Then will do a pip install for requirements.txt file
RUN pip install -r requirements.txt

# Expose port 5000 where the app is being run to communicate with the docker file
EXPOSE 5000

# This command runs the app
CMD ["python", "app.py"]

# Next use the docker build command to run the files and create the docker image.
# Docker build command: docker build -t chevi .
# Command ran all of the steps successfully. 
# Checked the docker image by typing 'docker images'


# Next run the image on port 5001, 5000 is the hardwired port. 
# -d detaches the image and gives the id of the container
# Docker run command: docker run -d -p 5001:5000 chevi
# Docker ps command gives the container ID, the image, the command file, the ports, and a container name recursing_darwin
