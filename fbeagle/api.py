from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .recommender import find_relevant_apps

app = FastAPI()

@app.get('/find')
def generate_recommendations(desc: str):
    # Webhook that fires when a user completes the survey.
    rel, weights = find_relevant_apps(desc)
    return [app.__dict__ for app in rel[:10]]

app.mount('/', StaticFiles(directory='public', html=True), name='public')
