# main imports
from fastapi import FastAPI

'''
    The main page on where both the models will sit. Both models will be pickled prior to model calling. 
    Included in this page will be both working models, and a function to renew the database with updated information. 
    Note: Will need to import current functions made in notebook into their own .py files 

    TODO: 
        * Pickle both machine learning models 
        * Import both models 
'''
# Declaring the Application
f1 = FastAPI()

@f1.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}