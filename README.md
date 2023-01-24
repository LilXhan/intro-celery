# CELERY EN PYTHON

Step One:

```bash
pip install celery
pip install redis
pip install ipython
```

Iniciate celery:
```bash
celery -A tasks worker -l info
```

use in python function add(x, y)
```python
add.delay(5, 6)
```

Monitoring tasks

```shell
pip install flower
celery -A tasks flower --port=5555
```

