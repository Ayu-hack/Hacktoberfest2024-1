// finding the 2nd min element in the array
#include <iostream>
using namespace std;

int secondMinElement(int arr[], int n, int min)
{
  int secondMin = arr[0];

  for (int i = 1; i < n; i++)
  {
    if (arr[i] < secondMin && arr[i] > min)
    {
      secondMin = arr[i];
    }
  }

  return secondMin;
}

int minElement(int arr[], int n)
{
  int mini = arr[0];

  for (int i = 1; i < n; i++)
  {
    if (arr[i] < mini)
    {
      mini = arr[i];
    }
  }

  return mini;
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
  cout << "Enter the number of elements in array: " << endl;
  cin >> n;

  int arr[n];
  inputArray(arr, n);

  // min ELement in the array
  int minimum = minElement(arr, n);

  // Second Min Element in the array
  int secondMini = secondMinElement(arr, n, minimum);
  cout << "The 2nd Minimum element in the array: " << secondMini << endl;

  return 0;
}