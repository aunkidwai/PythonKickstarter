# Import the Gradio library for creating the user interface
import gradio as gr

# Define the calculator function
def calculate(num1, num2, operation):
    """
    Performs the specified arithmetic operation on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform: "Add", "Subtract", "Multiply", or "Divide".

    Returns:
        str: The result of the operation as a string, or an error message if division by zero occurs.
    """
    # Perform the operation based on the user's selection
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero"
        else:
            result = num1 / num2
    else:
        # Fallback for unexpected operation values (though prevented by dropdown)
        return "Invalid operation"
    
    # Format the result: integer if whole number, else two decimal places
    if result.is_integer():
        return str(int(result))
    else:
        return f"{result:.2f}"

# Create the Gradio interface
interface = gr.Interface(
    fn=calculate,  # The function to call
    inputs=[
        gr.Number(label="First number"),  # Input field for the first number
        gr.Number(label="Second number"),  # Input field for the second number
        gr.Dropdown(
            choices=["Add", "Subtract", "Multiply", "Divide"],
            label="Operation"  # Dropdown menu for selecting the operation
        )
    ],
    outputs=gr.Textbox(label="Result"),  # Output field to display the result
    title="Simple Calculator",  # Title of the interface
    description="Enter two numbers and select an operation to see the result."  # Brief instructions
)

# Launch the interface
interface.launch()
