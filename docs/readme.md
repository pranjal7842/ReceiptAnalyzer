## Receipt Analyzer

Receipt Analyzer is Python based REST API to extract and identify relevant information in USA sales receipts by using Azure Form Recognizer. This API was created as the final project for the course *ITIS 6177 - System Integration* which as part of my Master of Science degree from University of North Carolina at Charlotte. 

The API consist of three resources/opertaions:
 - **/receipt/analyze/** - Upload and analyze receipt. The result is filtered out and only relevant fields are returned.
 - **/receipt/analyze/result/raw/{analysis_result_id}** - Returns receipt analysis raw result.
 - **/receipt/analyze/result/{analysis_result_id}** - Returns receipt analysis result. This operation filters out the result and returns only relevant fields.
