from fastapi import Body, FastAPI

from models import Business
from recommender import recommend

app = FastAPI()

@app.get('/')
def index():
    return f'''
    <p>Hello, World!</p>
    '''

@app.post('/generate_recommendations')
def generate_recommendations(business: Business):
    # Webhook that fires when a user completes the survey.
    res = recommend(business)
    print(res)
    return res
