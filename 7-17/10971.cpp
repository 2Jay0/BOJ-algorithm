#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int W[11][11];
int arr[11];
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);

	int n;
	cin >> n;

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			cin >> W[i][j];

	for (int i = 1; i <= n; i++)
		arr[i] = i;

	int min_cost = 1e+9;

	do {
		int cost = 0;
		int flag = 0;
		
		for (int i = 1; i <= n - 1; i++) {
			if (W[arr[i]][arr[i + 1]] > 0) {
				cost += W[arr[i]][arr[i + 1]];
			}
			else {
				flag = 1;
				break;
			}
		}
		if (W[arr[n]][arr[1]] > 0)
			cost += W[arr[n]][arr[1]];
		else
			flag = 1;

		if (flag == 0) {
			min_cost = min(cost, min_cost);
		}
	} while (next_permutation(arr, arr + n));

	cout << min_cost;
}