from models.Shared import db


class PantryIngredient(db.Model):
    """
    Ingredients table that holds ingredient names and quantities

    ...

    Columns
    -------
    id: int
        A unique identifier for the Ingredients

    pantry_id: int
        The pantry this list belongs to

    ingedient_name: string
        The name of the ingredient

    quantity: int
        the amount of ingredient

    unit: string
        the unit of measurement for the ingredient

    ...

    Methods

    """
    __tablename__ = "pantryingredients"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    pantry_id = db.Column(
        db.Integer,
        db.ForeignKey('pantrys.id', ondelete='cascade'),
        nullable=False
    )

    ingredient_name = db.Column(
        db.String(25),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    unit = db.Column(
        db.String(8),
        nullable=False
    )

    @classmethod
    def create_ingredient(cls, pantry_id, ingredient_name, quantity, unit):
        """Creates an ingredient in the user's pantry

        Args:
            pantry_id (int): id for the pantry
            ingredient_name (string): the name of the ingredient
            quantity (int): amount of ingredient
            unit (string): unit of measurement of ingredient

        Returns:
            PantryIngredient(obj)
        """

        ingredient = PantryIngredient(
            pantry_id=pantry_id,
            ingredient_name=ingredient_name,
            quantity=quantity,
            unit=unit
        )

        db.session.add(ingredient)
        return ingredient

    # Instance Methods
    # ----------------
    def update_ingredient(self, ingredient_name=-1, quantity=-1, unit=-1):
        """Edits the properties of an ingredient

        Args:
            id (int): identifier
            ingredient_name (string): name of the ingredient
            quantity (float): amount of item
            unit (string): unit of measurement

        Return:
            ingredient(GroceryIngredient): the updated ingredient 
        """
        # TODO maybe optimize this later
        if ingredient_name != -1:
            self.ingredient_name = ingredient_name

        if quantity != -1:
            self.quantity = quantity

        if unit != -1:
            self.unit = unit

        db.session.add(self)

        return self

    def delete_ingredient(self):
        """Deletes the ingredient from the database
        """
        db.session.delete(self)
        db.session.commit()

    def to_dict(self):
        """Turns the PantryIngredient into a dict with its properties

        Returns:
            (dict): a dictionaty with all of the properties of this object
        """
        return {
            "id": self.id,
            "pantry_id": self.pantry_id,
            "ingredient_name": self.ingredient_name,
            "quantity": self.quantity,
            "unit": self.unit
        }
