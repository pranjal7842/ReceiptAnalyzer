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
	sudo dnf install epel-release
	sudo yum install screen
	```


### Start the REST API:

#### If running on local windows machine
 - Replace IP in settings.py file with *localhost*
 - Run the following command:
	```
	python receipt_analyzer/app.py
	```

#### If running on digital ocean droplet
 - Run the following command:
	```
	screen -S session1
	python3 receipt_analyzer/app.py
	```
 - Use Ctrl+A+D to detach the screen session before closing command prompt. This will ensure the python server is up and running even if command prompt is closed.
