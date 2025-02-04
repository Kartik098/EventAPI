# Simplified Event Management API Specification

## 1. Project Overview

This project provides an event management system with user registration and ticket booking functionality. It consists of two Django apps:
1. **Authentication App:** Handles user registration and JWT-based authentication.
2. **Events App:** Manages event creation and ticket purchases.

---

## 2. Project Setup

### Prerequisites
- Python 3.x
- PostgreSQL/MySQL
- Virtual environment (optional)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kartik098/EventAPI.git
   cd eventapi
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
    `env\\Scripts\\activate` # On linux  source env/bin/activate 
   ```

3. Install dependencies:
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt
   ```

4. Configure `settings.py` for database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or 'django.db.backends.mysql'
        'NAME': 'eventapi_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',  # Change for MySQL
    }
}
```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

7. Start the server:
   ```bash
   python manage.py runserver
   ```

---

## 3. API Usage Guide

### Authentication

#### Register a new user
- **Endpoint:** `POST /api/register/`
- **Request Body:**
  ```json
  {
      "username": "john_doe",
      "password": "securepassword",
      "role": "User"
  }
  ```

#### Obtain JWT token
- **Endpoint:** `POST /api/token/`
- **Request Body:**
  ```json
  {
      "username": "john_doe",
      "password": "securepassword"
  }
  ```

#### Refresh JWT token
- **Endpoint:** `POST /api/token/refresh/`
- **Request Body:**
  ```json
  {
      "refresh": "your_refresh_token"
  }
  ```

### Event Management

#### List all events
- **Endpoint:** `GET /api/events/`

#### Create an event (Admin only)
- **Endpoint:** `POST /api/events/`
- **Request Body:**
  ```json
  {
      "name": "Music Concert",
      "date": "2025-02-10",
      "total_tickets": 100
  }
  ```

### Ticket Purchase

#### Purchase tickets
- **Endpoint:** `POST /api/events/{id}/purchase/`
- **Request Body:**
  ```json
  {
      "quantity": 2
  }
  ```

---

## 4. SQL Query Explanation

The following SQL query retrieves the top 3 events based on ticket sales:

```sql
SELECT event.id, event.name, event.date, event.total_tickets, SUM(ticket.quantity) AS tickets_sold
FROM event
JOIN ticket ON event.id = ticket.event_id
GROUP BY event.id, event.name, event.date, event.total_tickets
ORDER BY tickets_sold DESC
LIMIT 3;
```

**Explanation:**
1. Joins the `event` and `ticket` tables.
2. Groups by event details.
3. Orders by total tickets sold.
4. Limits the output to the top 3 events.

---

## 5. Considerations

- Ensure secure password hashing with Django's `make_password`.
- Use JWT for authentication.
- Implement permissions to restrict actions based on roles.
- Optimize database queries for large datasets.
- Add unit tests for core functionalities.

---



