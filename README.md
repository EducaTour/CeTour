# Project Name

## Table of Contents

1. [Project Overview](#1-project-overview)
1. [Installation](#2-installation)
   - [Prerequisites](#prerequisites)
   - [Clone the Repository](#clone-the-repository)
   - [Setup Environment](#setup-environment)
   - [Run the Application](#run-the-application)
1. [Configuration](#configuration)
   - [Environment Variables](#environment-variables)

---

## 1. Project Overview

Provide a brief overview of the project, including its purpose, goals, and key features. Describe the technologies and frameworks used.

## 2. Installation

### Prerequisites

List all dependencies and prerequisites that need to be installed before setting up the project.

1. Docker
1. Python (if applicable)
1. Git

### Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/EducaTour/CeTour.git
cd CeTour
```

### Setup Environment

1. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. Install dependencies:

   ```bash
   pip install -r app/requirements.txt
   ```

### Run the Application

- Development:

  ```bash
  docker-compose up --build
  ```

- Production:

  ```bash
   docker-compose -f docker-compose.prod.yml up --build
  ```

## Configuration

### Environment Variables

- Development:

  - `DEBUG`: Set to `1` for debugging mode.
  - `SECRET_KEY`: Secret key used by Django for cryptographic signing.
  - `GS_CREDENTIALS`: File path or content of Google Cloud Storage credentials JSON file.
  - `GS_PROJECT_ID`: Google Cloud Project ID.
  - `GS_BUCKET_NAME`: Google Cloud Storage bucket name.

- Production:
  - `SECRET_KEY`: Secret key used by Django for cryptographic signing.
  - `SQL_ENGINE`: Database engine (e.g., `django.db.backends.postgresql`).
  - `SQL_DATABASE`: Database name.
  - `SQL_USER`: Database user.
  - `SQL_PASSWORD`: Database password.
  - `SQL_HOST`: Database host.
  - `SQL_PORT`: Database port.
  - `DATABASE`: Database name for Docker container (if applicable).
  - `POSTGRES_USER`: PostgreSQL database user for Docker container (if applicable).
  - `POSTGRES_PASSWORD`: PostgreSQL database password for Docker container (if applicable).
  - `POSTGRES_DB`: PostgreSQL database name for Docker container (if applicable).
  - `CERTBOT_EMAIL`: Email address for Let's Encrypt certificate (if applicable).
  - `CERTBOT_DOMAIN`: Domain name for Let's Encrypt certificate (if applicable).
  - `GS_CREDENTIALS`: File path or content of Google Cloud Storage credentials JSON file.
  - `GS_PROJECT_ID`: Google Cloud Project ID.
  - `GS_BUCKET_NAME`: Google Cloud Storage bucket name.
