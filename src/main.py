import argparse
import sys

import calculator
import gui


def print_help():
    """Print a help message describing command-line options and their usage."""
    help_text = (
        "Usage: main.py [OPTION]... [ARGUMENT]...\n\n"
        + "Options:\n"
        + "  -h, --help               Show this help message and exit.\n"
        + "  --no-gui                 Run the calculator in the terminal with an input loop.\n"
        + "                           Terminate the loop by entering 'q', 'quit', or 'exit'.\n"
        + "  -c, --compute [FORMULA]  Compute the formula directly without launching the GUI.\n"
        + "  --full-error             Show the full error message when an error occurs.\n"
        + "                           Must be used with the --no-gui or --compute option.\n"
    )
    print(help_text)


def get_result(calc, s: str):
    """
    Get the result of the calculation.

    This function computes the result using the provided calculator and
    prints it. If an error occurs and the --full-error flag was provided,
    the full error message will be printed.

    :param calc: An instance of the calculator.
    :param s: The input string representing the formula.
    """
    result = calc(s)
    if isinstance(result, tuple):  # error output
        if print_full_error:
            print(result[1])
        else:
            print(result[0])
    else:
        print(result)


def compute(string_input: str):
    """
    Compute the given formula.

    This function creates a calculator instance and computes the result
    of the given input formula without launching the GUI.

    :param string_input: The input string representing the formula.
    """
    c = calculator.Calculator()
    get_result(c, string_input)


def run_loop():
    """
    Run the calculator in an input loop without GUI.

    This function creates a calculator instance and runs an input loop,
    asking for user input until the user types 'q', 'quit', or 'exit'.
    """
    c = calculator.Calculator()
    while (string_input := input("Input formula: ")) not in ["q", "quit", "exit"]:
        get_result(c, string_input)


def run_app():
    """
    Run the calculator app with GUI.

    This function launches the calculator application with a graphical
    user interface by creating an instance of the App class.
    """
    app = gui.App(calculator.Calculator())
    app.run()


def main():
    """Parse command-line arguments and call the appropriate function."""
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        "-h", "--help", action="store_true", help="Show this help message and exit"
    )
    parser.add_argument("-c", "--compute", type=str, help="Compute the string input")
    parser.add_argument(
        "--no-gui", action="store_true", help="Run the loop without GUI"
    )
    parser.add_argument(
        "--full-error", action="store_true", help="Set full error print mode"
    )

    args = parser.parse_args()

    if args.help:
        print_help()
        sys.exit()

    global print_full_error
    print_full_error = args.full_error

    if args.compute:
        compute(args.compute)
    elif args.no_gui:
        run_loop()
    else:
        run_app()


if __name__ == "__main__":
    main()
