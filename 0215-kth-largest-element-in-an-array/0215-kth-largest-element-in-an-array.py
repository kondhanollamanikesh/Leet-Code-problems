class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def heapify(arr,ind,n):
            largest_ind=ind
            left_child=(2*ind)+1
            right_child=(2*ind)+2
            if left_child<n and arr[left_child]>arr[largest_ind]:
                largest_ind=left_child
            if right_child<n and arr[right_child]>arr[largest_ind]:
                largest_ind=right_child
            if largest_ind!=ind:
                arr[largest_ind],arr[ind]=arr[ind],arr[largest_ind]
                heapify(arr,largest_ind,n)
        def heap_sort(nums1):
            n=len(nums1)
            for i in range(n//2 - 1,-1,-1):
                heapify(nums1,i,n)

            for last_index in range(n-1,0,-1):
                nums1[0],nums1[last_index]=nums1[last_index],nums1[0]
                heapify(nums1,0,last_index)
            return nums1
        heap_sort(nums)
        return nums[len(nums) - k]