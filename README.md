# Django To-Do API with DevOps Practices

A Django-based Todo API with DevOps practices including containerization, CI/CD pipeline, and automated deployment. Features include user authentication, PostgreSQL database integration, and email notifications.

## Features

- User authentication with custom user model
- Task management (CRUD operations)
- Task privacy (users can only access their own tasks)
- PostgreSQL database for data persistence
- Email notifications for task updates

## Technology Stack

- **Backend**: Django
- **Database**: PostgreSQL
- **Web Server**: Nginx
- **WSGI Server**: Gunicorn
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Configuration Management**: Ansible
- **Email Service**: Django send_mail

## Local Development Setup

Clone the repository:

```bash
git clone https://github.com/ChernetAsmamaw/DevOps_Challenge.git
cd DevOps_Challenge
```

Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Or on Windows: .\venv\Scripts\activate
```

Install dependencies and run migrations:

```bash
pip install -r requirements.txt
python manage.py migrate
```

Run tests:

```bash
python manage.py test todo.tests --settings=todo_project.test_settings
```

## Docker Setup

Start all services using Docker Compose:

```bash
# Build and start containers
docker-compose up --build -d

# View logs
docker-compose logs

# Stop services
docker-compose down
```

## Configuration

### Environment Variables

Create a `.env` file:

```dotenv
# Database
POSTGRES_DB=todo_db
POSTGRES_USER=dbuser
POSTGRES_PASSWORD=securepwd
DB_HOST=db
DB_PORT=5432

# Django
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,your-domain.com

# Email
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
```

## Deployment

### Server Access

```bash
ssh username@104.248.241.153
```

### Deployment Process

- Configure Ansible inventory with server details
- Run deployment:

```bash
ansible-playbook -i inventory.yml deploy.yml
```

### Port Configuration

- **Nginx**: 8400
- **APP**: 5000
- **PostgreSQL**: 5432

## API Endpoints

- **GET** `/todo/`: Lists user's todo list
- **POST** `/todo/add`: Create a new todo item
- **PUT** `/todo/edit`: Update details of an existing item
- **DELETE** `/todo/delete/`: Delete a todo item

## Monitoring

View container logs:

```bash
# Application logs
docker-compose logs web

# Nginx logs
docker-compose logs nginx

# Database logs
docker-compose logs db
```

## DEVOPS CHALLENGE BY CHERNET ASMAMAW
