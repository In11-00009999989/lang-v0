import math

operators = {
    "+": 2,
    "-": 2,
    "*": 2,
    "/": 2,
    "@": 1,
    "$": 1,
    "#": 1,
    "log": 1,
    "read_file": 1,
}


class Node:
    def __init__(self, data):
        self.data = data
        self.nodes = []

    def PrintTree(self):
        print(self.data)


def construct_bin_tree(arr: list) -> Node:
    if arr[0] not in operators:
        tmp = Node(arr[0])
        arr = arr[1:]

        return tmp, arr

    tmp = Node(arr[0])

    op = arr[0]
    arr = arr[1:]

    for i in range(operators[op]):
        tmpNode, arr = construct_bin_tree(arr)
        tmp.nodes.append(tmpNode)

    return tmp, arr


str = "+ - 0 3 - @ 100 90"

strr = str.split()
print(strr)

operations = [
    "+",
    "-",
    0,
    3,
    "-",
    "@",
    100,
    90,
]

node, arr = construct_bin_tree(operations)

# node = Node("+")
# node.nodes.append(Node(1))
# node.nodes.append(Node("-"))
# node.nodes[1].nodes.append(Node("@"))
# node.nodes[1].nodes[0].nodes.append(Node(100))
# node.nodes[1].nodes.append(Node(90))


def calc(node):
    if node.data == "+":
        return int(calc(node.nodes[0])) + int(calc(node.nodes[1]))
    if node.data == "-":
        return int(calc(node.nodes[0])) - int(calc(node.nodes[1]))
    if node.data == "*":
        return int(calc(node.nodes[0])) * int(calc(node.nodes[1]))
    if node.data == "/":
        return int(calc(node.nodes[0])) / int(calc(node.nodes[1]))
    if node.data == "@":
        return math.sqrt(int(calc(node.nodes[0])))

    if node.data == "$":
        return int(calc(node.nodes[0])) ** 2

    if node.data == "#":
        return int(calc(node.nodes[0])) ** 3

    if node.data == "log":
        return print(calc(node.nodes[0]))

    if node.data == "read_file":
        with open(calc(node.nodes[0]), "r") as f:
            print(f.read())

    return node.data


print(calc(node))
