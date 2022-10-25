import jsonschema
from jsonschema import validate

def Validator(jsonData, schemaName):
    try:
        validate(instance=jsonData, schema=schemaName)
    except jsonschema.exceptions.ValidationError as err:
        try:
            return err.schema["error_message"]
        except:
            return err.message
    return True