# main imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd 
import joblib
import uvicorn

from api import predictPlace, pointPredict


'''
    The main page on where both the models will sit. Both models will be pickled prior to model calling. 
    Included in this page will be both working models, and a function to renew the database with updated information. 
    Note: Will need to import current functions made in notebook into their own .py files 

    TODO: 
        * Pickle both machine learning models  ** DONE 
        * Import both models into the API 
        * Import the update function 
        * Improve both models
        * Pickle/Import both models 
        * Once happy, use jinja2 to redesign API to liking. 
'''
# Declaring the Application
f1 = FastAPI(
    title='F1 Prediction Project',
    docs_url='/',
)

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