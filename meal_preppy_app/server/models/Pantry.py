from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pantry(db.model):
    """
    A class to represent a Pantry table in the SQL database
    Each User can only have one pantry
    ...

    Columns
    -------
    id: int
        A unique identifier for the Pantry
    user_id: int
        The id of the user this Pantry belongs to
    item_name: string
        The name of the item in this Pantry
    quantity: int
        The amount of a certain item in the Pantry

    ...

    Methods
    -------
    """
    __tablename__ = "pantrys"

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
