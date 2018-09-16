class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # i = 0
        # j = 1
        # Max = 1
        # maxTemp = 1
        # lens = len(s)
        #
        # if lens == 0:
        #     return 0
        #
        # while j < lens:
        #     while ((s[i:j]).__contains__(s[j]) == False):
        #         j = j + 1
        #         maxTemp = maxTemp + 1
        #
        #         if j>=lens:
        #             if maxTemp>Max:
        #                 return maxTemp
        #             else:
        #                 return Max
        #
        #     if maxTemp > Max:
        #         Max = maxTemp
        #
        #     if j>=lens-1:
        #         return Max
        #
        #     while (s[i: j]).__contains__(s[j]):
        #         i = i + 1
        #         maxTemp = maxTemp - 1
        #
        #     j=j+1
        #
        # return Max

        i=0
        j=0
        Max =0
        maxTemp =0
        lens =len(s)

        while j<lens:
            while (s[i:j]).__contains__(s[j])==False:
                j=j+1
                maxTemp=maxTemp+1

                if Max < maxTemp:
                    Max = maxTemp

                if j == lens:
                    return Max

            while (s[i:j]).__contains__(s[j]):
                i=i+1
                maxTemp=maxTemp-1

        return Max




if __name__ == '__main__':
    solu =Solution()
    print(solu.lengthOfLongestSubstring("qwertyuiop"))