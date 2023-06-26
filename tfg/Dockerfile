FROM python:3.9-buster

# Environment variables
ENV HOME=/home/app/backend 

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

# Work directory  
RUN mkdir -p $HOME  
WORKDIR $HOME  

# Set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Install dependencies  
RUN pip install --upgrade pip  

# Copy whole project to your docker home directory. 
COPY . $HOME  

# Install dependencies. 
RUN pip install -r requirements.txt  

# Port where the Django app runs  
# EXPOSE 8040 -> Local docker

# Start server   
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8050