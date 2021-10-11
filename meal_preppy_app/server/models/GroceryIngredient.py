from models.Shared import db


class GroceryIngredient(db.Model):
    """
    Ingredients table that holds ingredient names and quantities

    ...

    Columns
    -------
    id: int
        A unique identifier for the Ingredients

    grocerylist_id: int
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
    __tablename__ = "groceryingredients"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    grocerylist_id = db.Column(
        db.Integer,
        db.ForeignKey('grocerylists.id', ondelete='cascade'),
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

    # Instance Methods
    # ----------------
    def updateItem(self, ingredient_name=-1, quantity=-1, unit=-1):
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
        if ingredient_name:
            self.ingredient_name = ingredient_name

        if quantity:
            self.quantity = quantity

        if unit:
            self.unit = unit

        db.session.add(self)

        return self
