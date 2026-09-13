from collections import Counter, namedtuple, defaultdict, OrderedDict, deque, ChainMap

def print_counter():
    words = ["apple", "banana", "apple", "orange", "banana", "apple"]
    word_count = Counter(words)

    print(word_count)                # Counter({'apple': 3, 'banana': 2, 'orange': 1})
    print(word_count["apple"])       # 3
    print(word_count.most_common(2)) # [('apple', 3), ('banana', 2)]

def print_namedtuple():
    Point = namedtuple("Point", ["x", "y"])
    p1 = Point(10, 20)

    print(p1.x, p1.y)  # 10 20
    print(p1)  # Point(x=10, y=20)

def print_defaultdict():
    grouped = defaultdict(list)
    students = [("CS", "Alice"), ("Math", "Bob"), ("CS", "Charlie")]

    for department, name in students:
        grouped[department].append(name)

    print(grouped)  # defaultdict(<class 'list'>, {'CS': ['Alice', 'Charlie'], 'Math': ['Bob']})

def print_dict():
    od = OrderedDict()
    od["one"] = 1
    od["two"] = 2
    od["three"] = 3

    od.move_to_end("one")
    print(od)  # OrderedDict({'two': 2, 'three': 3, 'one': 1})

def print_deque():
    dq = deque([1, 2, 3])
    dq.appendleft(0)
    dq.append(4)
    print(dq)  # deque([0, 1, 2, 3, 4])

    dq.popleft()
    print(dq)  # deque([1, 2, 3, 4])

def print_ChainMap():
    defaults = {"theme": "dark", "language": "en"}
    user_settings = {"language": "fr"}

    combined = ChainMap(user_settings, defaults)
    print(combined["language"])  # fr (user_settings takes priority)
    print(combined["theme"])  # dark (falls back to defaults)