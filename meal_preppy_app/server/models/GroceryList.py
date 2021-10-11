from models.Shared import db


class GroceryList(db.Model):
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
    __tablename__ = "grocerylists"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade'),
        nullable=False
    )

    ingredients = db.relationship("GroceryIngredient", backref="GroceryList")
