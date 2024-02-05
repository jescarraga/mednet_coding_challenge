from pydantic  import BaseModel
from decimal import Decimal

class NumberSchema(BaseModel):
    # Define the number float positive type and the required field
    number: Decimal
    unit : str
