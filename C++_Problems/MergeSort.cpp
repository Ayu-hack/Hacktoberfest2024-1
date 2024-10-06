#include <bits/stdc++.h>
using namespace std;

void combine(vector<int>& data, int start, int mid, int end) {
    int size1 = mid - start + 1;
    int size2 = end - mid;

    vector<int> left(size1), right(size2);

    for (int i = 0; i < size1; i++)
        left[i] = data[start + i];
    for (int j = 0; j < size2; j++)
        right[j] = data[mid + 1 + j];

    int i = 0, j = 0, k = start;

    while (i < size1 && j < size2) {
        if (left[i] <= right[j]) {
            data[k] = left[i];
            i++;
        } else {
            data[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < size1) {
        data[k] = left[i];
        i++;
        k++;
    }

    while (j < size2) {
        data[k] = right[j];
        j++;
        k++;
    }
}

void sortAndMerge(vector<int>& data, int start, int end) {
    if (start >= end)
        return;

    int mid = start + (end - start) / 2;
    sortAndMerge(data, start, mid);
    sortAndMerge(data, mid + 1, end);
    combine(data, start, mid, end);
}

void displayVector(vector<int>& data) {
    for (int i = 0; i < data.size(); i++)
        cout << data[i] << " ";
    cout << endl;
}
