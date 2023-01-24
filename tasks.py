from celery import Celery
import time

# Siguiente conectarnos al broker

redis_url = 'redis://default:ZCE2ffxbo5TxinhjxNc9BN0cxrFk9DDc@redis-11111.c281.us-east-1-2.ec2.cloud.redislabs.com:11111'


# Para este ejemplo estamos usando redis como broker y backend result
app = Celery('tasks', broker=redis_url, backend=redis_url)


# ¿Como podemos indicar que es una tarea?
# podemos usar un decorador -> @app.task

# Vamos a simular que nuestra funcion demore 10 segundos

@app.task
def add(x, y):
    # antes del return vamos a darle un stop de 10 segundos
    time.sleep(3)
    return x + y













