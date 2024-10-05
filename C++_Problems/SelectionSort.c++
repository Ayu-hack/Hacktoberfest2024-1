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
  cout << "Enter the number of element in array" << endl;
  cin >> n;

  int arr[n];
  inputArray(arr, n);

  // Selection Sort
  for (int i = 0; i < n - 1; i++)
  {
    int min_index = 1;

    for (int j = i + 1; j < n; j++)
    {
      if (arr[j] < arr[min_index])
      {
        min_index = j;
      }
    }

    if (min_index != i)
    {
      swap(arr[i], arr[min_index]);
    }
  }

  cout << "Sorted Array using selection sort algo" << endl;
  // printing sorted array
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }

  return 0;
}