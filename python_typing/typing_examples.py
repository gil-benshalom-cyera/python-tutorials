from typing import List, Dict, Tuple, Set, Optional, Callable


# 1️⃣ Basic Type Hints
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b


# 2️⃣ Using Collections in Type Hints
def process_numbers(numbers: List[int]) -> Tuple[int, int]:
    """Returns the sum and max of a list of numbers."""
    return sum(numbers), max(numbers)


# 3️⃣ Complex Nested Types: List of Dictionaries
def get_student_scores() -> List[Dict[str, int]]:
    """Returns a list of student scores (name -> score)."""
    return [{"Alice": 90}, {"Bob": 85}, {"Charlie": 78}]


# 4️⃣ Using Sets in Function Signatures
def get_unique_names(names: List[str]) -> Set[str]:
    """Returns a set of unique names."""
    return set(names)


# 5️⃣ Optional Type Hint (Value Can Be `None`)
def find_student_score(name: str, scores: Dict[str, int]) -> Optional[int]:
    """Returns the student's score if found, otherwise None."""
    return scores.get(name)


# 6️⃣ Using a User-Defined Class in Type Hints
class Person:
    """A simple class representing a person."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person(name: str, age: int) -> Person:
    """Creates and returns a Person object."""
    return Person(name, age)


# 7️⃣ Using Type Aliases for Readability
ScoreDict = Dict[str, int]  # Alias for dictionary of student scores


def get_top_student(scores: ScoreDict) -> str:
    """Returns the student with the highest score."""
    return max(scores, key=scores.get)


# 8️⃣ Using `Callable` for Function Signatures
def apply_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    """Applies a function to two numbers."""
    return func(x, y)


def main():
    # Basic types
    print(add(3, 5))

    # Collection types
    numbers = [10, 20, 30]
    print(process_numbers(numbers))

    # Complex nested types
    students = get_student_scores()
    print(students)

    # Sets
    print(get_unique_names(["Alice", "Bob", "Alice"]))

    # Optional return type
    scores = {"Alice": 95, "Bob": 88}
    print(find_student_score("Alice", scores))  # ✅ 95
    print(find_student_score("Charlie", scores))  # ✅ None

    # User-defined class
    person = create_person("John", 28)
    print(person)

    # Type alias
    student_scores = {"Alice": 90, "Bob": 85, "Charlie": 78}
    print(get_top_student(student_scores))

    # Callable function
    print(apply_function(add, 4, 7))  # ✅ Works with any function matching (int, int) -> int


# 🎯 Example Usage
if __name__ == "__main__":
    main()
