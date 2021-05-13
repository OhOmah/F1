# main imports
from fastapi import FastAPI
import gunicorn

import pandas as pd 
import joblib
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
f1 = FastAPI()

f1.include_router(predictPlace.router)
f1.include_router(pointPredict.router)