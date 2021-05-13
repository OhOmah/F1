import joblib
import logging
import pandas as pd 
import category_encoders as ce

from api.externalFunctions import quick_decode
from fastapi import APIRouter
from pydantic import BaseModel, Field

'''
    This contains both functions that import and call each model to return 
    the prediction 
'''

# Setting up the router 
router = APIRouter()

# Assigning the values that the model is going to use to predict with
class Item(BaseModel):
    ''' 
        This class contains what the models takes in for consideration.
        The class will include example values in case the user does not 
        want to fill in the data. Will allow the model to run without user
        input.
    '''
    year: int = Field(...,example=2021)
    session: int = Field(...,example=1)
    firstName: str = Field(...,example="Lewis")
    lastName: str = Field(...,example="Hamilton")
    constructor: str = Field(...,example="Mercedes")
    fastestTime: str = Field(...,example="1:07.342")
    fastestLap: str = Field(...,example="66")
    fastestLapAvgSpeedKPH: str = Field(...,example="222")
    status: str = Field(...,example="Finished")
    timeBehind: str = Field(..., example="1:20:05.154")
    q1Time: str = Field(...,example="1:04.432")
    q2Time: str = Field(...,example="1:04.422")
    q3Time: str = Field(...,example="1:03.809")
    track: str = Field(...,example="imola")
    points: int = Field(...,example=10)
    wins: int = Field(...,example=1)

@router.post('/predictPoints')
def predictPoints(user_input: Item):

    '''
        The function will return the predicted place of the 
        driver based on their stats. This will take in the user input and 
        run the model based on what user has said. Will always return an int. 

        TODO: 
        * Return the formatted prediction  
    '''
    # Declaring my encoder the encode the user input into 
    # values that the model will like. 
    encoder = ce.OrdinalEncoder()

    # Converting the user input into a dict
    ui_dict = user_input.dict()

    # Taking the user input (which will be turned into a dict) and transforming
    # the data into a dataframe, which the encoder and model will predict on. 
    column_list = ["Year", "Round", "First_Name", "Last_Name", "Track", "Points",
                 "Wins", "Q1_Time", "Q2_Time", "Q3_Time"]
    predictPlace_df = pd.DataFrame(columns=column_list)
    predictPlace_df = predictPlace_df.append(ui_dict, ignore_index=True)

    # Encoding the user input 
    predictPlace_encode = encoder.fit_transform(predictPlace_df)

    # Loading in the pickled model 
    model = joblib.load("../Notebooks/models/modelPoints.sav")

    # Now applying the model to the dataframe to see the result. 
    placePred = model.predict(predictPlace_encode)
    
    # Decodes prediction to one of the 3 outcomes. 
    final = quick_decode(placePred)
    
    # TODO: Format the final outcome. 
    return "{fName} {lName} is likely to finish in {pred}".format(fName=user_input.firstName,
                                                                    lName=user_input.lastName,
                                                                    pred=final)