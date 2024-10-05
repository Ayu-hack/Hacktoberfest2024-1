#include <iostream>
using namespace std;

int main()
{
  int n; // entering the number of elements
  cout << "Enter the number of elements: " << endl;
  cin >> n;

  int arr[n]; // input the array
  cout << "Inputing the array\n";
  for (int i = 0; i < n; i++)
  {
    cin >> arr[i];
  }

  // printing before reversing
  cout << "Array Elements before reversing\n";
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }

  // reversing the array
  for (int i = 0; i < n / 2; i++)
  {
    swap(arr[i], arr[n - i - 1]);
  }
  cout << endl;
  // printing the reversed array
  cout << "Array Elements after reversing\n";
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }

  return 0;
}