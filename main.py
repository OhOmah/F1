# main imports
from fastapi import FastAPI, Request

from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates


import pandas as pd 
import joblib
import uvicorn

from api import predictPlace, pointPredict


'''
    The main page on where both the models will sit. Both models will be pickled prior to model calling. 
    Included in this page will be both working models, and a function to renew the database with updated information. 
    Note: Will need to import current functions made in notebook into their own .py files 

    TODO: 
        * Once happy, use jinja2 to redesign API to liking. 
        * Update the training the data. 
        * Update the Model to deliver more accurate results 
'''
# Declaring the Application
f1 = FastAPI(
    title='F1 Prediction Project',
    docs_url='/',
)
templates = Jinja2Templates(directory="templates/")

f1.include_router(predictPlace.router)
f1.include_router(pointPredict.router)

f1.add_middleware(
    CORSMiddleware,
    allow_origin_regex='https?://.*',
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


if __name__ == '__main__':
    uvicorn.run(f1)