# **Python Advanced Concepts: Decorators, Generators, Concurrency, and Design Patterns**

## **📌 Session Overview**
This session covers advanced Python topics, including **decorators**, **generators**, **concurrency**, **dependency injection**, **design patterns**, and **anti-patterns**. The goal is to demonstrate how these concepts **improve code efficiency, readability, and maintainability**.

---

## **1️⃣ Understanding Decorators**
### **🔹 What Are Decorators?**
Decorators in Python allow us to **modify functions and methods dynamically** without modifying their actual code. They help in:
- **Avoiding code duplication** by extracting reusable logic.
- **Adding functionality dynamically** (e.g., logging, error handling, caching).
- **Keeping code DRY (Don't Repeat Yourself).**

### **🔹 Custom Decorators Implemented**
1. `@time_it` - Measures function execution time.
2. `@log_exceptions` - Logs errors instead of crashing.
3. `@save_to_dict` - Stores function output in a dictionary.
4. `@retry` - Retries a function multiple times upon failure.

### **🔹 Using Custom Decorators**
Demonstrating real-world use cases of our decorators on API calls, data processing, and error handling.

### **🔹 Built-in Python Decorators**
- `@property`, `@classmethod`, `@staticmethod`
- `@lru_cache` (for caching expensive functions)
- `@dataclass` (for data handling)
- `@abstractmethod` (enforcing abstraction in OOP)

---

## **2️⃣ Understanding Generators**
### **🔹 What Are Generators?**
Generators provide a **memory-efficient way** to iterate over large datasets by yielding items **lazily** instead of storing them in memory.

### **🔹 Custom Generators Implemented**
1. **Chunking a list** (`yield` list slices for batch processing).
2. **API Pagination Generator** (fetches results lazily from paginated APIs).
3. **Streaming Large Files** (reads file line-by-line instead of loading the entire file into memory).
4. **Countdown Generator** (simulates real-time countdown).

### **🔹 Using Custom Generators**
Show how these generators can be used to optimize API responses, data streaming, and processing large files efficiently.

### **🔹 Built-in Python Generators**
- `range()`, `enumerate()`, `zip()`, `map()`, `filter()`, `iter()`, `reversed()`, `open()` (reading files lazily).

---

## **3️⃣ Understanding Concurrency in Python**
### **🔹 CPU-Bound vs. I/O-Bound Tasks**
- **CPU-bound** tasks require heavy computations and are best handled by `multiprocessing`.
- **I/O-bound** tasks (file reading, API calls) benefit from `asyncio` and `multithreading`.

### **🔹 Comparison: CPU-Bound Tasks**
Demonstrating the performance difference between:
1. **Single-threaded execution**
2. **Multithreading** (ineffective due to GIL)
3. **Multiprocessing** (best choice for CPU-bound workloads)

### **🔹 Handling I/O-Bound Tasks**
Examples of using **multithreading, multiprocessing, and asyncio** for:
- **Reading multiple files** concurrently.
- **Fetching API data** efficiently.

### **🔹 Power of Async in FastAPI**
- Show how `async def` and `await` in **FastAPI** improve API responsiveness.
- Compare async handling in **Python vs. JavaScript & NodeJS**.

---

## **4️⃣ Understanding Dependency Injection (DI)**
### **🔹 Why DI Matters?**
- Helps manage **resource creation** efficiently.
- Improves **testability** by allowing easy dependency replacement.
- Promotes **loosely coupled code**.

### **🔹 Example: API Client and Data Handler**
- Implementing an API client that fetches data from external sources.
- Using DI to make it **testable and extendable**.

### **🔹 Writing Unit Tests with Mocking & Fixtures**
- **Mocking API responses** for test isolation.
- Using **pytest fixtures** to inject dependencies.

---

## **5️⃣ Understanding Design Patterns**
### **🔹 Why Use Design Patterns?**
- Improve **code reusability and scalability**.
- Ensure a **structured approach** to software design.

### **🔹 Factory Pattern Example**
- Demonstrating how **inheritance and code reuse** make factories efficient.
- Implementing a **ParserFactory** for parsing **PDF, TXT, and HTML** files.

### **🔹 Strategy Pattern Example**
- Implementing a **model evaluation system** where different evaluation metrics (accuracy, precision, recall) are selected dynamically.

---

## **6️⃣ Understanding Anti-Patterns in Python**
### **🔹 Common Anti-Patterns and Fixes**
1. **Mutable default arguments** → Use `None` and initialize inside function.
2. **Using `apply()` in Pandas instead of vectorized operations** → Use built-in functions.
3. **Appending to lists inside loops** → Use `list.append()` outside loops, then `pd.concat()`.
4. **Catching generic `Exception`** → Catch specific exceptions (`ValueError`, `TypeError`).
5. **Creating instances inside methods** → Use dependency injection instead.

---

## **7️⃣ Logger Initialization and Usage**
### **🔹 Setting Up a Python Logger**
- Initializing a logger with different logging levels (`INFO`, `DEBUG`, `WARNING`, `ERROR`).
- Configuring log format and saving logs to a file.

### **🔹 Using the Logger in Applications**
- Logging API responses and request times.
- Logging model training statistics in machine learning pipelines.
- Handling error logging with `@log_exceptions` decorator.

---

## **🚀 Conclusion**
This session provides a comprehensive understanding of **Python's advanced features**, improving:
- **Performance** (generators, concurrency, caching)
- **Code structure** (decorators, DI, design patterns)
- **Scalability & maintainability** (anti-pattern fixes, logging, OOP best practices)


