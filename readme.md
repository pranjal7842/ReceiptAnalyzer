# Receipt Analyzer

Python based REST API to extract and identify relevant information in USA sales receipts by using Azure Form Recognizer.


<br/>


## Azure Form Recognizer
Azure Form Recognizer is a cognitive service that lets you build automated data processing software using machine learning technology. Identify and extract text, key/value pairs, selection marks, tables, and structure from your documents—the service outputs structured data that includes the relationships in the original file, bounding boxes, confidence and more. You quickly get accurate results that are tailored to your specific content without heavy manual intervention or extensive data science expertise. Use Form Recognizer to automate data entry in your applications and enrich your documents search capabilities.

Form Recognizer is composed of custom document processing models, prebuilt models for invoices, receipts and business cards, and the layout model. You can call Form Recognizer models by using a REST API or client library SDKs to reduce complexity and integrate it into your workflow or application.

Refer to Azure Form Recognizer [documentation](https://azure.microsoft.com/en-us/services/cognitive-services/form-recognizer/) for more details on it.


<br/>


## API Details
API uses Swagger-UI to visualize and interact with the API’s resources. API is deployed on DigitalOcean and can be accessed by [Swagger-UI](http://68.183.137.125:8888/api/) link. To test the API:
 - Scan the receipt as a JPG file
 - Upload the scanned file using Swagger-UI
 - View the analysis result in JSON format

Some sample receipts can be found [here](https://github.com/pranjal7842/ReceiptAnalyzer/tree/main/sample_receipts).


<br/>


Looking for more details on Receipt Analyzer API please check out the API's **[GitHub Pages](https://pranjal7842.github.io/ReceiptAnalyzer/)** :books:

All the markdown files used by Github Pages can be found in **[/docs](https://github.com/pranjal7842/ReceiptAnalyzer/tree/main/docs)** folder.
