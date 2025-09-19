# Django Notes App

A simple, deployable Django notes application with user authentication.

## Features

- User registration and login
- Create, read, update, and delete notes
- User-specific notes (users can only see their own notes)
- Responsive Bootstrap UI
- Ready for deployment

## Setup Instructions

### 1. Clone or Download the Project

```bash
git clone <your-repo-url>
cd Notes_Website_Python
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Environment Configuration

Copy the example environment file and configure it:

```bash
copy env.example .env
```

Edit `.env` file and set your secret key:
```
SECRET_KEY=your-very-secret-key-here
DEBUG=True
```

### 6. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the application.

## Deployment

### Using Heroku

1. Install Heroku CLI
2. Create a Heroku app:
   ```bash
   heroku create your-app-name
   ```
3. Set environment variables:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   ```
4. Deploy:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

### Using Railway

1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False
3. Deploy automatically

### Using DigitalOcean App Platform

1. Connect your repository
2. Set environment variables
3. Deploy

## Usage

1. Register a new account or login
2. Create your first note
3. View, edit, or delete your notes
4. All notes are private to your account

## Project Structure

```
Notes_Website_Python/
├── manage.py
├── requirements.txt
├── notes_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── notes/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
└── templates/
    ├── base.html
    ├── registration/
    │   ├── login.html
    │   └── register.html
    └── notes/
        ├── note_list.html
        ├── note_detail.html
        ├── note_form.html
        └── note_confirm_delete.html
```

## Technologies Used

- Django 4.2.7
- Bootstrap 5.1.3
- Font Awesome 6.0.0
- SQLite (development)
- WhiteNoise (static files)
- Gunicorn (production server)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.
