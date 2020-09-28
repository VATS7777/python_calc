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

	