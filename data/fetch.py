import os
import pickle
import requests
import re
from typing import List, Dict

OPENCHANNEL_API_URL = 'https://market.openchannel.io/v2/apps'
DESIRED_FIELDS = dict(
    app_id='appId',
    name='name',
    safe_name='safeName[0]',
    rating='rating',
    reviews='reviewCount',
    # downloads='statistics.downloads.total',
    about='customData.aboutTheApp',
    description='customData.description',
    categories='customData.categories',
    features='customData.keyFeatures',
    keywords='customData.searchKeywords',
)

auth = (
    os.environ['OPENCHANNEL_MARKETPLACE_ID'],
    os.environ['OPENCHANNEL_SECRET'],
)


def normalize_value(obj: any):
    if isinstance(obj, list):
        print(111, obj)
        return ','.join(obj)
    return obj


item_access_pattern = re.compile(r'^(.+)\[(\d+)\]$')
def itemgetter_recursive(
    field_branches: Dict[str, str],
    ignore_missing=True
):
    def get_item(obj: any, field_branch: List[str]):
        field, *rest = field_branch
        try:
            target = None

            item_accesses = re.findall(item_access_pattern, field)
            if item_accesses:
                field, key = item_accesses[0]
                try:
                    target = obj[field][int(key)]
                except ValueError:
                    target = obj[field][key]
            else:
                target = obj[field]

            if rest: return get_item(target, rest)
            return target
        except KeyError:
            if not ignore_missing: raise

    return lambda obj: {
        key : get_item(obj, field_branch.split('.'))
        for key, field_branch in field_branches.items()
    }


resolve_desired_fields = itemgetter_recursive(DESIRED_FIELDS)

# Where the processed app listings will be stored.
apps = list()

page = 1
total_pages = 100
while page < total_pages:
    params = dict(
        query='{"status.value":"approved"}', # requests encodes for us
        pageNumber=page,
    )
    res = requests.get(OPENCHANNEL_API_URL, auth=auth, params=params)
    data = res.json()

    for app in data['list']:
        try:
            apps.append(resolve_desired_fields(app))
        except Exception as e:
            print(app, e)
            raise

    page += 1
    total_pages = data['pages']


with open('data/data.pickle', 'wb') as file:
    pickle.dump(apps, file)
