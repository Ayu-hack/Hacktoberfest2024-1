#include <iostream>
using namespace std;

bool binarySearch(int arr[], int n, int key)
{
  int start = 0;
  int end = n - 1;
  int mid = (start + end) / 2;

  while (start <= end)
  {
    if (arr[mid] == key)
    {
      return 1;
    }
    if (arr[mid] > key)
    {
      start = mid + 1;
      mid = (start + end) / 2;
    }
    if (arr[mid] < key)
    {
      end = mid - 1;
      mid = (start + end) / 2;
    }
  }

  return -1;
}

void inputArray(int arr[], int n)
{
  for (int i = 0; i < n; i++)
  {
    cin >> arr[i];
  }
}

int main()
{
  int n;
  cout << "Enter the number of elements:" << endl;
  cin >> n;

  int arr[n];
  inputArray(arr, n);

  int key;
  cout << "Enter the key you want to search:" << endl;
  cin >> key;

  bool isFound = binarySearch(arr, n, key);
  if (isFound)
  {
    cout << "Element " << key << " is found" << endl;
  }
  else
  {
    cout << "Element does not exist" << endl;
  }

  return 0;
}