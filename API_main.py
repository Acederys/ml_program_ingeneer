from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str
app = FastAPI()
classifier = pipeline('translation','Helsinki-NLP/opus-mt-en-ru')
@app.get('/')
async def root():
    return {'message':'Helloworld'}
@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]