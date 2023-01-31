#include <iostream>
#include<algorithm>
using namespace std;

int m, k;
char dp[5001];
short karr[21];



char check_win(int n) {
	if((n - karr[0]) < 0) {
		dp[n] = 0;
		return 0;
	}
	for(int i = 0; i < k; i++) {
		//cout << "n=" << n << "  karr[i]=" << karr[i] << "\n";
		if(n - karr[i] == 0) {
			dp[n] = 1;
			//cout << "return true because of case 1 at n=" << n << "\n";
			return 1;
		}
		else if(n - karr[i] < 0) {
			break;
		}
		else if(dp[n - karr[i]] == 0) {
			dp[n] = 1;
			//cout << "return true because of case 2 at n=" << n << "\n";
			return 1;
		}
	}
	dp[n] = 0;
	//cout << "return false because of case 3 at n=" << n << "\n";
	return 0;
}


int count_win(int m) {
	int result = 0;
	if(m>5000){
		for(int i = 1; i <= 5000;  i++) {
			if(!check_win(i)&&i<3000) {
				result++;
				//cout << i << "에서 추가\n";
			}
		}
		int cyclen = 1;  // cycle len
		for(int d = 2; d <= 2000; d++) {
			//cout << "주기=" <<d ;
			bool cylclebool = true;
			for(int i = 1000; i <= 3000; i++) {
				if(dp[i] != dp[i + d]) {
					cylclebool = false;
					//cout << "아님\n";
					break;
				}
			}
			if(cylclebool) {
				cyclen = max(cyclen, d);
				break;
			}
		}
		//cout << "최종주기="<<cyclen;
		int falsecntincycle = 0;
		for(int i = 1000; i < 1000 + cyclen; i++) {
			if(!dp[i]) falsecntincycle++;
		}
		//cout << "falsecntincycle="<< falsecntincycle;

		result += (int)((m - 3000) / cyclen) * falsecntincycle;
		for(int i = 3000; i <= 3000 + ((m - 3000) % cyclen); i++) {
			if(!dp[i]) result++;
		}
	}else{
		for(int i=1;i<m+1;i++){
			if(!check_win(i)) {
				result++;
				//cout << i << "에서 추가\n";
			}
		}
	}
	return result;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);


	cin >> m >> k;

	for(int i = 0; i < k; i++) {
		cin >> karr[i];
	}
	int result = count_win(m);
	cout << result;

}