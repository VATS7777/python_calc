# python_calc


	* PHP MVC is an application design pattern that separates the application data and business logic (model) from the presentation (view).


	* MVC stands for Model, View & Controller


	1> Model


	The model is responsible for managing the data of the application. It responds to the request from the view and it also responds to instructions from the controller to update itself.


	2> View


	It displays all the records fetched within the model. View never interacts with model; controller does this work (communicating with model and view).


	3> Controller


	The controller is responsible for responding to the user input and perform interactions on the data model objects. The controller receives the input, it validates the input and then performs the business operation that modifies the state of the data model.

	Controller interacts with model through the getAll() method which fetches all the records displayed to the end user.


	* When we have  instantiate a Controller we  have to specify a Model and a View


	4> What is PyQt5?


	PyQt is a library that lets you use the Qt GUI framework from Python. Qt itself is written in C++. By using it from Python, you can build applications much more quickly while not sacrificing much of the speed of C++.	


# Steps 

	1> Install PyQt
  	
  	* pip3 install pyqt5


  	2> Here’s a step-by-step MVC pattern for a GUI desktop application(Python_Calculator):
  	

	* The user performs an action or request (event) on the view (GUI).


	* The view notifies the controller about the user’s action.


	* The controller gets the user’s request and queries the model for a response.


	* The model processes the controller query, performs the required operations, and returns an answer or result.


	* The controller receives the model’s answer and updates the view accordingly.
	  The user finally sees the requested result on the view.
