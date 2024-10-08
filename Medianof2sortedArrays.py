def findMedianSortedArrays(nums1, nums2):
        n1,n2=len(nums1),len(nums2)
        if n1>n2:
            return findMedianSortedArrays(nums2,nums1)
        left=(n1+n2+1)//2
        low,high=0,n1
        while low<=high:
            mid1=(low+high)//2
            mid2=left-mid1
            l1,l2=float('-inf'),float('-inf')
            r1,r2=float('inf'),float('inf')
            if mid1<n1:
                r1=nums1[mid1]
            if mid2<n2:
                r2=nums2[mid2]
            if mid1-1>=0:
                l1=nums1[mid1-1]
            if mid2-1>=0:
                l2=nums2[mid2-1]
            if l1<=r2 and l2<=r1:
                if (n1+n2)%2!=0:
                    return max(l1,l2)
                else:
                    return ((max(l1,l2)+min(r1,r2))/2)
            elif l1>r2:
                high=mid1-1
            elif l2>r1:
                low=mid1+1
        return 0
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
print("The median of the sorted arrays is:",findMedianSortedArrays(nums1,nums2))