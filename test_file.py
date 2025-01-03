import random
import subprocess
import pytest

def test_while():
    # Set up the test input (number to sum up to)
    test_input = str(random.randint(1, 100)) + "\n"
    n = int(test_input)
    # Expected output (sum of numbers from 1 to n)
    expected_output = str(n * (n + 1) // 2) + "\n"

    # Run the student's script and capture output
    result = subprocess.run(
        ['python3', 'while_summation.py'],  # Adjust this to the specific student script file
        input=test_input,
        text=True,
        capture_output=True
    )

    # Print statements for debugging
    print("\nTesting While:")
    print(f"Test input (n): {n}")
    print(f"Expected output: {expected_output.strip()}")
    print(f"Actual output: {result.stdout.strip()}")

    # Assert if the output is as expected
    assert result.stdout.strip() == expected_output.strip(), f"Expected {expected_output.strip()}, but got {result.stdout.strip()}"

def test_for():
    # Set up the test input (number to sum up to)
    test_input = str(random.randint(1, 100)) + "\n"
    n = int(test_input)

    # Expected output (sum of numbers from 1 to n)
    expected_output = str(n * (n + 1) // 2) + "\n"

    # Run the student's script and capture output
    result = subprocess.run(
        ['python3', 'for_summation.py'],  # Adjust this to the specific student script file
        input=test_input,
        text=True,
        capture_output=True
    )

    # Print statements for debugging
    print("\nTesting For: ")
    print(f"Test input (n): {n}")
    print(f"Expected output: {expected_output.strip()}")
    print(f"Actual output: {result.stdout.strip()}")

    # Assert if the output is as expected
    assert result.stdout.strip() == expected_output.strip(), f"Expected {expected_output.strip()}, but got {result.stdout.strip()}"
