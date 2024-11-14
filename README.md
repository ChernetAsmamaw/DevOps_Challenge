# Django To-Do API with DevOps Practices

This project demonstrates deploying a Dockerized Django application with essential DevOps practices. The application is a simple to-do API that includes user authentication, data persistence using PostgreSQL, and email notifications. The deployment involves using Docker, GitHub Actions for CI/CD, and Ansible for automation on a cloud server.

## Table of Contents

- [Project Setup](#project-setup)
- [Dockerization](#dockerization)
- [GitHub Actions CI Pipeline](#github-actions-ci-pipeline)
- [Ansible Deployment](#ansible-deployment)
- [Port Management](#port-management)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Resources](#resources)

## Project Setup

- **Framework**: Django (Backend API)
- **Database**: PostgreSQL
- **Authentication**: Custom user model with Django’s authentication framework
- **Email Notifications**: Configured using an SMTP server (example: MailHog)

## Dockerization

The project is split into multiple Docker containers:

- **Django Application**: Runs the Django app with Gunicorn as the WSGI server.
- **PostgreSQL Database**: Manages data persistence.
- **Nginx Web Server**: Serves as a reverse proxy to manage requests.
- **Email Server**: Configured for email notifications (example: MailHog).

Each service is defined in its own Dockerfile and orchestrated with `docker-compose.yml`.

## GitHub Actions CI Pipeline

The project includes a GitHub Actions CI pipeline located at `.github/workflows/main.yml` with the following steps:

- **Linting**: Checks for code quality.
- **Build and Test**: Builds Docker images and runs unit and integration tests.
- **Docker Hub Deployment**: Pushes successful builds to Docker Hub.

## Ansible Deployment

The Ansible playbook automates server configuration and application deployment, ensuring a smooth production setup. Key tasks include:

- **Installing Docker and Docker Compose**: Ensures Docker is available on the server.
- **Pulling Latest Docker Images**: Fetches the latest application images from Docker Hub.
- **Running the Application**: Uses `docker-compose up -d` to start the application in detached mode.

Server details:

- **IP Address**: 104.248.241.153
- **Username and Password**: Chernet Masresha Asmamaw

## Port Management

To avoid conflicts, unique ports have been assigned to each Docker service. Update `docker-compose.yml` and the Ansible playbook to reflect the following ports:

- **Nginx**: YOUR_NGINX_PORT
- **Django**: YOUR_DJANGO_PORT
- **Email Service**: YOUR_EMAIL_PORT

Replace `YOUR_NGINX_PORT`, `YOUR_DJANGO_PORT`, and `YOUR_EMAIL_PORT` with the specified ports.

## Getting Started

### Prerequisites

- Docker and Docker Compose
- Ansible
- GitHub account with Actions enabled
- SSH access to the server

### Step-by-Step Deployment

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/todo-api-devops.git
   cd todo-api-devops
   ```

2. **Set Up Environment Variables**: Create a `.env` file in the root directory with your configuration (see [Environment Variables](#environment-variables)).

3. **Run Docker Containers Locally**:

   ```bash
   docker-compose up -d
   ```

4. **Run the GitHub Actions CI Pipeline**:

   - Push your changes to GitHub to trigger the pipeline.
   - Ensure all checks (linting, testing, and deployment) pass successfully.

5. **Deploy Using Ansible**:
   ```bash
   ansible-playbook -i hosts.ini playbook.yml --ask-become-pass
   ```

## Environment Variables

Set the following environment variables in the `.env` file for sensitive data:

```dotenv
# Database
POSTGRES_DB=todo_db
POSTGRES_USER=YOUR_DB_USER
POSTGRES_PASSWORD=YOUR_DB_PASSWORD
DB_HOST=db
DB_PORT=5432

# Django
DJANGO_SECRET_KEY=YOUR_SECRET_KEY
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=YOUR_HOSTS

# Email
EMAIL_HOST=YOUR_EMAIL_HOST
EMAIL_PORT=YOUR_EMAIL_PORT
EMAIL_HOST_USER=YOUR_EMAIL_USER
EMAIL_HOST_PASSWORD=YOUR_EMAIL_PASSWORD
```

## Resources

- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Ansible Documentation](https://docs.ansible.com/)
- [Django Documentation](https://docs.djangoproject.com/)
