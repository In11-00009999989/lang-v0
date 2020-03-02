operators = {
    "+": 2,
    "-": 2,
    "*": 2,
    "/": 2,
    "$": 1,
    "#": 1,
    "log": 1,
    "read_file": 1,
}

bad_chars = ["(", ")"]


class Node:
    def __init__(self, data):
        self.data = data
        self.nodes = []

    def PrintTree(self):
        print(self.data)


lineList = list()
with open("./program.ze") as f:
    for line in f:
        lineList.append(line)

for operations in lineList:

    test_string = "".join(i for i in operations if i not in bad_chars)

    arr_operations = operations.split(" ")

    filter(None, arr_operations)

    def construct_bin_tree(arr):
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

    tree, arr = construct_bin_tree(arr_operations)

    def calc(node: Node):
        if node.data == "+":
            return int(calc(node.nodes[0])) + int(calc(node.nodes[1]))

        if node.data == "-":
            return int(calc(node.nodes[0])) - int(calc(node.nodes[1]))

        if node.data == "*":
            return int(calc(node.nodes[0])) * int(calc(node.nodes[1]))

        if node.data == "/":
            return int(calc(node.nodes[0])) / int(calc(node.nodes[1]))

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

    calc(tree)
