from models.Shared import db


class Pantry(db.Model):
    """
    A class to represent a Pantry table in the SQL database
    Each User can only have one pantry
    A pantry points to an ingredients list
    ...

    Columns
    -------
    id: int
        A unique identifier for the Pantry
    user_id: int
        The id of the user this Pantry belongs to

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

    ingredients = db.relationship("PantryIngredient", backref="pantrys")

    @classmethod
    def createPantry(cls, user_id):
        """Creates a new Pantry on the database

        Args:
            user_id(int): the user that this pantry belongs to
            ingredients_id(int): The id to the ingredients list

        Returns:
            Pantry(Object)
        """
        pantry = Pantry(
            user_id=user_id
        )

        db.session.add(pantry)
        return pantry
