class Solution:
    def minMeetingRoomsA(self, intervals):
        # Check if the intervals list is empty
        if len(intervals) == 0:
            return 0

        # Create a new list of tuples to store the start and end times of each meeting
        meetings = []

        # Convert each interval in the input list to a tuple and add it to the meetings list
        for interval in intervals:
            meetings.append(
                (interval[0], 1)
            )  # 1 represents the start time of a meeting
            meetings.append(
                (interval[1], -1)
            )  # -1 represents the end time of a meeting

        # Sort the meetings list in ascending order based on the meeting times
        meetings.sort()

        cnt = 0  # Counter variable to keep track of the number of ongoing meetings
        maxValue = 0  # Variable to store the maximum number of simultaneous meetings

        # Iterate through the sorted meetings list
        for meeting in meetings:
            cnt += meeting[
                1
            ]  # Update the counter based on the start or end time of the meeting
            maxValue = max(maxValue, cnt)  # Update the maximum value if needed

        # Return the maximum number of simultaneous meetings
        return maxValue

    def minMeetingRoomsB(self, intervals):
        # Create a list to store the start and end times of each meeting
        meetings = []

        # Convert intervals to tuples and add them to the meetings list
        for start, end in intervals:
            meetings.append((start, 1))  # 1 represents the start time of a meeting
            meetings.append((end, -1))  # -1 represents the end time of a meeting

        # Sort the meetings list in ascending order based on the meeting times
        meetings.sort()

        cnt = 0  # Counter variable to keep track of the number of ongoing meetings
        max_rooms = 0  # Variable to store the maximum number of simultaneous meetings

        # Iterate through the sorted meetings list
        for _, delta in meetings:
            cnt += delta  # Update the counter based on the start or end time of the meeting
            max_rooms = max(max_rooms, cnt)  # Update the maximum value if needed

        # Return the maximum number of simultaneous meetings
        return max_rooms

    def minMeetingRoomsC(self, intervals: List[List[int]]) -> int:
        times: list[list[int]] = []
        for start, end in intervals:
            times.append([start, 1])
            times.append([end, -1])
        times.sort()
        res = cnt = 0
        for t in times:
            cnt += t[1]
            res = max(res, cnt)
        return res
