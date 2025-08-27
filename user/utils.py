from rest_framework.response import Response


def success_response(
        statusCode : int ,
        message : str ,
        data : any
) :
    """function that returns a successful response 

    Args:
        statusCode (int): _description_
        message (str): _description_
        data (any): _description_
    """

    obj = {
        'statusCode' : statusCode ,
        'message' : message,
        'data' : data
    }

    return Response(data=obj , status=statusCode)

def error_validation(
        serializer : any ,
        message : str,
        statusCode : int 
) :
    
    """Function that handles error validation
    """

    errors = []

    for field , error_list in serializer.errors.items() :
        for error in error_list :
            errors.append({'field' :field , "message": str(error)})
    obj = {
        'statusCode' : statusCode ,
        'message' : message,
        'data' : errors
    }

    return Response (data=obj , status=statusCode)