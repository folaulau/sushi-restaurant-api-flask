
authenticate_schema = {
    "type": "object",
    "properties": {
        "token": {
            "type": "string",
            "error_message": "token is invalid"
        }
    },
    "required": ["token"]
}