from typing import List


class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: str
    subjects: List[str]
    hobbies: List[str]
    picture: str
    address: str

    def __init__(self, first_name, last_name, email, gender, phone_number, date_of_birth, subjects, hobbies, picture,
                 address):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.subjects = subjects
        self.hobbies = hobbies
        self.picture = picture
        self.address = address
