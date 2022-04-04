from typing import Literal
from pydantic import BaseModel

Industry = Literal[
    'Accounting and Finance',
    'Administration',
    'Agriculture',
    'Architecture',
    'Arts and Entertainment',
    'Automotive and Transport',
    'Construction and Trades',
    'Creative Professionals',
    'Development & Programming',
    'Education',
    'Engineering',
    'Environment',
    'Event Planning',
    'Fashion and Beauty',
    'Food Services',
    'Health and Wellness',
    'Hospitality, Travel and Tourism',
    'Human Resources and Staffing',
    'Information Technology and Support',
    'Legal',
    'Management Consulting',
    'Marketing, Communications & Media',
    'Non-Profit and Volunteer Management',
    'Print Management',
    'Project Management',
    'Real Estate and Property Management',
    'Retail',
    'Sales and Business Development',
    'Telecommunications',
    'Web Hosting',
    'Other',
]

class Business(BaseModel):
    name: str
    business_description: str
    industry: Industry
