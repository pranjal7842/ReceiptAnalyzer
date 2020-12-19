# Controller script defining all the operations

from flask_restplus import Resource
from werkzeug.datastructures import FileStorage
from api.restplus import api
from service import analyzer_service as service

ns = api.namespace('receipt/analyze', description='Operations related Receipt Analysis')
upload_parser = api.parser()
upload_parser.add_argument('receipt_file', location='files', type=FileStorage, required=True)

@ns.route('/')
@api.doc(
    description="Analyze and returns the results for scanned(JPG) receipt"
)
class ReceiptAnalysis(Resource):

    # Operation to Upload and Analyze Receipt
    @api.expect(upload_parser)
    def post(self):
        """Upload and Analyze Receipt"""
        args = upload_parser.parse_args()
        uploaded_file = args['receipt_file']
        return service.analyze_file(uploaded_file)


@ns.route('/result/<string:analysis_result_id>')
@api.doc(
    description="Returns receipt analysis result using the analysis result id from Analyze operation",
    params={"analysis_result_id": "Analysis result id from Analyze operation"}
)
class ReceiptAnalysisResult(Resource):

    # Operation to Get Receipt Analysis Result
    def get(self, analysis_result_id):
        """Returns Receipt Analysis Result"""
        return service.get_analyze_result(analysis_result_id)


@ns.route('/result/raw/<string:analysis_result_id>')
@api.doc(
    description="Returns receipt analysis raw result using the analysis result id from Analyze operation",
    params={"analysis_result_id": "Analysis result id from Analyze operation"}
)
class ReceiptAnalysisRawResult(Resource):

    # Operation to Get Receipt Analysis Raw Result
    def get(self, analysis_result_id):
        """Returns Receipt Analysis Raw Result"""
        return service.get_analyze_raw_result(analysis_result_id)
