from collections import defaultdict
from typing import List


class SolutionA:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        Exceeds time limit
        """
        plist = defaultdict(list)
        desc = [kill]

        def descendants(pid):
            nonlocal plist, desc
            ans = []
            if pid in plist:
                ps = plist[pid]
                for p in ps:
                    if p not in desc:
                        ds = [d for d in descendants(p) if d not in desc]
                        desc = desc + [p] + ds
                        ans += ds
            return ans

        for i, parent in enumerate(ppid):
            plist[parent].append(pid[i])
        _ = descendants(kill)
        return desc


from collections import defaultdict


class SolutionB:
    def killProcess(self, pid, ppid, kill):
        # Create a defaultdict to store the parent-child relationships
        map = defaultdict(list)

        # Iterate through the ppid list
        for i, parent in enumerate(ppid):
            # Check if the parent id is greater than 0 (not the root process)
            if parent > 0:
                # Add the current process id as a child of the parent
                map[parent].append(pid[i])

        # Create a list to store the killed processes, starting with the initial kill process
        killed_processes = [kill]

        # Recursively traverse the child processes and add them to the killed_processes list
        self.get_all_children(map, killed_processes, kill)

        # Return the final list of killed processes
        return killed_processes

    # Helper function to recursively get all children of a given process
    def get_all_children(self, map, killed_processes, kill):
        # Check if the process has any children in the map
        if kill in map:
            # Iterate through the children and add them to the killed_processes list
            for child_id in map[kill]:
                killed_processes.append(child_id)
                # Recursively call get_all_children to get all children of the current child process
                self.get_all_children(map, killed_processes, child_id)


class SolutionC:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parent = defaultdict(int)
        n = len(pid)
        # 建立并查集 O(n)
        for i in range(n):
            parent[pid[i]] = ppid[i]
        # 设置被杀进程的父节点为 -1
        parent[kill] = -1
        ans = []
        for i in parent:
            r = i
            # 寻找每个节点的父节点
            while r != 0 and r != -1:
                r = parent[r]
            # 父节点被杀，所以当前节点也被杀了
            if r == -1:
                ans.append(i)
        return ans


from collections import defaultdict, deque


class SolutionD:
    def killProcess(self, pid, ppid, kill):
        # Create a defaultdict to store the parent-child relationships
        map = defaultdict(list)

        # Iterate through the ppid list
        for i in range(len(ppid)):
            # Check if the parent id is greater than 0 (not the root process)
            if ppid[i] > 0:
                # Add the current process id as a child of the parent
                map[ppid[i]].append(pid[i])

        # Create a deque to perform breadth-first search
        queue = deque()
        # Create a list to store the killed processes
        killed_processes = []

        # Add the initial kill process to the queue
        queue.append(kill)

        # Perform breadth-first search to traverse the child processes
        while queue:
            # Remove the front element from the queue
            current_process = queue.popleft()
            # Add the current process to the killed_processes list
            killed_processes.append(current_process)
            # Check if the current process has any children in the map
            if current_process in map:
                # Iterate through the children and add them to the queue
                for child_id in map[current_process]:
                    queue.append(child_id)

        # Return the final list of killed processes
        return killed_processes


from collections import defaultdict


class SolutionE:
    def killProcess(self, pid, ppid, kill):
        # Create a defaultdict to store the parent-child relationships
        parent = defaultdict(int)

        # Build the parent-child relationships
        for i in range(len(pid)):
            parent[pid[i]] = ppid[i]

        # Set the parent node of the kill process to -1
        parent[kill] = -1

        # Find the killed processes by checking parent nodes
        killed_processes = [i for i in parent if self.is_killed(parent, i)]

        # Return the final list of killed processes
        return killed_processes

    def is_killed(self, parent, process):
        # Check if the process or its ancestor is killed
        while process != 0 and process != -1:
            process = parent[process]
        return process == -1
