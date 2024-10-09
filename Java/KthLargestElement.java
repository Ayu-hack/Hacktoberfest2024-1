import java.util.PriorityQueue;

public class KthLargestElement {

  // Function to find the Kth largest element using Min-Heap
  public static int findKthLargest(int[] nums, int k) {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>(k);
    for (int num : nums) {
      minHeap.add(num);
      if (minHeap.size() > k) {
        minHeap.poll();
      }
    }
    return minHeap.peek();
  }

  public static void main(String[] args) {
    int[] nums = { 3, 2, 1, 5, 6, 4 };
    int k = 2;

    // Find and print the Kth largest element
    int kthLargest = findKthLargest(nums, k);
    System.out.println("The " + k + "th largest element is: " + kthLargest);
  }
}
