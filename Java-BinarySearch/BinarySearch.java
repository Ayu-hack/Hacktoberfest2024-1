package com.omkar.BinarySearch;

public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = {2, 3, 4, 5, 12, 45, 45, 77, 85, 87, 88, 95, 99};
        int target = 45;
        int ans = binarySearch(arr, target);
        System.out.println(ans);
    }

    // return the index
    // return -1 if it does not exist
    static int binarySearch(int[] arr, int target) {
        int start = 0;
        int end = arr.length - 1;

        while (start <= end) {
            // find the middle element.

            // int mid = start + end / 2; // but it has problem which integer has fixed size. after some of the value,
            // you can't put value input as Integer. but might be possible that (start+end) exceeds the range of int in java.
            // better way to do those things
            int mid = start + (end - start) / 2;

            if (target < arr[mid]) {
                end = mid - 1;
            } else if (target > arr[mid]) {
                start = mid + 1;
            } else {
                // answer found
                return mid;
            }
        }
        return -1;
    }
}