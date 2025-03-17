# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")


# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# greet_with("Jack Bauer", "Nowhere")

# greet_with("Nowhere", "Jack Bauer")

greet_with(name = "Jack Bauer", location = "Nowhere")
greet_with(location = "Nowhere", name = "Jack Bauer")