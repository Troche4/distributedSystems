# distributedSystems

Repo for the clicker project in COMP 339/439.
Team members: Matt Hempe, Trey Roche

Project details:
The project is to create a decentralized client/server system for creating and responding to quiz questions. Instructors should be able to create questions of several different types and present them along with a code to join the quiz. Students should be able to use the code to access the questions. 

Stack: HTML& CSS, XML, Python, Flask, MySQL.

Setup: 
To keep this project's dependencies from interfering from those of the local machine, it is advised to run a virtual environment.

First, install pip at https://pip.pypa.io/en/stable/installing/

Secondly, clone this repository and run this command in the distributedSystems directory:
pip install -r requirements.txt

Next, set up the virtual environment:
virtualenv <your_virtualenv_name>

To run the virtual environment:
source /<your_virtualenv_name>/bin/activate

To run the app through Flask (with the virtualenv active):
python main.py

The output of running the above command will provide an IP address and port on which the app is running. Access that address and port in a web browser to see the app.
