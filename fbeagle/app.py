from freshbooks import Client

import os
from pprint import pprint

os.environ['FRESHBOOKS_AUTH_URL'] = 'https://auth.staging.freshenv.com'
os.environ['FRESHBOOKS_API_URL'] = 'https://api.staging.freshenv.com'

client = Client(
    client_id='3fc104f952681ef915179ab66e5e2ce007bbc1f9d3de5d3fb1e7f7345f3cd4ad',
    client_secret='c31175e4ef96f4b19a3f4da9d14f538b1f558994cd3c21ba2ecc5fa0722da40d',
    redirect_uri='http://localhost:6463/',
)

scopes = ['user:profile:read']

# auth_url = client.get_auth_request_url([
#     'user:profile:read',
# ])
# code = input(auth_url + '\n')
# auth_results = client.get_access_token(code)
# print(auth_results)
# print('Authenticated.')

# user = client.current_user()
# pprint(user.business_memberships)
# print('=' * 20)
# pprint(user.data)

sample_user = dict(
    industry='development',
    business_description='we make programs',
    team_size='asdf'
)


