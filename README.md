# Tasks

This repository is an API that can be used to register tasks. It one is very simple and I've made to learn Flask.

### Install

a) Configure environment file

```bash
cp .env-sample .env
```

b) Up the docker containers

```bash
docker-compose up -d --build
```

c)  Run migrations

```bash
docker-compose exec app flask db upgrade  
```

## Example requests

Bellow, there are some examples of requests and their responses.

> ### /api/tasks

It gets a list of tasks

#### Request
```bash
curl --location --request GET 'http://localhost:5000/api/tasks' --header 'Content-Type: application/json'
```

#### Successful Response

```json
{
  "data": [
    {
      "id": 9,
      "title": "Test Title 2",
      "date_begin": "2020-02-03T08:00:00",
      "date_until": "2020-02-03T18:00:00",
      "description": "Lorem Ipsum 2"
    },
    {
      "id": 10,
      "title": "Test Title",
      "date_begin": "2020-02-02T08:00:00",
      "date_until": "2020-02-02T18:00:00",
      "description": "Lorem Ipsum"
    },
    {
      "id": 11,
      "title": "Test Title",
      "date_begin": "2020-02-02T08:00:00",
      "date_until": "2020-02-02T18:00:00",
      "description": "Lorem Ipsum"
    },
    {
      "id": 12,
      "title": "Test Title",
      "date_begin": "2020-02-02T08:00:00",
      "date_until": "2020-02-02T18:00:00",
      "description": "Lorem Ipsum"
    }
  ]
}
```

> ### /api/tasks/add

It adds a task

#### Request
```bash
curl --location --request POST 'http://localhost:5000/api/tasks/add' \
	--header 'Content-Type: application/json' \
	--data-raw '{
		"title": "Test Title",
		"description": "Lorem ipsum",
		"date_begin": "22/04/1500 10:00:00",
		"date_until": "31/12/2020 10:00:00"
	}'
```

#### Successful Response
```json
{
	"status": "success",
	"message": "Task added successfully"
}
```

#### Example of an error response
```json
{
	"status": "error", 
	"message": "strptime() argument 1 must be str, not None"
}
```

> ### /api/tasks/edit

It edits a task

```bash
curl --location --request PUT 'http://localhost:5000/api/tasks/edit/11' \
	--header 'Content-Type: application/json' \
	--data-raw '{
		"title": "Test Title 2",
		"description": "Lorem ipsum 2",
		"date_begin": "19/05/2020 10:00:00",
		"date_until": "19/05/2020 18:00:00"
	}'
```

#### Successful Response
```json
{
	"status": "success",
	"message": "Task edited successfully"
}
```

#### Example of an error response
```json
{
	"status": "error", 
	"message": "400 Bad Request: Failed to decode JSON object: Expecting property name enclosed in double quotes: line 2 column 3 (char 4)"
}
```

> ### /api/tasks/remove

It removes a task

```bash
curl --location --request DELETE 'http://localhost:5000/api/tasks/remove/10' --header 'Content-Type: application/json'	
```

#### Successful Response
```json
{
	"status": "success",
	"message": "Task removed successfully"
}
```

#### Example of an error response
```json
{
	"status": "error", 
	"message": "'scoped_session' object has no attribute 'flus'"
}
```


> ### /api/tasks/show

It shows details about a task

```bash
curl --location --request GET 'http://localhost:5000/api/tasks/show/10' --header 'Content-Type: application/json'	
```

#### Successful Response
```json
{
	"data": {
		"id": 9, 
		"title": "Test Title 2", 
		"description": "Lorem Ipsum 2", 
		"date_begin": "2020-02-03T08:00:00", 
		"date_until": "2020-02-03T18:00:00"
	}
}
```

#### Example of an error response
```json
{
	"status": "error",
	"message": "'NoneType' object has no attribute 'id'"
}
```

## Tests

```bash
docker-compose exec app py.test
```