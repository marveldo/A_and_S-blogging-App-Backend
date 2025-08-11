## Blogging API 

Blogging api where users can perform Crud operations on a Blog while also adding User Authentication and Authorization

## Setup Application

1. Create a Virtual Environment 
```sh
 python -m venv env
```
2. Activate virtual environment.
```sh
    /path/to/venv/bin/activate`
```
3. Install project dependencies `pip install -r requirements.txt`
4. Incase of Created Apps and Models First run 
```sh
python manage.py makemigrations
```
to create migration files then 
```sh
python manage.py migrate
```
to migrate those changes to the database 
5. Start server.
 ```sh
 python management.py runserver 
```
 you could also specify the host and port to run 
 ```sh
 python management.py runserver ${host} ${port}
 ```

 ## Extra Note 
 Always endeavour to check the sample.env to view extra environment variables added
