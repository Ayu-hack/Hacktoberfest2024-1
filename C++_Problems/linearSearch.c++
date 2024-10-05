#include <iostream>
using namespace std;

bool linearSearch(int arr[], int n, int key)
{
  for (int i = 0; i < n; i++)
  {
    if (arr[i] == key)
    {
      return 1;
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

  bool isFound = linearSearch(arr, n, key);
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