class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        course = {}
        for a, b in prerequisites:
            course.setdefault(b, []).append(a)
        visit = set()
        trace = set()
        
        def dfs(i):
            if i in trace:
                return False
            if i in visit:
                return True
            
            trace.add(i)
            for y in course.get(i,[]):
                if not dfs(y):
                    return False
            trace.remove(i)
            visit.add(i)
            
            return True
        
        for x in list(course):
            if not dfs(x):
                return False
        return True