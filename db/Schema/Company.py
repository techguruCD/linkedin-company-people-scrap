import mongoengine

class Company(mongoengine.Document):
    linkedin_url = mongoengine.StringField()
    name = mongoengine.StringField()
    about_us = mongoengine.StringField()
    website = mongoengine.StringField()
    headquaters = mongoengine.StringField()
    founded = mongoengine.StringField()
    industry = mongoengine.StringField()
    company_type = mongoengine.StringField()
    company_size = mongoengine.StringField()
    specialties = mongoengine.StringField()
    showcase_pages = mongoengine.ListField()
    affiliated_companies = mongoengine.ListField()