"""Simple CLI tool that classifies a student's score into a grade band."""

# Grade thresholds, defined once so they're easy to tweak later
GRADE_BANDS = [
    (90, 100, "EXCELLENT"),
    (80, 89, "SUPERB"),
    (60, 79, "GREAT"),
    (50, 59, "PASSED"),
]
MIN_VALID_MARKS = 0
MAX_VALID_MARKS = 100
EXIT_COMMAND = "exit"


def get_grade_label(marks):
    """Return the grade label for a given score, or 'FAILED' if below all bands."""
    for lower_bound, upper_bound, label in GRADE_BANDS:
        if lower_bound <= marks <= upper_bound:
            return label
    return "FAILED"


def print_score_report(marks):
    """Print a friendly message summarizing the student's grade."""
    grade = get_grade_label(marks)
    if grade == "FAILED":
        print(f"Bad! You have FAILED. You need to work harder. Your score is {marks}")
    else:
        print(f"Congratulations! You are an {grade} student. Your score is {marks}")


def parse_marks(raw_input):
    """
    Convert user input into a valid marks value.
    Returns an int/float on success, or None if input is invalid.
    """
    try:
        marks = float(raw_input)
    except ValueError:
        print(f"Invalid input: '{raw_input}' is not a number. Please try again.")
        return None

    if not (MIN_VALID_MARKS <= marks <= MAX_VALID_MARKS):
        print(f"Invalid marks: must be between {MIN_VALID_MARKS} and {MAX_VALID_MARKS}.")
        return None

    return marks


def printBrand():
    print(f"Enter marks to check the grade (type '{EXIT_COMMAND}' to quit).")
    while True:
        raw_input_value = input("Enter marks: ").strip()

        if raw_input_value.lower() == EXIT_COMMAND:
            print("Goodbye!")
            break

        marks = parse_marks(raw_input_value)
        if marks is None:
            continue  # invalid input already reported — ask again

        print_score_report(marks)