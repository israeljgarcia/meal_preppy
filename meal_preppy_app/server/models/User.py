from models.Shared import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


class User(db.Model):
    """
    A class to represent a User table in the SQL database

    ...

    Columns
    -------
    id: int
        A unique identifier for the User
    first_name: string
        --------------
    last_name: string
        --------------
    username: string
        The display name for the user
    email: string(email)
        The User's email address for authentication
    password: string(hashed)
        The User's login password, hashed to protect data

    ...

    Methods
    -------

    signup(cls, first_name, last_name, username, email, password):
        creates new user on the database
        returns new user

    authenticate(cls, username, password):
        checks user's private credentials
        returns User() or False
    """
    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    first_name = db.Column(
        db.String(12),
        nullable=False
    )

    last_name = db.Column(
        db.String(12),
        nullable=False
    )

    username = db.Column(
        db.String(16),
        nullable=False,
        unique=True
    )

    email = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.Text,
        nullable=False
    )

    pantry = db.relationship("Pantry", backref="users")

    # Classmethods
    # ------------
    @classmethod
    def signup(cls, first_name, last_name, username, email, password):
        """Creates a new User on the database

        Args:
            first_name (string): first name
            last_name (string): user last name 
            username (string): user screen name
            email (string): user's email
            password (string): user's hashed password

        Returns:
            User()
        """

        hashed_pass = bcrypt.generate_password_hash(password).decode('UTF-8')
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=hashed_pass
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Finds a User with `username` and `password`

        Args:
            username (string): user's username
            password (string): user's password

        Returns:
            if True: User()
            if False: Boolean
        """
        user = cls.query.filter_by(username=username).first()

        if user:
            user_is_auth = bcrypt.check_password_hash(user.password, password)
            if user_is_auth:
                return user

        return False

    # Instance methods
    # ----------------
    def getPantryIngredients(self):
        """Querys the ingredients in the user's pantry

        Returns:
            ingredients[list]: a list of ingredients that belong to the user 
        """
        ingredients = self.pantry[0].ingredients

        return ingredients

    def to_dict(self):
        """Turns the user's id, first_name, last_name, username, email into a dictionary

        Returns:
            dict: a dict containing the users id, name, email, and username
        """
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "username": self.username,
            "email": self.email
        }
