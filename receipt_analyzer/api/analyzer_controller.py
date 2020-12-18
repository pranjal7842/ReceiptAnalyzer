import string

from flask_restplus import Resource
from werkzeug.datastructures import FileStorage
from api.restplus import api
from service import analyzer_service as service

ns = api.namespace('receipt/analyze', description='Operations related Receipt Analysis')
upload_parser = api.parser()
upload_parser.add_argument('receipt_file', location='files', type=FileStorage, required=True)

@ns.route('/')
class ReceiptAnalysis(Resource):

    @api.expect(upload_parser)
    def post(self):
        """Upload and Analyze Receipt"""
        args = upload_parser.parse_args()
        uploaded_file = args['receipt_file']
        return service.analyze_file(uploaded_file)


@ns.route('/result/<string:id>')
@api.doc(params={"id": "Result ID"})
class ReceiptAnalysisResult(Resource):

    def get(self, id):
        """Returns Receipt Analysis Result"""
        return service.get_analyze_result(id)


@ns.route('/result/raw/<string:id>')
@api.doc(params={"id": "Result ID"})
class ReceiptAnalysisResult(Resource):

    def get(self, id):
        """Returns Receipt Analysis Raw Result"""
        return service.get_analyze_raw_result(id)
