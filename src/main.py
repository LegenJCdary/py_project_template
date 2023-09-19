from typing import Optional


def print_something(something: Optional[str]) -> None:
    print(something)


def main():
    print_something("Veritas vos liberabit.")
    print_something(None)


def py_project_template():
    return main()


if __name__ == "__main__":
    py_project_template()
