from fastapi import FastAPI, Request

from sentient import sentient
from model import prediction
from data import rsi, call



app = FastAPI()


@app.get("/")
async def blank():
    return {"x":"hello"}

# Define a route for accepting input data and returning predictions
@app.post('/predict')
async def make_prediction(request: Request):
    symbol = await request.json()
    return prediction(symbol["symbol"])

@app.post('/sentient')
async def make_sentient(request: Request):
    symbol = await request.json()
    vals = sentient(symbol["symbol"])
    return vals

@app.post('/rsi')
async def get_rsi(request: Request):
    symbol = await request.json()
    output = rsi(symbol["symbol"])
    return output

@app.post('/data')
async def get_data(request: Request):
    symbol = await request.json()
    #print(symbol["symbol"])
    return call(symbol["symbol"])