import os
import sys
from fastapi import FastAPI, Request, Depends
from pydantic import BaseModel
import models
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import product
import math




app=FastAPI()

models.Base.metadata.create_all(bind=engine)

class productdesc(BaseModel):
    id: int
    product_name: str
    product_price: int

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()

@app.get('/')
def index():
    return "hello"
    # pass


@app.get('/products/{product_name}')
def get_product(product_name: str,Tenure:int,Percentage: int, db: Session = Depends(get_db)):
    db=SessionLocal()

    stock= db.query(product.product_price).filter(product.product_name == product_name).first()
    P=int(stock[0])
    R=Percentage/(12*100)
    N=Tenure
    emi=(math.pow((1 + R), N)/(math.pow((1 + R),(N))-1))
    return emi*P*R


