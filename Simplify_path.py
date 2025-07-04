class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split("/"):
            if i == "" or i == ".":
                continue
            if i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/" + "/".join(stack)


s = Solution()
print(s.simplifyPath("/a/./b/../../c/"))
print(s.simplifyPath("/home/"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/a/../../b/../c//.//"))
print(s.simplifyPath("home//foo/"))
print(s.simplifyPath("/.../b/c/./d/.."))
