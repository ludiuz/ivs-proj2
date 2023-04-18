# ivs-proj2
## Project: Calculator
This project is a calculator with a command-line interface and an optional graphical user interface (GUI). To run the calculator, you need to have the required dependencies installed and execute the src/main.py script.


### Setting up a virtual environment
To create a virtual environment using Python's built-in env module, follow these steps:

1. #### Open a terminal and navigate to the project directory.
2. #### Run one of the following command to create a virtual environment named venv:
	```python3 -m venv env```
	
4. #### Activate the virtual environment:
	>For Linux or macOS:

	```source env/bin/activate```
	>For Windows:

	```.\env\Scripts\activate```


###  Installing required libraries
After activating the virtual environment, install the necessary libraries listed in the requirements.txt file by running the following command:

```pip install -r requirements.txt```


### Running main.py
With the virtual environment activated and required libraries installed, you can now run src/main.py. To do this, execute the following command:

```python src/main.py```

By default, the calculator will run with a GUI. You can also run the calculator in command-line mode with various options:
```
--no-gui: Run the calculator without the GUI.
--help or -h: Display help information.
--compute <formula> or -c <formula>: Directly compute the result of the given formula.
```
For example, to compute the result of "2 + 3" directly, use:

```python src/main.py --compute "2 + 3"```

To exit the command-line mode, type "q", "quit", or "exit".
