from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validate_name(self, key, value):
        if value == "":
           raise ValueError("Author must have a name") 
        return value

    @validates('phone_number')
    def validate_phone_number(self, key, value):
        if len(value) != 10:
            raise ValueError("Invalid phone number")    
        return value

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    # All posts have a title.
    # @validates("title")
    # def validate_title(self, key, value):
    #     if value == None:
    #         raise ValueError("requires each post to have a title.")
    #     return value

    # Post content is at least 250 characters long.
        #"Won't Believe""Secret""Top""Guess"
    @validates('content')
    def validate_content(self, key,value):
        if len(value) < 250:
              raise ValueError("Contents must be max of 250 chars")    
        return value   
    
    @validates('summary')
    def validate_summary(self, key,value):
        print("this is the length", len(value))
        print(value)
        if len(value) > 250:
              raise ValueError("Summary cannot be more than 250 chars")    
        return value   

    @validates('category')
    def validate_category(self, key, value):
        if value not in ["Fiction", "Non-Fiction"]:
            raise ValueError("Category must be Fiction or Non-Fiction")
        return value 
    
    @validates("title")
    def validates_title(self, key, value):
        if value not in ["Won't Believ", "Secret","Top [number]"]:
            raise ValueError(" title is not sufficiently clickbait-y.")    
        return value 



    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
