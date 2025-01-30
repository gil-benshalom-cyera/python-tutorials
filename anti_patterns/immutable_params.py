def add_item_wrong(item, items=[]):  # ❌ List persists across calls
    items.append(item)
    return items


def add_item_correct(item, items=None):
    if items is None:
        items = []  # ✅ Creates a new list each time
    items.append(item)
    return items


def test_add_item_correct():
    print(add_item_wrong("apple"))  # ['apple']
    print(add_item_wrong("banana"))  # ['apple', 'banana'] ❌ Unexpected!


def test_add_item_wrong():
    print(add_item_correct("apple"))  # ['apple']
    print(add_item_correct("banana"))  # ['banana'] ✅ Works correctly


def main():
    test_add_item_correct()
    test_add_item_wrong()


if __name__ == '__main__':
    main()
