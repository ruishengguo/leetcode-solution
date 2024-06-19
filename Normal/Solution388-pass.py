# 388、文件的最长绝对路径


class dir_tree:
    def __init__(self, depth, name):
        self.depth = depth
        self.name, self.real_name = name, name
        self.subclasses = []
        self.upper = None

    def get_subclasses(self, subclass):
        self.subclasses.append(subclass)
        subclass.name = self.name + '/' + subclass.name
        subclass.upper = self

    def get_upper_class(self):
        return self.upper

    def get_sub_dir(self):
        if not self.subclasses:
            if '.' in self.real_name:
                return [self.name]
            else:
                return ['\\']
        else:
            names = []
            for i in self.subclasses:
                names.extend(i.get_sub_dir())
            return names


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        all_dirs = input.split('\n')
        root = dir_tree(-1, '')
        cur = root
        for i in all_dirs:
            if '\t' not in i:
                cur = dir_tree(0, i)
                root.get_subclasses(cur)
            else:
                table = list(i).count('\t')
                new = dir_tree(table, i[table:])
                if table > cur.depth:
                    cur.get_subclasses(new)
                elif table == cur.depth:
                    cur.upper.get_subclasses(new)
                else:
                    up = cur.upper
                    while table <= up.depth:
                        up = up.upper
                    up.get_subclasses(new)
                cur = new
        max_ = 0
        for i in root.get_sub_dir():
            if len(i) > max_:
                max_ = len(i)
        return max_ - 1

