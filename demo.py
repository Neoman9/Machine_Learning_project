from housing_1.Pipeline.pipeline import pipeline
from housing_1.exception import HousingException
from housing_1.logger import logging
def main():
    try:
        pipeline = pipeline
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()