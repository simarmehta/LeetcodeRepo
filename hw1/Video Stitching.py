class Solution(object):
    def videoStitching(self, clips, time):
        sorted_clips= sorted(clips,key=lambda x:(x[0],-x[1]))
        curr_end=0
        next_end=0
        count=0
        i=0
        n=len(clips)

        while i < n and curr_end<time:
            if sorted_clips[i][0]>curr_end:
                return -1

            while i < n and sorted_clips[i][0]<=curr_end:
                next_end = max(next_end, sorted_clips[i][1])
                i=i+1

            count=count+1
            curr_end=next_end

            if curr_end>=time:
                return count
        if curr_end<time:
            return -1
        else:
            return count


        """
        :type clips: List[List[int]]
        :type time: int
        :rtype: int
        """
        