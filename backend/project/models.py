from project.server import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String, nullable=False)
    contact_phone = db.Column(db.String, nullable=False)
    deleted = db.Column(db.Boolean, nullable=False, default=0)

    def __init__(self, contact_name, contact_phone, deleted = 0):
        self.contact_name = contact_name
        self.contact_phone = contact_phone
        self.deleted = deleted
    
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id': self.id,
           'contact_name': self.contact_name,
           'contact_phone': self.contact_phone
       }