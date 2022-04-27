# fbeagle

Hunt down apps to improve your FreshBooks experience.

## Setup

1. Set up a virtual environment, enter it, and install the required dependencies.
    - `python -m venv venv` (Replace `python` with the name for your python3 executable)
    - `source venv/bin/activate`
    - `pip install -r requirements.txt`
2. Rename `.env.example` to `.env` and populate the fields accordingly.
3. Run `source setenv.sh` to load the values in the current shell environment.
    - Alternatively, refactor the program to use `dotenv`.
4. Run `python data/fetch.py` to populate the dataset. A file called `data/data.pickle` should appear.
5. Run the FastAPI server with `python -m uvicorn fbeagle.api:app --reload`.

## Devlog

- Realized that `business_description` did not mean what I thought it meant. Only apparent usable survey metric is `industry` now.
- Industry responose from FB API identity call seems to be blank even if specified in the survey, so OAuth app seems unbeneficial now.
- App now functions as a standalone page that asks users to describe their business and gives app recommendations based on this.

## Future

- Add "description of business" as a field into the survey, so this project can be automatically integrated into the onboarding process.
- App analytics
    - How much are businesses using a particular app? Why did they uninstall it? How long did they end up using it for?
    - which industries prefer which apps? i.e. correlation between various aspects of a business and which apps they use the most
    - Obtain quantifiable metrics for what determines a "good recommendation"

## References

- https://2ndsiteinc.atlassian.net/wiki/spaces/G/pages/2456322223/New+Survey+data+flow
- https://2ndsiteinc.atlassian.net/wiki/spaces/G/pages/2290810899/Survey+Fields+Mapping
- https://2ndsiteinc.atlassian.net/wiki/spaces/G/pages/2493055116/Detecting+Survey+Completion+Issues
- https://github.com/freshbooks/masterlock/blob/main/app/models/business_survey_result.rb
- https://www.freshbooks.com/api/me_endpoint
