# 297、二叉树的序列化与反序列化
from setup import TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = []
        pile = [root]
        while True:
            new_pile = []
            end = True
            for i in pile:
                if isinstance(i, TreeNode):
                    res.append(i.val)
                    new_pile += [i.left, i.right]
                    end = False
                else:
                    res.append(None)
            if end:
                break
            pile = new_pile[:]
        while True:
            node = res.pop()
            if node is not None:
                res.append(node)
                break
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = list(map(lambda x: int(x) if x != 'None' and x != 'null' else None, ''.join(data[1:-1].split(' ')).split(',')))[::-1]
        pile = [TreeNode(data.pop())]
        cur = 0
        while data:
            l = data.pop()
            if data:
                r = data.pop()
            else:
                r = None
            if l is not None:
                l = TreeNode(l)
                pile.append(l)
            if r is not None:
                r = TreeNode(r)
                pile.append(r)
            pile[cur].left, pile[cur].right = l, r
            cur += 1
        return pile[0]
