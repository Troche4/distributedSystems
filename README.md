# distributedSystems
Author: Trey Roche

### Project details:
The project is to create a decentralized client/server system for creating and responding to quiz questions. Instructors should be able to create questions of several different types and present them along with a code to join the quiz. Students should be able to use the code to access the questions. This code is for phase 1 of the project, which was to model the questions and quizzes using XML and object orientation, and to begin understanding a way to implement the backend.

Stack: HTML, XML, Python, Flask

### Setup: 
To keep this project's dependencies from interfering from those of the local machine, it is advised to run a virtual environment.

First, install pip at https://pip.pypa.io/en/stable/installing/

Secondly, clone this repository and run this command in the distributedSystems directory:
`$ pip install -r requirements.txt`

Next, set up the virtual environment:
`$ virtualenv <your_virtualenv_name>`


### Testing:
To run the virtual environment:
`$ source /<your_virtualenv_name>/bin/activate`

To run the app for testing Flask (with the virtualenv active):
`(virtualenv) $ python main.py`
The output of running the above command will provide an IP address and port on which the app is running. Access that address and port in a web browser to see the app.

To test the XML parsing, simply run the file in the command line:
`$ python InstructorXMLParser.py`
`$ python StudentXMLParser.py`
The results will be printed to the command line. These files are configured to parse some sample XML data, but you can change the URL in the `if __name__ == "__main__":`block to point to any other XML file. 
