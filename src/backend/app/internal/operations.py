from decimal import Decimal
from ..schemas.number_schema import NumberSchema

import json

# Read the units guide from the JSON file
with open('app/config/units_conversion.json') as conversion_file_guide:
    conversion_guide = json.load(conversion_file_guide)

conversion_file_guide.close()

def convert_function( 
        number: Decimal, 
        unit_source: str, 
        unit_target: str, 
        type_of_conversion : ["weight","height","distance" ]) -> (Decimal, str):

   # Convert the number to the base unit - kg
    base_number = number / Decimal(conversion_guide[str(type_of_conversion)][str(unit_source)])

    # Convert the number from kg to the target unit
    target_number = base_number * Decimal(conversion_guide[str(type_of_conversion)][str(unit_target)])

    # precision decimal places
    target_number = Decimal(target_number).quantize(Decimal(str(conversion_guide["precision"])))

    return target_number, unit_target

def convert_units(
        entry_data: NumberSchema,
        type_of_conversion : ["weight","height","distance"], unit_target: str) -> NumberSchema:
    
    if entry_data.unit not in conversion_guide[str(type_of_conversion)].keys() or unit_target not in conversion_guide[str(type_of_conversion)].keys():

        raise Exception 

    try:

        target_number, unit_target = convert_function(entry_data.number, entry_data.unit, unit_target, type_of_conversion)

        return NumberSchema(number=target_number, unit=unit_target)
    
    except Exception as e:
        print(e)
        
def add_or_subtract_units(
        entry_data_1: NumberSchema, 
        entry_data_2: NumberSchema, 
        type_of_conversion: ["weight","height","distance"],
        type_of_operation:  ["add", "subtract"]) -> (NumberSchema, NumberSchema):
    
    if type_of_operation == "add":

        #sum 1
        number_2_converted = convert_units(entry_data_2, type_of_conversion, entry_data_1.unit)

        result_add_1 = NumberSchema(number=entry_data_1.number + number_2_converted.number, unit=entry_data_1.unit)


        #sum 2

        number_1_converted = convert_units(entry_data_1, type_of_conversion, entry_data_2.unit)

        result_add_2 = NumberSchema(number=entry_data_2.number + number_1_converted.number, unit=entry_data_2.unit)

        return result_add_1, result_add_2
    
    elif type_of_operation == "subtract":

        # Convert to the same unit and get the highest number

        number_2_converted = convert_units(entry_data_2, type_of_conversion, entry_data_1.unit)

        highest_number = max(entry_data_1.number, number_2_converted.number)

        lowest_number = min(entry_data_1.number, number_2_converted.number)

        # Subtract 1 - the lowest number from the highest number with the same unit of the first entry data

        result_subtract_1 = NumberSchema(number=highest_number - lowest_number, unit=entry_data_1.unit)

        # Convert to the same unit that the second entry data

        number_1_converted = convert_units(entry_data_1, type_of_conversion, entry_data_2.unit)

        # Subtract 2 - the lowest number from the highest number with the same unit of the second entry data

        highest_number = max(entry_data_2.number, number_1_converted.number)

        lowest_number = min(entry_data_2.number, number_1_converted.number)

        result_subtract_2 = NumberSchema(number=highest_number - lowest_number, unit=entry_data_2.unit)

        return result_subtract_1, result_subtract_2





        


        
    

    
    


