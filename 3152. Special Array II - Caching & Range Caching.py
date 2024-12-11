'''
3152. Special Array II

An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
subarray
 nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

Example 1:

Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:

Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
'''

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        answers = []
        '''
        This allows us to know the answer is a Failure if
        the cached pair of indices is within the range of our from & to indices.
        '''
        cached_failures = set()
        '''
        If our from and to indices are within the successful from and to range then we know the answer is True
        '''
        smallest_successful_from = None
        largest_successful_to = None

        for q in queries:
            _from, _to = q[0], q[1]
            
            # Check if any failure indices are within the current range
            if any((_from <= idx1 <= _to and _from <= idx2 <= _to) for (idx1, idx2) in cached_failures):
                answers.append(False)
                continue  # Skip further checks for this query

            # Check if current range is within the largest successful range
            if smallest_successful_from is not None and largest_successful_to is not None:
                if smallest_successful_from <= _from and largest_successful_to >= _to:
                    answers.append(True)
                    continue

            # Check for alternating parity within the range    
            broke = False
            last = nums[_from] % 2
            for i in range(_from + 1, _to + 1):
                answer = nums[i] % 2
                if answer == last: # Same Parity = Failure
                    answers.append(False)
                    cached_failures.add((i - 1, i)) # Store the pair indices 
                    broke = True
                    break
                last = answer
            if not broke:
                answers.append(True)
                # Check if the max successful range can be extended
                if smallest_successful_from is None or (smallest_successful_from >= _from and smallest_successful_from <= _to):
                    smallest_successful_from = _from
                if largest_successful_to is None or (largest_successful_to <= _to and largest_successful_to >= _from ):
                    largest_successful_to = _to
    
        return answers