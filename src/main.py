# libs
import sys

# scripts
import core
import gui

def get_result(formula, engine):
    result = engine.validate(formula)
    if isinstance(result, float):
        print(result)
    elif isinstance(result, tuple):
        if "--full-error" in sys.argv:
            print(result[1])
        else:
            print(result[0])
    else:
        print("¯\\_(ツ)_/¯")
                
def ask4input():
    return input("Input formula: ")

if __name__ == "__main__":
    engine = core.Engine()
    if ("--help" or "-h") in sys.argv:
        print("You got this man")
    elif "--no-gui" in sys.argv:
        formula = ask4input()
        while (formula not in ["q", "quit", "exit"]):
            get_result(formula, engine)
            formula = ask4input()
    elif "-c" in sys.argv or "--compute" in sys.argv:
        idx = next(i for i, arg in enumerate(sys.argv) if arg in ["--compute", "-c"])
        if len(sys.argv) != 1 + idx and sys.argv[idx + 1]:
            get_result(sys.argv[idx + 1], engine)
    else:
        app = gui.CalculatorGUI(engine)
        app.run_loop()
