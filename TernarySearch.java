import java.util.Scanner;

public class TernarySearch {

    // Function to perform ternary search on a sorted array
    public static int ternarySearch(int[] arr, int left, int right, int key) {
        if (right >= left) {
            // Find the two mid points
            int mid1 = left + (right - left) / 3;
            int mid2 = right - (right - left) / 3;

            // Check if key is at any mid
            if (arr[mid1] == key) {
                return mid1;
            }
            if (arr[mid2] == key) {
                return mid2;
            }

            // Key lies in left one-third
            if (key < arr[mid1]) {
                return ternarySearch(arr, left, mid1 - 1, key);
            }
            // Key lies in right one-third
            else if (key > arr[mid2]) {
                return ternarySearch(arr, mid2 + 1, right, key);
            }
            // Key lies in middle one-third
            else {
                return ternarySearch(arr, mid1 + 1, mid2 - 1, key);
            }
        }

        // Key not found
        return -1;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Taking array input
        System.out.print("Enter the number of elements in the array: ");
        int n = scanner.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter the elements of the array in sorted order:");
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
        }

        // Taking the key input
        System.out.print("Enter the element to search for: ");
        int key = scanner.nextInt();
  
        // Performing ternary search
        int result = ternarySearch(arr, 0, arr.length - 1, key);

        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found in the array.");
        }

        scanner.close();
    }
}
 
    

