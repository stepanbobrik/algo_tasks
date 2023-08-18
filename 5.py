class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def path(root):
    ans = []
    l = 0
    q = [root]
    while l<len(q):
        if not q[l]:
            l+=1
            continue
        ans.append(q[l].val)
        q.append(q[l].left)
        q.append(q[l].right)
        l+=1
    return ans

