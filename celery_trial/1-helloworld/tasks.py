from celery import Celery

#認証情報@hostを書く
app=Celery("tasks",broker="amqp://user:password@localhost:5672/")


app.conf.task_routes = {
    "tasks.multdir": {"queue": "mult"},
}
app.conf.task_default_queue = "default"


@app.task
def add(x,y):
    print("desktop application")
    print("waaaaaaaaaaaaaaaaaa")
    return x+y

@app.task
def mult(x,y):
    print(x*y)
    return x*y


@app.task
def minus(x,y):
    print("desktop application")
    print("waaaaaaaaaaaaaaaaaa")
    return x+y
