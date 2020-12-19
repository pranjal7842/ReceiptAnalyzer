## Technical Implementation

## Project Structure

 - **docs** - folder contains all the md files for GitHub Pages
 - **receipt_analyzer** - main project folder
	 - **api** - contains code for controllers for different operations
	 - **service** - contains code to connect to azure form analyzer API and return the JSON results
 - **sample_receipts** - contains sample jpg files for testing


<br/>


## Setup
### Prerequisite:

 - Python 3
 - pip


### Setup on Local Windows Machine:

 - Clone the code from [GitHub Repo](https://github.com/pranjal7842/ReceiptAnalyzer)
 - Run the following commands:
	```
	cd receipt_analyzer
	pip install -r requirements.txt
	```


### Setup on Digital Ocean:

 - Clone the code from [GitHub Repo](https://github.com/pranjal7842/ReceiptAnalyzer) on local machine
 - Create a new CentOS Droplet
 - Transfer the code via ssh by executing following command:
	```
	scp -r ./receipt_analyzer root@<Droplet's I.P.>:~
	```
 - SSH into the Droplet by executing following command:
	```
	ssh root@<Droplet's I.P.>
	```
 - Prepare the droplet to run python code by executing following commands:
	```
	sudo dnf update -y
	sudo dnf install python3 -y
	sudo dnf -y groupinstall development
	```


### Start the REST API:

 - Run the following command:
	```
	python3 receipt_analyzer/app.py
	```
