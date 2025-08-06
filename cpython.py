class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1=version1.split('.')
        list2=version2.split('.')
        i,j=0,0
        while i<len(list1) or j < len(list2):
            v1=int(list1[i]) if i < len(list1) else 0 
            v2=int(list2[i]) if j < len(list2) else 0
            if v1 < v2:
                return -1
            if v1 > v2:
                return 1
            i+=1
            j+=1
        return 0

if __name__ == '__main__':
    sol = Solution()

    # 用例 1：正常不同版本
    print(sol.compareVersion("1.2.3", "1.2.4"))   # 期望输出 -1

    # 用例 2：长度不一致，后者更长
    print(sol.compareVersion("1.0", "1.0.0.1"))   # 期望输出 -1

    # 用例 3：前导零 & 相等
    print(sol.compareVersion("01.0.0", "1.0"))    # 期望输出 0