# 🎓 Course Management System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.0.4-green.svg)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern course management system built with Django 5.0.4, featuring a REST API and a clean web interface.

## ✨ Features

- 🎯 **Course management** — create, edit, and view courses
- 📚 **Course categories** — organize content by themes and topics
- 👥 **User system** — authentication and authorization
- 🔌 **REST API** — integration via Django Tastypie
- 🎨 **Modern UI** — responsive design using Django templates
- 🚀 **Rapid development** — production-ready structure

## 🏗️ Project structure

```
Course/
├── api/                 # REST API app
├── base/                # Django project settings
├── shop/                # Main app for courses
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   └── shop/            # Templates for the course pages
├── manage.py            # Django management
└── requirements.txt     # Python dependencies
```

## 🚀 Quickstart

### Prerequisites

- Python 3.10+
- pip or pipenv
- Git

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/course-management.git
   cd course-management
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

## 📱 Usage

### Web interface

- **Home page** (`/`) — list of all available courses
- **Course details** (`/course/<id>/`) — detailed information about a course
- **Admin panel** (`/admin/`) — manage courses and categories

### API Endpoints

- `GET /api/v1/courses/` — list all courses
- `GET /api/v1/courses/{id}/` — get a single course
- `GET /api/v1/categories/` — list all categories

## 🛠️ Tech stack

- **Backend**: Django 5.0.4
- **API**: Django Tastypie
- **Database**: SQLite3 (for development)
- **Frontend**: HTML, CSS, Django Templates, Bootstrap5
- **Authentication**: Django built-in auth

## 📊 Data models

### Course
- `title` — course title
- `price` — course price
- `students_qty` — number of students
- `reviews_qty` — number of reviews
- `category` — foreign key to category
- `created_at` — creation timestamp

### Category
- `title` — category title
- `created_at` — creation timestamp

## 🔧 Configuration

### Environment variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database

SQLite3 is used by default. For production, PostgreSQL is recommended:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test shop
python manage.py test api
```

## 📦 Deployment

### Docker (recommended)

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### Traditional deployment

1. Configure a web server (Nginx/Apache)
2. Configure a WSGI server (Gunicorn/uWSGI)
3. Update `ALLOWED_HOSTS` in `settings.py`
4. Set `DEBUG=False`
5. Configure static files

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See `LICENSE` for details.

## 👨‍💻 Author

**Muhammadrasul Kholov** — [@retra-project](https://github.com/retra-project)

## 🙏 Acknowledgements

- [Django](https://www.djangoproject.com/) — web framework
- [Django Tastypie](https://django-tastypie.readthedocs.io/) — REST API
- [Python](https://www.python.org/) — programming language

