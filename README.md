# device-info-parser
> Before jumping into the project description, I apologize for the delay of submission due to participation to team and company dinners.


## Summary
### The flow would be like:
  1. JSON data in *device.json* would be in the body of the http request.
  2. The request URLs by functions are mapped like below:
        - Inserting records to db/updating db : ['/db']
        - Select from db by id : ['/id']
        - Select form db by type : ['/type']
        - Select from db by status : ['/status']
        - Select all(view whole lists) from db : ['/all']
        
  3. Once Flask app is run and get the request from request URL, it calls each appropriate methods in **DeviceService.py** for DB handling.
  4. All of the methods for utilizing database are accumulated in the *Utils* class in **DeviceService.py**.
  5. *DeviceHandler* class in **DeviceService.py** inherits from *Utils* class for using the db connection methods.
  6. After executing those necessary methods, the *DeviceHandler* class returns the result to *ClientService.py'*.
  7. *ClientService* returns the result in dict format.
  
## Environment settings
### Application setting
1. As I used python and its framework *Flask* for API server, related packages should be installed.
    ```
    pip install flask
    pip install falsk-restx
    ```
2. To deal with Json format data, install json package: `pip install json`
3. After executing **ClientService.py** with the command `python ClientService.py` in cmd, api service can be reached via **localhost(127.0.0.1):80/[uri]**.

### DB setting
1. Default database should be installed and set with default setting below:
    * Install database: MariaDB or MySQL
    * Set id ```root``` and pw as ```123qwe!!!```
    * Create database like ```create database test;```
    
2. Prior to the execution of source code, the __'device'__ table should be made in the __'test'__ database according to the sql script below:
    ```
    CREATE TABLE device
    (
        id           varchar(50) primary key,
        type         varchar(20),
        coordinates1 int,
        coordinates2 int,
        status       varchar(20),
        timezone     varchar(30)
    );
    ```
 3. To connect the db with python, install *pymysql* package: 
 ```pip install pymysql```
