from myapp import mongo
from datetime import datetime


class Comment(mongo.EmbeddedDocument):
    name=mongo.StringField(required=True)
    text=mongo.StringField(required=True)
    date=mongo.DateTimeField(default=datetime.now())

    def to_json(self):
        json_c={
            #'id':self.id,
            'name':self.comment,
            'text':self.text,
            'date':self.date
        }
        return json_c

    def __str__(self):
        return f"<Comment> {self.name}"


class Role(mongo.Document):
    name=mongo.StringField(max_lenght=64, required=True, unique=True)
    description=mongo.StringField()

    def __str__(self):
        return f"<Role> {self.name}"


class User(mongo.Document):
    username=mongo.StringField(required=True)
    password=mongo.StringField()
    roles=mongo.ListField(mongo.ReferenceField(Role))

    def to_json(self):
        json_u={
            #'id':self.id,
            'username':self.username,
            'roles':self.roles
        }
        return json_u

    @staticmethod
    def from_json(json_user):
        username=json_user.get('username')
        if username is None or username=='':
            raise ValidationError('Username blank')
        return User(username=username)

    def __str__(self):
        return f"<User> {self.username}"


class Post(mongo.Document):
    title=mongo.StringField(required=True)
    text=mongo.StringField()
    publish_date=mongo.DateTimeField(default=datetime.now())
    user=mongo.ReferenceField(User)
    comments=mongo.ListField(mongo.EmbeddedDocumentField(Comment))
    tags=mongo.ListField(mongo.StringField())

    def to_json(self):
        json_p={
            #'id':self.id,
            'name':self.title,
            'text':self.text,
            'publish':self.publish_date,
            'user':self.user,#.username,
            'comments':self.comments,
            'tags':self.tags
        }
        return json_p

    @staticmethod
    def from_json(json_post):
        title=json_post.get('title')
        text=json_post.get('text')
        if title is None or title=='':
            raise ValidationError('title blank')
        return Post(title=title, text=text) 


    def __str__(self):
        return f"<Post> {self.title}"
