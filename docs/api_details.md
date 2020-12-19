## API Details

API is deployed on DigitalOcean and can be accessed by [Swagger UI](http://68.183.137.125:8888/api/) link. The API consist of three resources/operations:

 - **/receipt/analyze/**
	 - **Summary:** Upload and Analyze Receipt
	 - **Description:** Analyze and returns the results for scanned(JPG) receipt
	 - **HTTP Method:** POST
	 - **consumes:** multipart/form-data
	 - **Response content type:** application/json
	 - **parameter:** 
		 - **Name:** receipt_file
		 - **type:** file
	 - Sample receipt files to test can be found **[here](https://github.com/pranjal7842/ReceiptAnalyzer/tree/main/sample_receipts)**


<br/>

 - **/receipt/analyze/result/raw/{analysis_result_id}**
	 - **Summary:** Returns Receipt Analysis Raw Result
	 - **Description:** Returns receipt analysis raw result using the analysis result id from Analyze operation
	 - **HTTP Method:** GET
	 - **consumes:** multipart/form-data
	 - **Response content type:** application/json
	 - **parameter:** 
		 - **Name:** analysis_result_id
		 - **type:** string
	 - To execute this operation use a previously known analysis result id. If the id is not known then run the analyze operation by uplading a receipt file and using the analysis result id from its response.

<br/>

 - **/receipt/analyze/result/{analysis_result_id}**
	 - **Summary:** Returns Receipt Analysis Result
	 - **Description:** Returns receipt analysis result using the analysis result id from Analyze operation
	 - **HTTP Method:** GET
	 - **consumes:** multipart/form-data
	 - **Response content type:** application/json
	 - **parameter:** 
		 - **Name:** analysis_result_id
		 - **type:** string
	 - To execute this operation use a previously known analysis result id. If the id is not known then run the analyze operation by uplading a receipt file and using the analysis result id from its response.

<br/>

**Full Swagger JSON** for the API deployed on Digital Ocean can be found [here](http://68.183.137.125:8888/api/swagger.json).
