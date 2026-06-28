# Fleet Management App

A Python Django-based fleet management application designed to maintain vehicle records, track fleet operations, and manage driver training programs to enhance road safety and minimize accident risks.

## Features

- ✅ **Vehicle Registration**: Managed by the Super User.
- ✅ **Vehicle Tracking**: Vehicles are monitored based on condition ratings (Bad, Below Average, Average, and Good) submitted by the Super User.
- ✅ **Driver Training**: Training records are created and managed by the Super User.
- ✅ **Super User Profile**: Allows the Super User to manage and update their profile information.

## Setup

- **1. Install dependencies**: `pip install -r requirements.txt`
- **2. Run migrations**: `python manage.py migrate`
- **3. Run server**: `python manage.py runserver`
- **4. Superuser Credentials**: `Username: admin | Password: admin@123`

## Usage

- User can track their vehicles and driver training data through graph.
- User can submit the contact form for any enquiry or report.

## Technologies

- Python (version 3.9+)
- Django
- SQLite