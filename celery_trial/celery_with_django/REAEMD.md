
## quick start


```
python manage.py runserver
## from another terminal
celery -A CELERY worker --loglevel=INFO

```
### run worker for specific queues
```

celery -A config worker --loglevel=INFO -c 1 -Q long,short
#複数ワーカーを動かしたいとき↓
celery multi start -A config node1 node2 -c:1 1 -Q:1 long -c:2 5 -Q:2 short

```


## settings
