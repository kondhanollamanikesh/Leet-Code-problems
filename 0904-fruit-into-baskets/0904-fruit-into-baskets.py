class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxi=0
        left=0
        right=0
        my_dict={}
        while right<len(fruits):
            if fruits[right] not in my_dict:
                my_dict[fruits[right]]=0
            my_dict[fruits[right]]+=1
            if len(my_dict)>2:
                if my_dict[fruits[left]]>0:
                    my_dict[fruits[left]]-=1
                if my_dict[fruits[left]]==0:
                    del my_dict[fruits[left]]
                left+=1
            if len(my_dict)<=2:
                maxi=max(maxi,right-left+1)
            right+=1
        return maxi

