from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class List(db.model):
    """
    A class to represent a List table in the SQL database
    Each User can have multiple lists, each List has one User
    ...

    Columns
    -------
    id: int
        A unique identifier for the List
    user_id: int
        The id of the user this List belongs to
    item_name: string
        The name of the item in this List
    quantity: int
        The amount of a certain item in the List

    ...

    Methods
    -------
    """
    __tablename__ = "lists"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade'),
        nullable=False
    )

    item_name = db.Column(
        db.String(25),
        nullable=False
    )

    quanity = db.Column(
        db.Integer,
        nullable=False,
        unique=True
    )
