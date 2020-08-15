class personal_information():
    def __init__(self):
        self.full_name = "Your Full Name" #TODO maybe distill into individual names
        self.age = "Your Age"
        self.contact_numbers = [ "Your Mobile", "Home Phone "]
        self.email = "example.email@notarealemail.com"
        self.address = "Your Address"
        self.photo_path = None

class work_experience():
    def __init__(self, job_title: str):
        self.job_title = job_title
        self.start_date = None
        self.end_date = None
        self.responsibilities = []
        self.additional_information = None

class responsibility():
    def __init__(self):
        self.short_description = "Lorem ipsum dolor sit amet"
        self.detailed_description = "Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet"
