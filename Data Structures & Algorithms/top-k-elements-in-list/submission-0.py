class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        sorted_dict_desc = sorted(count.items(), key = lambda item: item[1], reverse = True)
        kth = sorted_dict_desc[:k]
        for val in kth:
            order = [val[0] for val in kth]

        return order