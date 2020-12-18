## Receipt Analyzer

Receipt Analyzer is Python based REST API to extract and identify relevant information in USA sales receipts by using Azure Form Recognizer. This API was created as the final project for the course *ITIS 6177 - System Integration* which as part of my Master of Science degree from University of North Carolina at Charlotte. 

The API consist of three resources/opertaions:
 - **/receipt/analyze/** - Upload and Analyze Receipt
 - **/receipt/analyze/result/raw/{id}** - Returns Receipt Analysis Raw Result
 - **/receipt/analyze/result/{id}** - Returns Receipt Analysis Result
