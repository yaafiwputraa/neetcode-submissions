class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)

        for num in nums :
            freq_map[num] += 1
        
        n = len(nums)
        bucket = [[] for _ in range (n+1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(n, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result