'''
769. Max Chunks To Make Sorted

You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

 

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
Example 2:

Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.
 

Constraints:

n == arr.length
1 <= n <= 10
0 <= arr[i] < n
All the elements of arr are unique.
'''

'''
Intution: If the num is not equal to the index, then reordering is required, hence it will need to be part of a chunk.
When the largest value in the chunk matches the index, we'll eventually add one to the number of chunks. This works because integers are in the range [0, n - 1].
'''
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_in_chunk = -1
        
        for idx, num in enumerate(arr):
            max_in_chunk = max(max_in_chunk, num)
            if max_in_chunk == idx:
                chunks += 1
        return chunks

