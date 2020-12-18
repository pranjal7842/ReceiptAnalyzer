import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask, Blueprint
import settings
from api.analyzer_controller import ns as controller_namespace
from api.restplus import api


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'
#logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
#logging.config.fileConfig(logging_conf_path)
#log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = settings.FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(controller_namespace)
    flask_app.register_blueprint(blueprint)


def main():
    initialize_app(app)
#    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(receipt_analyzer.config['SERVER_NAME']))
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()