# Patient Platform

## Overview
This is a platform to monitor patients at home or in the hospitals.

## Project Description
### User
·Patients: Upload or update personal information and get access to only his/her information.

·Medical Professionals (Nurses and Doctors): Upload or update personal information and get access to the patients on his/her watch.

·Administrators: get access to information of all patients.

_Developers:_

·Application developers

·Device integrators

·Machine Learning Scientists

### Branching Structure

Each module will be implemented on its own branch.

Main only provides the final Cworking code for each module, and eventually pulls them together.

### Web Framework

We mainly use Django web framework to achieve the goals in this project and this web framework makes it a lot easier to operate in the project. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

## Modules
### Device Module
Units in the field of measurement are listed below.
| Test Item  | Unit   | Data Type|
|  ------|------|------|
|temperature| ℃|double]
|blood pressure|mmHg|double|
|pulse| bpm|double|
|oximeter| %|double|
|height| cm|int|
|weight| kg|int|
|glucometer| mg/dL|double|

### Chat Module
#### Patients
```bash
# Patient can enter measurement at any time
# Patient can write a text or upload video or voice message to the MP
# Patient can book an appointment with the MP
# Patient can view their medical measurements
```
#### Medical Professional (MP)
```bash
# Browse Patients
# Assign a medical device to a Patient
# Assign Alert and scheduling for medical measurement, e.g., 
# MP can input data for any patient
# MP can chat with patients using text, voice or videos.
# MP can read transcripts of Patient uploaded videos and messages
# MP can search for keywords in messages and chats
# MP have a calendar where they can show open time slots for appointments
# MP can see all appointments booked at any time
```

## Installation

### Prerequisites

#### 1. Install Python
Install ```python-3.7.2``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### 2. Install MySQL
Install ```mysql-8.0.15```. Follow the steps form the below reference document based on your Operating System.
Reference: [https://dev.mysql.com/doc/refman/5.5/en/](https://dev.mysql.com/doc/refman/5.5/en/)
#### 3. Setup virtual environment
```bash
# Install virtual environment
sudo pip install virtualenv
# Make a directory
mkdir envs
# Create virtual environment
virtualenv ./envs/
# Activate virtual environment
source envs/bin/activate
```
#### 4. Clone git repository
```bash
git clone "https://github.com/BU-XY/patient-platform"
```

#### 5. Install requirements
```bash
cd patient-platform/
pip install -r requirements.txt
#### 6. Load sample data into MySQL
```bash
# open mysql bash
mysql -u <mysql-user> -p
# Give the absolute path of the file
mysql> source ~/patient-platform/world.sql
mysql> exit;
```
#### 7. Edit project settings
```bash
# open settings file
vim panorbit/settings.py
# Edit Database configurations with your MySQL configurations.
# Search for DATABASES section.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'world',
        'USER': '<mysql-user>',
        'PASSWORD': '<mysql-password>',
        'HOST': '<mysql-host>',
        'PORT': '<mysql-port>',
    }
}
# Edit email configurations.
# Search for email configurations
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-email-password>'
EMAIL_PORT = 587
# save the file
```
#### 8. Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate
# For search feature we need to index certain tables to the haystack. For that run below command.
python manage.py rebuild_index
# Run the server
python manage.py runserver 0:8001
# your server is up on port 8001
```
Try opening [http://localhost:8001](http://localhost:8001) in the browser.
Now you are good to go.
