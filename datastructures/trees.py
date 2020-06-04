class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        current_node = self.root
        if current_node is None:
            self.root = new_node
            return self.root

        queue = [self.root]

        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = new_node
                return new_node

            if current.right is None:
                current.right = new_node
                return new_node

            queue.append(current.left)
            queue.append(current.right)



class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def insert(self, value):
        new_node = Node(value)

        current_node = self.root
        if current_node is None:
            self.root = new_node
            return self.root

        while current_node is not None:
            if value < current_node.info:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break


def pre_order(root):
    if root is not None:
        print(root.info, end=" ")
    if root.left is not None:
        pre_order(root.left)
    if root.right is not None:
        pre_order(root.right)


def in_order(root):
    if root is not None:
        if root.left is not None:
            in_order(root.left)
        print(root.info, end=" ")
        if root.right is not None:
            in_order(root.right)


def post_order(root):
    if root is not None:
        if root.left is not None:
            post_order(root.left)
        if root.right is not None:
            post_order(root.right)
        print(root.info, end=" ")


# height = no edges
def height(root):
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))


def create_bst_from_array(array):
    tree = BinarySearchTree()

    for element in array:
        tree.create(element)

    return tree


def create_bt_from_array(array):
    tree = BinaryTree()

    for element in array:
        tree.insert(element)

    return tree


def level_order(root):
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        print(current, end=" ")
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)


def in_order_max_aux(node, max_v):
    if node is not None:
        is_visible = node.info > max_v
        max_v = max(max_v, node.info)
        if is_visible:
            print(node.info, end=" ")
        in_order_max_aux(node.left, max_v)
        in_order_max_aux(node.right, max_v)


def in_order_max(root):
    in_order_max_aux(root, -9999)


def main():
    test_value = create_bst_from_array([1, 2, 5, 3, 6, 4])
    test_value2 = create_bst_from_array([4, 2, 3, 1, 7])
    test_valueBt = create_bt_from_array([5, 3, 10, 20, 21, 1])
    test_bt_custom = BinaryTree()
    test_bt_custom.root = Node(-10)
    test_bt_custom.root.right = Node(-15)
    test_bt_custom.root.right.right = Node(-1)
    in_order_max(test_bt_custom.root)

if __name__ == "__main__":
    main()
