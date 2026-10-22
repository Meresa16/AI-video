from fastapi import FastAPI\n\napp = FastAPI(title=\
AI
Video
Studio
API\, version=\1.0.0\)\n\n@app.get(\/\)\ndef root():\n    return {\message\: \AI
Video
Studio
API\}\n\n@app.get(\/health\)\ndef health():\n    return {\status\: \ok\}\n
