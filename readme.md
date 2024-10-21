# Dependencies

All Dependencies are in the requirements.txt
To install dependencies:
`python -m venv venv`
Activate the virtual environment (venv) \* Always make sure your virtual environment is activated.
`./venv/Scripts/activate`
Install requirements.txt
`pip install -r requirements.txt`

# Starting the App

Start it from the vs code python debugger

# Layers in Web development

1: Visual Layer (HTML, CSS, Javascript). This is what is displayed on the web page

2: Service Layer (Python). This is your business logic and it lets the visual layer communicate with your database

- GET is retrieving data
- POST is create a new record
- PUT is updating an existing record
- DELETE is deleting a record

3: Data Layer (SQL/Database). This is where the data is stored as well as CRUD(Create, Read, Update, Delete) operations.
