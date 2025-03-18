class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def add_person(self, person: "Person") -> None:
        if person.name not in Person.people:
            Person.people[person.name] = person


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        if person.get("wife", None):
            new_person.wife_name = person["wife"]
            result.append(new_person)
        elif person.get("husband", None):
            new_person.husband_name = person["husband"]
            result.append(new_person)
        else:
            result.append(new_person)
        new_person.add_person(new_person)

    for item in result:
        if hasattr(item, "wife_name"):
            for item2 in result:
                if hasattr(item2, "husband_name"):
                    if item.name == item2.husband_name:
                        item.wife = item2
                        item2.husband = item

    return result
