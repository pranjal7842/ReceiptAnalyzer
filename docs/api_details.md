## API Details

API is deployed on DigitalOcean and can be accessed by [Swagger UI](http://68.183.137.125:8888/api/) link. The API consist of three resources/operations:

 - **/receipt/analyze/**
	 - **Summary:** Upload and Analyze Receipt
	 - **HTTP Method:** POST
	 - **consumes:** multipart/form-data
	 - **Response content type:** application/json
	 - **parameter:** 
		 - **Name:** receipt_file
		 - **type:** file

<br/>

 - **/receipt/analyze/result/raw/{id}**
	 - **Summary:** Returns Receipt Analysis Raw Result
	 - **HTTP Method:** GET
	 - **consumes:** multipart/form-data
	 - **Response content type:** application/json
	 - **parameter:** 
		 - **Name:** analysis-result-id
		 - **type:** string

<br/>

 - **/receipt/analyze/result/{id}**
	 - **Summary:** Returns Receipt Analysis Result
	 - **HTTP Method:** GET
	 - **consumes:** multipart/form-data
	 - **Response content type:** application/json
	 - **parameter:** 
		 - **Name:** analysis-result-id
		 - **type:** string

<br/>

**Full Swagger JSON** for the API deployed on Digital Ocean can be found [here](http://68.183.137.125:8888/api/swagger.json).
