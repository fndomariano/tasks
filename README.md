# Tasks

### Install

```bash
docker-compose up -d --build
```

Run migrations
```bash
docker-compose exec app flask db upgrade  
```

## Example requests

### /api/tasks

Obtém informações das tarefas

### Request
```bash
curl --location --request GET 'http://localhost:5000/api/tasks' --header 'Content-Type: application/json'
```

### /api/tasks/add

Adiciona uma nova tarefa

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
	"id": 8
}
```

#### Error Response
```json
{
	"status": "error", 
	"message": "strptime() argument 1 must be str, not None"
}
```

### /api/tasks/edit

Edita uma tarefa

```bash
curl --location --request PUT 'http://localhost:5000/api/tasks' \
	--header 'Content-Type: application/json' \
	--data-raw "{
		'id': 1,
		'title': 'Test Title',
		'description': 'Lorem ipsum'
		'date_begin:' '22/04/1500 10:00:00',
		'date_begin:' '31/12/2020 10:00:00'
	}"
```

### /api/tasks/remove

Remove uma tarefa

```bash
curl --location --request DELETE 'http://localhost:5000/api/tasks' \
	--header 'Content-Type: application/json' \
	--data-raw "{
		'id': 1
	}"
```

## Tests

```bash
docker-compose exec app py.test
```
