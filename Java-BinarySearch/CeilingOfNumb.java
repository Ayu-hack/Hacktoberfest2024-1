package com.omkar.BinarySearch;
//Note: Before going to solve the question, read the theory from the notebook, once check it out.

public class CeilingOfNumb {
    public static void main(String[] args){
        int[] arr = {2, 3, 5, 9, 14, 16, 18};
        int target = 15;
        int ans = ceiling(arr, target);
        System.out.println(ans);
    }

    //ceiling -> the smallest element in the array which is greater than or equal to target. (smallest number >= target)
    static int ceiling(int[] arr, int target){

        //but what if the target is greater than the greatest number in the array
        if(target > arr[arr.length - 1]){
            return -1;
        }

        int start = 0;
        int end = arr.length -1;

        while(start <= end){
            int mid = start + (end - start) / 2;

            if(target > arr[mid]){
                start = mid + 1;
            } else if (target < arr[mid]) {
                end = mid - 1;
            } else{
                return mid;
            }
        }
        return start;
    }
}
