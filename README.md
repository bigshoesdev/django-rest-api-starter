# CRUD Sample

## Requirements
1. Python 3.6+
1. Pipenv 

## Installation
1. Start Python virtual ENV
```
pipenv shell
```
2. Install dependencies
```
pipenv install
```
3. Run database migrations
```
python manage.py migrate
```
4. Create admin user
```
python manage.py createsuperuser --username admin
```

## Run application
```
python manage.py runserver
```
Once the server is running, visit http://127.0.0.1:8000 in your web browser. Now, you should see something like the following:

**Note:** access the Django admin interface here: http://127.0.0.1:8000/admin. Example:

## Endpoints
* ```api/login/```
* ```api/refresh/```
* ```api/users/ (GET)```
* ```api/users/1 (GET)```
* ```api/users/ (POST)```
* ```api/users/1 (PATCH)```
* ```api/users/1 (DELETE)```
## API/endpoint examples

### Login
```
URL: http://localhost:8000/api/login/  (POST)
Request: {'username': 'admin', 'password': 'admin'} 
Response: {"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYwMDEwMjU4NywianRpIjoiMjE3NmE1MTNhMTIyNDM5MmEwMTk0NDlhY2ZjNzg0NGIiLCJ1c2VyX2lkIjoxfQ.RjXDUt90_W7t6N-h4P333clLbQ5oDLHSS3suQ56w1_Q","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAwMTAyNTg3LCJqdGkiOiI4ZmY0YjVkMTNmMTY0MDk4YjVmMGE2MmUwMTRhMGUwZSIsInVzZXJfaWQiOjF9.pOof6NyWHSfFVcJrJhpQMlAEzFKpyR9aTj-og_OpVaE"}
```

### Create a user
```
URL: http://localhost:8000/api/users/  (POST)
Request: {
    "info": "Update Info",
    "email": "test@test.com",
    "username": "test",
    "password": "123456"
}
Response: {
    "id": 4,
    "email": "test@test.com",
    "username": "test",
    "info": "",
    "created_at": "2023-03-01T05:41:52.626985Z",
    "deleted_at": null
}
```

### Update a user
```
URL: http://localhost:8000/api/users/1/  (PATCH)
Headers: {"Authorization": "Bearer {ACCESS_TOKEN}"}
Request: {'info': 'Update Info'} or {'password': '123456'}
Response: {
    "id": 1,
    "email": "admin@admin.com",
    "username": "admin",
    "info": "Update Info",
    "created_at": "2023-03-01T04:48:34.828587Z",
    "deleted_at": null
}
```

### Delete a user
```
URL: http://localhost:8000/api/users/1/  (DELETE)
Headers: {"Authorization": "Bearer {ACCESS_TOKEN}"}
Response: {
    "id": 1,
    "email": "admin@admin.com",
    "username": "admin",
    "info": "Update Info",
    "created_at": "2023-03-01T04:48:34.828587Z",
    "deleted_at": "2023-03-01T05:14:41.078050Z"
}
```

### Read a  user
```
URL: http://localhost:8000/api/users/1/  (GET)
Headers: {"Authorization": "Bearer {ACCESS_TOKEN}"}
Response: {
    "id": 1,
    "email": "admin@admin.com",
    "username": "admin",
    "info": "TTT",
    "created_at": "2023-03-01T04:48:34.828587Z",
    "deleted_at": null
}
```

### Retrieve user list
```
URL: http://localhost:8000/api/users/  (GET)
Headers: {"Authorization": "Bearer {ACCESS_TOKEN}"}
Response: {
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "email": "admin@admin.com",
            "username": "admin",
            "info": "TTT",
            "created_at": "2023-03-01T04:48:34.828587Z",
            "deleted_at": null
        }
    ]
}
```

## Resources
* Properly installing Python - https://docs.python-guide.org/starting/installation/
* Installing pipenv - https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv
* Django REST Framework - https://www.django-rest-framework.org
* Django REST Framework Simple JWT - https://github.com/davesque/django-rest-framework-simplejwt
