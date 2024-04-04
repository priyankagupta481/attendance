# Orizzonte Employee Attendance System

The Orizzonte Employee Attendance System is a web application designed to manage employee attendance for Orizzonte Company. It provides features for user authentication, signup, login, and marking attendance.

## Features

- **User authentication**: Employees can sign up and log in to the system securely.
- **Signup with domain restriction**: Only email addresses with the orizzonte.com domain are allowed during signup.
- **Welcome page**: A visually appealing welcome page welcomes users to the system.
- **Login page**: Users can log in using their credentials.
- **Signup page**: New users can create an account with their email and password.
- **Marking attendance page**: Employees can mark their attendance, specifying whether they are working online or offline, providing their employee ID, time-in, and time-out.
- **Django administration panel integration**: Attendance records are stored and managed in the Django administration panel.
- **Automatic login time recording**: The system records the login time of users automatically.


## Prerequisites

- Python 3.x
- Django

## Installation

1. Clone the repository:
git clone https://github.com/priyankagupta481/attendance

2. Navigate to the project directory:
cd registration


3. Create and activate a virtual environment:
# python -m venv venv
# source venv/bin/activate # On Unix/Mac
# venv\Scripts\activate # On Windows


4. Install dependencies:
pip install -r requirements.txt

## Works

- Visit the homepage to access the registration functionality.
- Sign up or log in using valid credentials.
- Fill out the registration form with the required details.
- Submit the form to mark your attendance.

## Usage

1. Run the Django development server:
python manage.py runserver

2. Open your web browser and go to http://localhost:8000/registration to access the registration page.

3. Sign up or log in to access other functionalities like marking attendance.

## Dependencies
- Django
- Python
- Other dependencies listed in requirements.txt

## File Structure
- **admin.py**: Contains Django admin configurations for the Registration model.
- **forms.py**: Defines forms, including the RegistrationForm used in the project.
- **models.py**: Contains the Registration model definition.
- **views.py**: Defines views, including registration_page and related functions.
- **urls.py**: Contains URL patterns for routing within the app.


## Contributing
- Fork the repository.
- Create a new branch (git checkout -b feature/fooBar).
- Commit your changes (git commit -am 'Add some fooBar').
- Push to the branch (git push origin feature/fooBar).
- Create a new Pull Request.
