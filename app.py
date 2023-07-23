from flask import Flask
import sys
from housing_1.logger import logging 
from housing_1.exception import HousingException


app= Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():
    try :
        raise Exception ('We testing custom exception ')
    except Exception as e:
        raise HousingException(e,sys) from e
    logging.info(housing.error_message)

    logging.info("we are testing logging module")
    return "starting my first machine learning project"

if __name__ == "__main__":
    app.run(debug=True)
