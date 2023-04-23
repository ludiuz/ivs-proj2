# libs
import sys

# scripts
import calculator
import gui


def get_result(formula, engine):
    """
    Get the result of the formula using the provided engine and print the result.
    If the result is a tuple (an error), print the error type or the full error message
    depending on the command-line arguments. Otherwise, print the result directly.
    """
    result = engine(formula)
    if isinstance(result, tuple):  # error output
        if "--full-error" in sys.argv:
            print(result[1])
        else:
            print(result[0])
    else:
        print(result)


def ask4input():
    return input("Input formula: ")


if __name__ == "__main__":
    engine = calculator.Calculator()

    ## @brief Display help message
    if ("--help" or "-h") in sys.argv:
        help_text = (
            "Usage: main.py [OPTION]... [ARGUMENT]...\n\n"
            "Options:\n"
            "  -h, --help               Show this help message and exit.\n"
            "  --no-gui                 Run the calculator in the terminal with an input loop.\n"
            "                           Terminate the loop by entering 'q', 'quit', or 'exit'.\n"
            "  -c, --compute [FORMULA]  Compute the formula directly without launching the GUI.\n"
            "  --full-error             Show the full error message when an error occurs.\n"
            "                           Must be used with the --no-gui or --compute option.\n"
        )
        print(help_text)

    ## @brief Run calculator in terminal (no GUI)
    elif "--no-gui" in sys.argv:
        # Run in command-line mode, repeatedly asking for input until the user types 'q', 'quit', or 'exit'
        while (formula := input("Input formula: ")) not in ["q", "quit", "exit"]:
            get_result(formula, engine)

    ## @brief Compute a formula directly without launching the GUI
    elif "-c" in sys.argv or "--compute" in sys.argv:
        # Directly compute the input provided as an argument following "--compute" or "-c"
        idx = next(i for i, arg in enumerate(sys.argv) if arg in ["--compute", "-c"])
        if len(sys.argv) != 1 + idx and sys.argv[idx + 1]:
            get_result(sys.argv[idx + 1], engine)

    ## @brief Launch the calculator's GUI
    else:
        # Launch the GUI application if no command-line arguments are provided
        app = gui.App(engine)
        app.run()
