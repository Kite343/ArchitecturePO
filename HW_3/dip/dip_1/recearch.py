from relatinship_browser import RelationshipBrowser
from relatinship import Relationship

class Research:
    def __init__(self, browser: RelationshipBrowser, name) -> None:
        for p in browser.find_all_children_of(name):
            print(p)