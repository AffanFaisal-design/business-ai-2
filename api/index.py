from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Business AI LIVE"}

# 🚨 THIS NAME MUST BE EXACT
handler = Mangum(app)