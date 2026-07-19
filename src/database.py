import json
import os


class Database:
    def __init__(self, filename="students.json"):
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump([], file, indent=4)

    def load_students(self):
        with open(self.filename, "r") as file:
            return json.load(file)

    def save_students(self, students):
        with open(self.filename, "w") as file:
            json.dump(students, file, indent=4)