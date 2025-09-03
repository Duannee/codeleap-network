# *Posts API (CodeLeap Network)*


---

## **Index**

1. [Description](#description)  
2. [Tech Stack](#tech-stack)  
3. [Installation and Setup](#installation-and-setup)    
4. [Authentication](#authentication)   
5. [Documentation](#documentation)    
6. [Tests](#tests)  
7. [Contato](#contato)

---

## **Description**
API built with Django and Django REST Framework to manage posts (CodeLeap challenge).
It provides create, list, retrieve, update, and delete operations.
Additionally, it includes interactive documentation available on Swagger.

---

## **Tech Stack**
- *Django 5.x* – web framework.
- *Django REST Framework* – REST APIs.
- *Drf-spectacular* – OpenAPI/Swagger docs.
- *Pytest, pytest-django, pytest-cov* – testing.
- *Model-bakery* – test utilities.
- *Django-cors-headers* – CORS.
- *Psycopg (psycopg[binary]) / dj-database-url* – PostgreSQL & DATABASE_URL parsing.
- *Python-dotenv* – local environment variables.
- *Gunicorn* – WSGI server (production).
- *Whitenoise* – static files (production).

---

## **Installation and Setup**

1. Clone o repositório:

```
git clone https://github.com/Duannee/codeleap-network
cd codeleap-network

```

2. Create & activate the virtual environment:
```
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows

```

3. Instale as dependências:
 ```
 pip install -U pip wheel
 pip install -r requirements.txt
 # or: pip install "psycopg[binary]"  # if using modern Postgres driver
 ```

5. Migrations 
```
cd src
python manage.py migrate

```

4. Run the application:
```
python manage.py runserver
```

---

## *Authentication*

The Api does not require authentication. All routes are public to simplify frontend consumption.

---

## *Documentation*

[Swagger UI — API Documentation (Production)](https://codeleap-network-d77t.onrender.com/api/docs/swagger-ui/)

Obs: It may take a while to load due to the free deploy on the render platform.

---

## *Tests*

Tests use pytest + pytest-django.

Run:
```
cd src
pytest
```
Coverage:
```
pytest --cov=posts --cov-report=term-missing

```

---


## *Contato*
- Desenvolvedor: Duanne Moraes
- Email: duannemoraes.dev@gmail.com
- LinkedIn: [Duanne Moraes Linkedin](https://www.linkedin.com/in/duanne-moraes-7a0376278/)

















  





