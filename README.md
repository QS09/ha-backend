# DJANGO API

1. Install python3.10 or later version, **Ubuntu22.04** is recommended as it includes python3.10 as default python version.

Confirm python version.
```commandline
    python3 --version
```

Output is going to be like this:
```commandline
    #Output
    Python 3.10.10
```

The next step is to install python3-pip in order to manage Python packages. Let's use the built-in command:
```commandline
    sudo apt install python3-pip -y
```

To make sure the software environment is reliable, you need to install several packages
```commandline
    sudo apt install build-essential libssl-dev libffi-dev python3-dev
```

2. Set up and create a virtual environment
```commandline
    sudo apt install python3-venv -y
```

```commandline
    python3 -m venv env
```


3. Activate virtualenv and install python packages
```commandline
    source env/bin/activate
```

```commandline
    pip install -r requirements.txt
```

4. Migrate database.
```commandline
    python manage.py migrate
```

5. Create superuser for admin access
```commandline
    python manage.py createsuperuser
```

6. Run project
```commandline
    python manage.py runserver
```

7. Check the project is running properly
- Django Admin: http://localhost:8000/admin
- Swagger: http://localhost:8000/api/swagger
