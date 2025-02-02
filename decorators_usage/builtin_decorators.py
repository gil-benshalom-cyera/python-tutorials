from abc import ABC, abstractmethod
from functools import lru_cache
from dataclasses import dataclass
from utils.decorators import time_it
import time


# 1️⃣ Abstract Base Class with `@abstractmethod`
class Shape(ABC):
    """Abstract base class to demonstrate @abstractmethod."""

    @abstractmethod
    def area(self):
        """Must be implemented by subclasses."""
        pass


# 2️⃣ Data Class (`@dataclass`)
@dataclass
class Rectangle(Shape):
    """Demonstrates @dataclass (auto-generates __init__, __repr__, etc.)."""

    width: float
    height: float

    # 3️⃣ Property Decorator
    @property
    def area(self):
        """Demonstrates @property (computed attribute)."""
        return self.width * self.height

    # 4️⃣ Getter Method
    @property
    def width_in_cm(self):
        """Returns width in centimeters."""
        return self.width * 100

    # 5️⃣ Setter Method
    @width_in_cm.setter
    def width_in_cm(self, value):
        """Sets width in meters (converts from cm)."""
        self.width = value / 100

    # 6️⃣ Class Method (`@classmethod`)
    @classmethod
    def from_square(cls, side_length):
        """Creates a rectangle from a square."""
        return cls(side_length, side_length)

    # 7️⃣ Static Method (`@staticmethod`)
    @staticmethod
    def is_valid_size(value):
        """Checks if a size is valid (positive)."""
        return value > 0

    # 8️⃣ LRU Cache (`@lru_cache`)
    @time_it
    @lru_cache(maxsize=10)
    def expensive_calculation(self, factor):
        """Expensive calculation that benefits from caching."""
        print(f"Computing: {self.width * self.height * factor}")
        time.sleep(5)
        return self.width * self.height * factor


    def __hash__(self):
        return hash((self.width, self.height))



def main():
    rect = Rectangle(5, 10)  # Uses @dataclass auto-generated constructor

    print(f"Area: {rect.area}")  # ✅ Uses @property
    print(f"Width in cm: {rect.width_in_cm}")  # ✅ Uses getter
    rect.width_in_cm = 300  # ✅ Uses setter (converts cm to meters)
    print(f"Updated Width: {rect.width}")

    square = Rectangle.from_square(4)  # ✅ Uses @classmethod
    print(f"Square Area: {square.area}")

    print(Rectangle.is_valid_size(-1))  # ❌ False (uses @staticmethod)
    print(Rectangle.is_valid_size(10))  # ✅ True

    print(rect.expensive_calculation(2))  # ✅ Uses @lru_cache
    print(rect.expensive_calculation(2))  # 🔥 Cached result (no recomputation)


# 🎯 **Testing the Built-in Decorators**
if __name__ == "__main__":
    main()
