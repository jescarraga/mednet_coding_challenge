from fastapi import APIRouter, HTTPException, status


# Import the schemas
from ..schemas.number_schema import NumberSchema

# Import the operations
from ..internal.operations import convert_units, add_or_subtract_units




# Instantiate APIRouter
router = APIRouter(
    prefix="/convert",
    tags=["convert"],
    responses={404: {"description": "Not found"}},
)

@router.get("/",
    response_model=str,
    summary="Get the home page",
    description="Get the home page of the API",
    status_code=status.HTTP_200_OK,
)
async def get_home_page():
    return "Welcome to the home page of the API"

# First route to convert a given number from the source Unit to the target Unit
@router.post("/{type_of_conversion}",
    response_model=NumberSchema,
    summary="simple convert number operation",
    description="Convert a number from the source unit to the target unit",
    status_code=status.HTTP_200_OK,
)
async def convert_units_request(entry_data: NumberSchema, type_of_conversion: str, unit_target: str):

    if entry_data.number < 0 or type_of_conversion not in ["weight", "height", "distance"]:
        raise HTTPException(status_code=400, detail="The number must be positive and the type of conversion must be weight, height or distance")
    else:
        try:
            return convert_units(entry_data, type_of_conversion, unit_target)
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Error in the conversion process. Please check the entry data and the type of conversion.")

@router.post("/{type_of_conversion}/{type_of_operation}",
    response_model= list[NumberSchema],
    summary="add or subtract and convert number operation",
    description="add or subtract two amounts that have different units of measurement",
    status_code=status.HTTP_200_OK,
)
async def add_or_subtract_units_request(
    entry_data_1: NumberSchema, 
    entry_data_2: NumberSchema, 
    type_of_conversion: str, 
    type_of_operation: str):

    if entry_data_1.number < 0 or entry_data_2.number < 0 or type_of_conversion not in ["weight", "height", "distance"] or type_of_operation not in ["add", "subtract"]:
        raise HTTPException(status_code=400, detail="The numbers must be positive and the type of conversion must be weight, height or distance and the type of operation must be add or subtract")
    else:
        try:
            return add_or_subtract_units(entry_data_1, entry_data_2, type_of_conversion, type_of_operation)
        
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Error in the conversion process. Please check the entry data and the type of conversion.")