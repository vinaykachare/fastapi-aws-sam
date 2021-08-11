from fastapi import FastAPI
from mangum import Mangum
from .config import Settings

app = FastAPI()
setting = Settings()

@app.get("/hello")
async def root():
    # return {"message": "hell"}

    return {"message": f"Hello World {setting.env}"}

handler = Mangum(app)