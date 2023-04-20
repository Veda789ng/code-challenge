# Weather API
You can retrieve weather information for many places and years using this API. By date and place, the data can be filtered. Additionally, the API offers statistical statistics on the weather data.

## Features
- Retrieve weather information for a specified date and area.
- Retrieve statistics data about the weather, such as the maximum, minimum, and overall precipitation for a certain day and place.

## These are the respective API endpoints :

    /weather - retrieves weather data
    /weather/stats - provides statistics about the data
    /apidocs - provides documentation using openapi

# Environment_setup
```base
python3 -m venv venv
source venv/bin/activate
```
# Installation

>Install the required packages:
```base
pip3 install -r requirements.txt
```

## Usage

- Run the following command to create the database and populate it with data:

```bash
python3 -m flask create
```

- Start the API server
```bash
 python3 -m flask run
```
- The API can now be accessed at http://127.0.0.1:5000.

# Endpoints

## **Swagger**
[http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)

##### Weather data
```
GET /weather/
```
This endpoint returns a paginated list of weather records. You can filter the results by date and station using query parameters:

##### Statistics
```
GET /weather/stats/

```
This endpoint returns statistical information about the weather data. You can filter the results by date and station using query parameters, in the same way as the /api/weather/ endpoint.


# Testing

## Run the tests

```bash
pytest -v
```