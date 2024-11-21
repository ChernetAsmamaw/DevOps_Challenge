# Django To-Do API with DevOps Practices

This project demonstrates deploying a Dockerized Django application with essential DevOps practices. The application is a simple to-do API built using Django that includes user authentication, data persistence using PostgreSQL, and email notifications using Django's built-in email functionality.

## Project Setup

- **Framework**: Django (Backend API)
- **Database**: PostgreSQL
- **Authentication**: Custom user authentication
- **Email**: Django's built-in email library for notifications

## Dockerization

The project uses Docker to containerize different services:

- **Django Application**: Runs the Django app with Gunicorn
- **PostgreSQL Database**: Manages data persistence
- **Nginx Web Server**: Reverse proxy for managing requests

## Docker Commands

```bash
# Build Docker images
docker-compose build

# Start containers
docker-compose up -d

# Stop and remove containers
docker-compose down
```

## Email Configuration

Configure email settings in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
```

## Environment Variables

Create a `.env` file with:

```dotenv
# Database
POSTGRES_DB=todo_db
POSTGRES_USER=dbuser
POSTGRES_PASSWORD=securepassword
DB_HOST=db
DB_PORT=5432

# Django
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,your-domain.com

# Email
EMAIL_HOST=your-smtp-server
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-password
```

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Ansible Documentation](https://docs.ansible.com/)
- [Django Documentation](https://docs.djangoproject.com/)
