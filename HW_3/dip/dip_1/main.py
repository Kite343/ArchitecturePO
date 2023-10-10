from recearch import Research
from relatinships import Relationships
from person import Person

if __name__ == '__main__':
    person_1 = Person('Alex')
    relationships = Relationships()
    relationships.add_parent_and_child(person_1, Person('Olga'))
    relationships.add_parent_and_child(person_1, Person('Max'))
    
    Research(relationships, person_1.name)


