from datetime import datetime as dt
import requests as re
def detc_season():
    curr_date=dt.now()
    month=curr_date.month 
    if month in [6,7]:
        season='Kharif season'
    elif month in [10,11,12]:
        season='Rabi season'
    elif month in [3,4,5]:
        season='Zaid season'        
    else:
        season='''Sowing is not advisable during this season, as climatic conditions may change in the coming days. If you still plan to sow, please carefully check the current weather conditions and proceed only after ensuring suitability.Which the data of current weather conditions shown below '''
    return season