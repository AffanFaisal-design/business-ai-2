from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from mangum import Mangum

app = FastAPI()

@app.get("/")
def home():
    return HTMLResponse("<h1>Business AI is LIVE 🚀</h1>")

# 🔑 THIS IS THE KEY LINE
handler = Mangum(app)