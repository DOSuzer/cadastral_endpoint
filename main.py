import random

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from time import sleep

app = FastAPI()


@app.get("/data")
async def root():
    sleep(random.randint(0, 60))
    return JSONResponse(
        content=jsonable_encoder({'result': random.choice([True, False])})
    )
