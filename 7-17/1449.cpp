#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int arr[1002];

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int N, L;
	cin >> N >> L;

	for (int i = 0; i < N; i++)
		cin >> arr[i];

	sort(arr, arr + N);

	int start = arr[0];
	int ans = 1;

	for (int i = 1; i < N; i++)
	{
		if (arr[i] - start + 1 > L)
		{
			ans++;
			start = arr[i];
		}
	}

	cout << ans;
}
