#include <bits/stdc++.h>
using namespace std;

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
  cout << "Enter the number of element in array:" << endl;
  cin >> n;

  int arr[n];
  inputArray(arr, n);

  // insertion sort
  for (int i = 1; i < n; i++)
  {
    int key = arr[i];
    int j = i - 1;

    while (j >= 0 && arr[j] > key)
    {
      arr[j + 1] = arr[j];
      j = j - 1;
    }
    arr[j + 1] = key;
  }

  // printing the sorted array
  cout << "Sorted array using Insertion sort algo" << endl;
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }
}