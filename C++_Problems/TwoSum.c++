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
  cout << "Enter the number of elements in array:" << endl;
  cin >> n;

  int arr[n];
  inputArray(arr, n);

  int target;
  cout << "Enter the target:" << endl;
  cin >> target;

  int index1 = -1, index2 = -1;
  for (int i = 0; i < n - 1; i++)
  {
    for (int j = i + 1; j < n; j++)
    {
      if (arr[i] + arr[j] == target)
      {
        index1 = i;
        index2 = j;
        break;
      }
    }
  }

  cout << "The two element are at indexs: " << index1 << " " << index2 << endl;
}