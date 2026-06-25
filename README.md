# Fleet Management App

A Django web application that facilitates collaboration between Drivers and Company Owner(Super User) to manage fleet problem in your area.

## Features

- Vehicle Register
- Vehicle Tracking is based on the vehicle condition i.e. Bad, Below Average, Average and Good submitted by Super user
- Driver Training
- Super user profile

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Run server: `python manage.py runserver`
4. Superuser Credentials: `Username: admin | Password: admin@123`

## Usage

- User can track their vehicle and driver training data through graph.
- User can submit the contact form for any enquiry or report.


## Technologies

- Python
- Django
- SQLite