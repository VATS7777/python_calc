import sys


from PyQt5.QtWidgets import QApplication
from view import GUI
from controller import Controller
from  model import evaluateExpression

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    pycalc = QApplication(sys.argv)
    # Show the calculator's GUI
    view = GUI()
    view.show()

	# Create instances of the model and the controller
    model = evaluateExpression
    Controller(model=model, view=view)

    # Execute the calculator's main loop
    sys.exit(pycalc.exec_())

if __name__ == '__main__':
    main()