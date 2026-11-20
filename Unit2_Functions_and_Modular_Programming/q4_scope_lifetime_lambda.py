"""Unit 2 - Q4: Scope, Lifetime and Lambda Functions"""

# ---------- Global variable ----------
# Created when the program starts, destroyed when the program ends.
counter = 10
message = "I am a global variable"


def show_local():
    """Local variable: created when the function is called and
    destroyed as soon as the function returns."""
    local_var = "I am local to show_local()"
    print("Inside show_local():", local_var)
    print("Inside show_local() reading global:", message)  # reading a global is allowed


def modify_without_global():
    """Assigning to a name creates a NEW local variable;
    the global 'counter' is not changed."""
    counter = 99
    print("Inside modify_without_global(), local counter =", counter)


def modify_with_global():
    """The 'global' keyword lets the function change the global variable."""
    global counter
    counter += 5
    print("Inside modify_with_global(), global counter =", counter)


def outer():
    """Enclosing / nested scope example (LEGB rule)."""
    x = "enclosing"

    def inner():
        y = "inner local"
        print("inner() sees:", x, "and", y)

    inner()
    # print(y)  # would raise NameError - y's lifetime ended with inner()


if __name__ == "__main__":
    print("=== Scope and Lifetime ===")
    print("Start of program, global counter =", counter)

    show_local()
    # print(local_var)  # NameError: local variable no longer exists

    modify_without_global()
    print("After modify_without_global(), global counter =", counter)

    modify_with_global()
    print("After modify_with_global(), global counter =", counter)

    outer()

    print("\nLifetime summary:")
    print(" - Global variables live from program start to program end.")
    print(" - Local variables live only while their function is executing.")

    print("\n=== Lambda Functions ===")
    square = lambda x: x ** 2
    cube = lambda x: x ** 3
    maximum = lambda a, b: a if a > b else b
    addition = lambda a, b: a + b

    n = int(input("Enter a number: "))
    m = int(input("Enter another number: "))
    print(f"Square of {n}       = {square(n)}")
    print(f"Cube of {n}         = {cube(n)}")
    print(f"Max of {n} and {m}  = {maximum(n, m)}")
    print(f"Sum of {n} and {m}  = {addition(n, m)}")
