FROM python:3.11-slim\n\nWORKDIR /app\n\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\n\nCOPY . .\n\nCMD [\
celery\, \-A\, \app.workers.celery\, \worker\, \--loglevel=info\]
