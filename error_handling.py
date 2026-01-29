import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception
class NegativeNumberError(Exception):
    pass


def divide_numbers(a, b):
    try:
        if a < 0 or b < 0:
            raise NegativeNumberError("Negative numbers are not allowed")

        result = a / b

    except ZeroDivisionError:
        logging.error("Attempted division by zero")
        print("Error: Division by zero is not allowed.")

    except TypeError:
        logging.error("Invalid data type used")
        print("Error: Please enter numeric values only.")

    except NegativeNumberError as e:
        logging.error(e)
        print(f"Error: {e}")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred.")

    else:
        print(f"Result: {result}")

    finally:
        print("Execution completed.")


# Simulating runtime errors
if __name__ == "__main__":
    divide_numbers(10, 2)     # Valid
    divide_numbers(10, 0)     # ZeroDivisionError
    divide_numbers("10", 5)   # TypeError
    divide_numbers(-5, 2)     # Custom Exception
