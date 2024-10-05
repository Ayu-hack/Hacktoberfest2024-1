#include <iostream>
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
  cout << "Enter the number of element:" << endl;
  cin >> n;

  int arr[n];
  inputArray(arr, n);

  // bubble sort
  int i, j, temp;
  for (i = (n - 1); i >= 0; i--)
  {
    for (j = 1; j <= i; j++)
    {
      if (arr[j - 1] > arr[j])
      {
        temp = arr[j - 1];
        arr[j - 1] = arr[j];
        arr[j] = temp;
      }
    }
  }

  // printing the sorted array
  cout << "Sorted array using Bubble Sort" << endl;
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }
}