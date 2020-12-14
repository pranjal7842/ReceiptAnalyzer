import logging

from flask_restplus import Api
from receipt_analyzer import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Receipt Analyzer API',
          description='Extract receipt data using the Form Recognizer REST API with Python')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500