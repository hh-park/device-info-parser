# device-info-parser
> I couldn't implement the pagination in time, but I hope to have chance to dig into it and implement it in the future.

## Summary
### The flow would be like:
  1. JSON data in *device.json* would be in the body of the http request.
  2. The request URLs by functions and examples of request format are like below:
        - Inserting records to db/updating db : '/db' ('POST' method)
        ```
        {
          "json_data" : {
            "c44dt2ecie6h7m4li3cg": {
              "id": "c44dt2ecie6h7m4li3cg",
              "type": "awair-glow",
              "coordinates": [
                55.5136433,
                25.4052165
              ],
              "status": "connected",
              "timezone": "Asia/Dubai"
            },
            "c44dt2ecie6h7m4li3d0": {
              "id": "c44dt2ecie6h7m4li3d0",
              "type": "awair-element",
              "coordinates": [
                54.37,
                24.47
              ],
              "status": "connected",
              "timezone": "Asia/Dubai"
            }, ...
          }
        }
        ```
        - Select from db by id : '/id' ('GET' method)
        ```
        {
          "id" : "c44dt2ecie6h7m4li3cg"
        }
        ```
        - Select form db by type : '/type' ('GET' method)
        ```
        {
          "type" : "awair-glow"
        }
        ```
        - Select from db by status : '/status' ('GET' method)
        ```
        {
          "status" : "connected"
        }
        ```
        - Select all(view whole lists) from db : '/db' ('GET' method)
        
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
3. After executing **ClientService.py** with the command `python ClientService.py` in cmd, api service can be reached via **localhost(127.0.0.1):5000/[uri]**.

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
