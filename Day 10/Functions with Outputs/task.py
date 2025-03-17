def function_1(text):
    return text + text

def function2(text):
    return text.title()

output = function2((function_1("hello")))
print(output)