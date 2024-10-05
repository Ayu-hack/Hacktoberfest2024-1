// finding the 2nd max element in the array
#include <iostream>
using namespace std;

int secondMaxElement(int arr[], int n, int max)
{
  int secondMax = arr[0];

  for (int i = 1; i < n; i++)
  {
    if (arr[i] > secondMax && arr[i] <= max)
    {
      secondMax = arr[i];
    }
  }

  return secondMax;
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
  cout << "Enter the number of elements in array: " << endl;
  cin >> n;

  int arr[n];
  inputArray(arr, n);

  // max ELement in the array
  int maximun = maxElement(arr, n);

  // Second Max Element in the array
  int secondMaxi = secondMaxElement(arr, n, maximun);
  cout << "The 2nd Maximum element in the array: " << secondMaxi << endl;

  return 0;
}