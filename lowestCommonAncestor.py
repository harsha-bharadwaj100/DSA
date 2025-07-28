class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None and right is None:
            return None
        if left is None and right is not None:
            return right
        if left is not None and right is None:
            return left
        return root


def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)


# Test
tree_list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
root = build_tree(tree_list)
sol = Solution()
p = find_node(root, 5)
q = find_node(root, 4)
print(sol.lowestCommonAncestor(root, p, q).val)  # Should print 5

p = find_node(root, 5)
q = find_node(root, 6)
print(sol.lowestCommonAncestor(root, p, q).val)  # Should print 3

p = find_node(root, 3)
q = find_node(root, 4)
print(sol.lowestCommonAncestor(root, p, q).val)  # Should print 3

p = find_node(root, 6)
q = find_node(root, 7)
print(sol.lowestCommonAncestor(root, p, q).val)  # Should print 5
