# Django Authentication Application

## Overview

This Django application implements user authentication with email-based login. It includes features like signup, login, password reset, password change, dashboard, and profile pages with access control.

## Features

- User signup with email and password
- Login with email and password
- Forgot password with email reset link
- Change password functionality
- User dashboard with navigation
- User profile page with account details
- Access control for authenticated users

## Prerequisites

- Python 3.x
- Django 5.x

## Installation

1. **Clone the Repository:**

```bash
git clone https://github.com/harivansht/django-auth-app.git
cd django-auth-app
```

2. **Create Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

3. **Install Dependencies:**

```bash
pip install django
```

4. **Apply Migrations:**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create Superuser (Optional):**

```bash
python manage.py createsuperuser
```

6. **Run Server:**

```bash
python manage.py runserver
```

## Application URLs

- **Login:** `/login/`
- **Signup:** `/signup/`
- **Forgot Password:** `/forgot-password/`
- **Change Password:** `/change-password/`
- **Dashboard:** `/dashboard/`
- **Profile:** `/profile/`
