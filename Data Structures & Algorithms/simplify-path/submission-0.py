class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0

        while i < len(path):
            if path[i] == "/":
                i += 1
                continue

            count = i
            while i < len(path) and path[i] != "/":
                i += 1

            directory = path[count:i]

            if directory == "..":
                if stack:
                    stack.pop()
            elif directory != ".":
                stack.append(directory)

        return "/" + "/".join(stack)