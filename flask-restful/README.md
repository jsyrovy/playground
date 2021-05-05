# flask-restful-demo

## Example usage


Get the list

```bash
curl http://localhost:5000/todos
```

Get a single task

```bash
curl http://localhost:5000/todos/todo3
```

Delete a task

```bash
curl http://localhost:5000/todos/todo2 -X DELETE -v
```

Add a new task

```bash
curl http://localhost:5000/todos -d "task=something new" -X POST -v
```

Update a task

```bash
curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v
```
