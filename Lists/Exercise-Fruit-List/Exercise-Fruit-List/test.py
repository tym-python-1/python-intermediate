import subprocess
import json
import platform

def run_test(input_data):
    # Run main.py as a subprocess
    if platform.system() == "Windows":
        python_interpreter = 'python'
    else:
        python_interpreter = 'python3'

    # Run main.py as a subprocess
    process = subprocess.Popen([python_interpreter, 'solution.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Pass input data to main.py
    stdout, stderr = process.communicate(input_data)

    # Return the output of main.py
    return stdout.strip()

def main():
    # Define test cases
    with open('check.json') as f:
        test_cases = json.load(f)
        test_cases = test_cases["templateTests"]
        # print(test_cases["templateTests"])

    # Run test cases
    for i, case in enumerate(test_cases, 1):
        print(f"Running test case {i}:")
        actual_output = run_test(case["input"])
        if actual_output == case["output"]:
            print("Test passed")
        else:
            print("Test failed")
            print("Expected output:", case["output"])
            print("Actual output:", actual_output)

if __name__ == "__main__":
    main()