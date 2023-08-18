class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
def path(root):
    ans = []
    def dfs(root:Node):
        if not root:
            return
        dfs(root.left)
        dfs(root.right)
        ans.append(root.val)
        return
    dfs(root)
    return ans


