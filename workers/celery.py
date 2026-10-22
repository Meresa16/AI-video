from celery import Celery\n\ncelery_app = Celery(\n    \
ai_video_studio\,\n    broker=\redis://redis:6379/0\,\n    backend=\redis://redis:6379/0\\n)\n\ncelery_app.autodiscover_tasks([\app.workers\])\n
