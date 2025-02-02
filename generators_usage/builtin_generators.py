def generate_enumerate(iterable):
    """Generator using enumerate() - iterates with an index."""
    return enumerate(iterable)  # ✅ Returns an iterator


def generate_zip(iter1, iter2):
    """Generator using zip() - iterates over multiple iterables in parallel."""
    return zip(iter1, iter2)  # ✅ Returns an iterator


def generate_map(func, iterable):
    """Generator using map() - lazily applies a function to an iterable."""
    return map(func, iterable)  # ✅ Returns a generator


def generate_filter(func, iterable):
    """Generator using filter() - lazily filters elements."""
    return filter(func, iterable)  # ✅ Returns a generator


def generate_iter(iterable):
    """Generator using iter() - converts an iterable into an iterator."""
    return iter(iterable)  # ✅ Returns an iterator


def generate_reversed(iterable):
    """Generator using reversed() - lazily iterates in reverse order."""
    return reversed(iterable)  # ✅ Returns an iterator


def read_file_line_by_line(file_path):
    """Generator using open() - reads a file line-by-line."""
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()  # ✅ Yield each line lazily


def main():
    print("\n\n🔹 enumerate indexing Example:")
    try:
        generate_enumerate(["a", "b", "c"])[0]  # ❌ Error: 'enumerate' object is not subscriptable
    except TypeError as e:
        print(f"Error: {e}")

    print("\n\n🔹 enumerate() Example:")
    for index, letter in generate_enumerate(["a", "b", "c"]):
        print(f"{index}: {letter}")  # ✅ Indexed iteration

    print("\n🔹 zip() Example:")
    for pair in generate_zip(["Alice", "Bob"], [90, 80]):
        print(pair)  # ✅ ('Alice', 90), ('Bob', 80)

    print("\n🔹 map() Example:")
    for name in generate_map(str.upper, ["alice", "bob"]):
        print(name)  # ✅ ALICE, BOB

    print("\n🔹 filter() Example:")
    for num in generate_filter(lambda x: x % 2 == 0, range(10)):
        print(num, end=" ")  # ✅ 0 2 4 6 8

    print("\n\n🔹 iter() Example:")
    num_iter = generate_iter([10, 20, 30])
    print(next(num_iter))  # ✅ 10
    print(next(num_iter))  # ✅ 20

    print("\n🔹 reversed() Example:")
    for num in generate_reversed([1, 2, 3]):
        print(num, end=" ")  # ✅ 3 2 1

    print("\n\n🔹 open() Example (Requires a file):")
    # Uncomment and replace 'data.txt' with an actual file path
    # for line in read_file_line_by_line("data.txt"):
    #     print(line)


# 🎯 Running the Demonstrations
if __name__ == "__main__":
    main()
