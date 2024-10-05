#include <iostream>
using namespace std;

int minElement(int arr[], int n)
{
  int min = arr[0];

  for (int i = 1; i < n; i++)
  {
    if (arr[i] < min)
    {
      min = arr[i];
    }
  }

  return min;
}

int maxElement(int arr[], int n)
{
  int max = arr[0];

  for (int i = 1; i < n; i++)
  {
    if (arr[i] > max)
    {
      max = arr[i];
    }
  }

  return max;
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
  cout << "Enter the number of elements: " << endl;
  cin >> n;

  // inputing the array
  int arr[n];
  inputArray(arr, n);

  // maximum element in the array
  int maximun = maxElement(arr, n);

  // minimum element in the array
  int minimum = minElement(arr, n);

  cout << "The max element and Min element in the array are:" << maximun << " " << minimum << endl;
  return 0;
}