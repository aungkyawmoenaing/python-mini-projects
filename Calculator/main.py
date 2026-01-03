from calculator import add, subtract, multiply, divide
from logger import get_logger

logger = get_logger(__name__)

def main():
    print("Welcome to the Professional Calculator App")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == "5":
            print("Exiting calculator. Goodbye!")
            logger.info("Calculator exited by user.")
            break
        
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            logger.warning("User entered non-numeric values.")
            continue
        
        try:
            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
            logger.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
