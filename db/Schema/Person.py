import mongoengine

class Person(mongoengine.Document):
    linkedin_url = mongoengine.StringField()
    name = mongoengine.StringField()
    about = mongoengine.ListField()
    experiences = mongoengine.ListField(),
    educations = mongoengine.ListField(),
    interests = mongoengine.ListField()
    accomplishments = mongoengine.ListField()
    also_viewed_urls = mongoengine.ListField()
    contacts = mongoengine.ListField()
    company = mongoengine.StringField()
    job_title = mongoengine.StringField()