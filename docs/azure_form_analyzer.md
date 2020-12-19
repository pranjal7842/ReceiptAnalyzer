## Azure Form Analyzer

Azure Form Recognizer is a cognitive service that lets you build automated data processing software using machine learning technology. Identify and extract text, key/value pairs, selection marks, tables, and structure from your documents—the service outputs structured data that includes the relationships in the original file, bounding boxes, confidence and more. You quickly get accurate results that are tailored to your specific content without heavy manual intervention or extensive data science expertise. Use Form Recognizer to automate data entry in your applications and enrich your documents search capabilities.

Form Recognizer is composed of custom document processing models, prebuilt models for invoices, receipts and business cards, and the layout model. You can call Form Recognizer models by using a REST API or client library SDKs to reduce complexity and integrate it into your workflow or application.

Refer to Azure Form Recognizer [documentation](https://azure.microsoft.com/en-us/services/cognitive-services/form-recognizer/) for more details on it.


<br/>


## Azure Setup
 - To start using the Azure Form Service we need to first create a new Form Recognizer resource on the Azure portal.
 - Once the resource is created it will give endpoint and the resourse key. These are used in Receipt Analyzer API's code when making call to azure service.


<br/>


## Azure Form Analyzer APIs
To start analyzing a receipt, we call Analyze Receipt API using the Python code in Receipt Analyzer API. The response of this API includes an Operation-Location header, which is used get the results in JSON format using Get Analyze Receipt Result API. There are 2 main node in the JSON response 
 - readResults - This node contains all of the recognized text. Text is organized by page, then by line, then by individual words. 
 - documentResults - This node contains the receipt-specific values that the model discovered. This is where we'll find useful key/value pairs like the tax, total, merchant address, and so on.

Refer to below links from Azure Form Recognizer [documentation] for more details on these APIs:
 - [Analyze Receipt API](https://westus2.dev.cognitive.microsoft.com/docs/services/form-recognizer-api-v2/operations/AnalyzeReceiptAsync)
 - [Get Analyze Receipt Result API](https://westus2.dev.cognitive.microsoft.com/docs/services/form-recognizer-api-v2/operations/GetAnalyzeReceiptResult)
