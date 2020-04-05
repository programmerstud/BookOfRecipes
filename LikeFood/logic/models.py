from flask_login import UserMixin

from logic import db, manager, ma

user_like_recipe = db.Table('user_like_recipe',
                 db.Column('recipe_id', db.Integer, db.ForeignKey('recipe.id'), primary_key=True),
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
                 )


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
        nullable=False)
    image = db.Column(db.String(255), nullable=False, unique=True)
    recipe_text = db.Column(db.String(1024), nullable=False, unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    recipes = db.relationship('Recipe', backref='user', lazy=True)
    user_like_recipe = db.relationship('Recipe', secondary=user_like_recipe, lazy='subquery',
        backref=db.backref('User', lazy=True))

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False, unique=True)
    recipes = db.relationship('Recipe', backref='category', lazy=True)

@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True

user_schema = UserSchema(many = True)

class RecipeSchema(ma.ModelSchema):
    class Meta:
        model = Recipe
        include_relationships = True
        load_instance = True

recipe_schema = RecipeSchema(many = True)

class CategorySchema(ma.ModelSchema):
    class Meta:
        model = Category
        include_relationships = True
        load_instance = True

category_schema = CategorySchema(many = True)