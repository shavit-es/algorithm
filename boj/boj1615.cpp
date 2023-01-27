#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;

ll sum(vector<ll>& tree, int i)
{
	ll ans = 0;
	while(i > 0)
	{
		ans += tree[i];
		i -= (i & -i);
	}

	return ans;
}

void update(vector<ll>& tree, int i)
{
	while(i < tree.size())
	{
		tree[i] += 1;
		i += (i & -i);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	cin >> n >> m;
	vector<vector<int>> v(m+1);

	for(int l = 0; l < m; l++) {
		int a, b;
		cin >> a >> b;
		v[a].push_back(b);
	}

	
	ll result = 0; // 정답
	ll count = 0; //탐색 횟수
	vector<ll> tree(n + 1);

	for(int i=1; i<= n; i++){
		sort(v[i].begin(), v[i].end());
		int v_size = v[i].size();
		for(int k = 0; k < v_size; k++) {
			update(tree, v[i][k]);
			result += count++ + 1 - sum(tree, v[i][k]);
		}
	}
	
	cout << result;
	return 0;
}
