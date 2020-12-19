# Python script to define default error handling and defining API details

from flask_restplus import Api
import settings


# Defining API Details
api = Api(version='1.0', title='Receipt Analyzer API',
          description='Extract receipt data using the Form Recognizer REST API with Python')


# Default Error Handler
@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.' + str(e)
    print(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500