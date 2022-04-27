import re
import pickle
from dataclasses import dataclass, field
from typing import Counter, Dict, List
from math import log


split_pattern = re.compile(r'\W+')
def get_terms(s: str) -> List[str]:
    terms = re.split(split_pattern, s.lower())
    return [term for term in terms if term]


@dataclass
class FreshApp:
    app_id: str
    name: str
    safe_name: str

    rating: int
    reviews: int
    # downloads: int
    
    about: str
    description: str
    icon: str

    categories: List[str]
    features: List[str]
    keywords: List[str]

    terms: List[str] = field(init=False)
    freq: Dict[str, int] = field(init=False)

    def __post_init__(self):
        # list_terms = [
        #     ' '.join(self.categories or []),
        #     ' '.join(self.features or []),
        #     ' '.join(self.keywords or []),
        # ]

        about_terms = get_terms(self.about)
        desc_terms = get_terms(self.description)

        self.freq = (
            Counter(about_terms) +
            Counter(desc_terms)
        )

        self.terms = about_terms + desc_terms


with open('data/data.pickle', 'rb') as file:
    data = pickle.load(file)
    apps = [FreshApp(**app) for app in data]
    N = len(apps)


def find_relevant_apps(business_description: str):
    from collections import defaultdict

    terms = get_terms(business_description)
    weights = defaultdict(list)

    for term in terms:
        term_freq = sum((term in app.terms) for app in apps)
        idf = log(N / term_freq) if term_freq else 0

        for app in apps:
            tf = log(1 + app.freq[term])
            tf_idf = tf * idf
            weights[app.app_id].append(tf_idf)

    def key(app: FreshApp):
        return sum(weights[app.app_id])

    return sorted(apps, key=key, reverse=True), weights


if __name__ == '__main__':
    rel, weights = find_relevant_apps(input())
    print(list(zip(rel, weights)))
    raise
    for app in rel[:10]:
        print('=' * 50)
        print(app.name, f'https://appstore.freshbooks.com/details/{app.safe_name}')
        print(app.about)
        print(weights[app.app_id])
