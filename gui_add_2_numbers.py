from guizero import App, TextBox, PushButton, Text

def add_numbers():
    try:
        num1 = int(entry_num1.value)
        num2 = int(entry_num2.value)
        result = num1 + num2
        result_text.value = f"Result: {result}"
    except ValueError:
        result_text.value = "Invalid input. Please enter numbers."

app = App("Addition App", width=300, height=200)
text1 = Text(app, text="Put your 2 numbers here.")
entry_num1 = TextBox(app, width=10)
entry_num2 = TextBox(app, width=10)
add_button = PushButton(app, add_numbers, text="Add")
result_text = Text(app, text="Result: ")
app.display()
