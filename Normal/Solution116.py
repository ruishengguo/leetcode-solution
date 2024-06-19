from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Left -> 0 Right -> 1
        def find_node(rt: 'Optional[Node]', path: str) -> 'Optional[Node]':
            if path == '':
                return rt
            elif path[0] == '1':
                return find_node(rt.right, path[1:])
            else:
                return find_node(rt.left, path[1:])

        def bfs(base_rt: 'Optional[Node]', rt: 'Optional[Node]', path: str = '') -> None:
            if not rt:
                return
            elif '0' not in path:
                rt.next = None
                bfs(base_rt, rt.left, path + '0')
                bfs(base_rt, rt.right, path + '1')
            else:
                temp = path
                new_path = ''
                for i in path[::-1]:
                    path = path[:-1]
                    if i == '0':
                        new_path = path + '1' + new_path
                        break
                    else:
                        new_path = '0' + new_path
                rt.next = find_node(base_rt, new_path)
                bfs(base_rt, rt.left, temp + '0')
                bfs(base_rt, rt.right, temp + '1')

        bfs(root, root)
        return root


s = Solution()
s.connect(Node(1, left=Node(2, left=Node(4), right=Node(5)), right=Node(3, left=Node(6), right=Node(7))))

