# test_main.py
import os
import pytest
import subprocess

# Get the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
main_py_path = os.path.join(script_dir, "..", "src", "main.py")


def test_help():
    expected_output = (
        "Usage: main.py [OPTION]... [ARGUMENT]...\n\n"
        + "Options:\n"
        + "  -h, --help               Show this help message and exit.\n"
        + "  --no-gui                 Run the calculator in the terminal with an input loop.\n"
        + "                           Terminate the loop by entering 'q', 'quit', or 'exit'.\n"
        + "  -c, --compute [FORMULA]  Compute the formula directly without launching the GUI.\n"
        + "  --full-error             Show the full error message when an error occurs.\n"
        + "                           Must be used with the --no-gui or --compute option.\n"
    )

    command = f"python {main_py_path} --help"
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True
    )

    assert result.stdout == expected_output + "\n"


def test_compute():
    command = f'python {main_py_path} --compute "3+2"'
    result = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True
    )

    assert result.stdout == "5.0" + "\n"


def test_compute():
    expected_output = "Input formula: " + "5.0\n" + "Input formula: "

    command = f"python {main_py_path} --no-gui"
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        input="3+2\nq\n",
        text=True,
        shell=True,
    )

    assert result.stdout == expected_output


if __name__ == "__main__":
    test_help()
    test_compute()
    test_no_gui()
