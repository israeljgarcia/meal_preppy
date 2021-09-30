from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.model):
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
        nullable=False, unique=True
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
