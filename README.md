# HexaAPI
FastAPI integrated database for enterprise administration and client-order management

## Getting Started

### SQL installation
In order to integrate the RestFull API with a back end SQL database, you need to make sure to "build" it first. 

Download MySQL workbanch in your computer, and run the .sql file inside the repository. That way, you will have all the necessary tables and connections needed to integrate the API with the database.

### .env file

Please create a .env file inside the repository with the following attributes:

SERVER = #your server host name exemple: localhost:3306

USER = #your root

PASSWORD = #password

DB = #if you are using the given SQL script (highly recommended), use "hexadatabase"

These informations were given when you installed and created an environment during the MySQL installation

## Running the code
In order to run the code, open your terminal and write the following command
```
uvicorn main:app --reload
```

## Analyzing the API
If you want to know more about all the requests and how they work, please put a "/docs" following the url given by the terminal's output in your browser.

This way, you will see all possible request that can be used, following the CRUD method

