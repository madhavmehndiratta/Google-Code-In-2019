#include <bits/stdc++.h>
#define FIO(fname) freopen(fname,"w",stdout);
using namespace std;

default_random_engine generator;
uniform_int_distribution<int> distribution(1,101);
auto RAND = bind(distribution,generator);

int main(){
	FIO("data.txt")
	
	for(int i=0;i<500;i++){
		cout<<RAND()<<" ";
	}
	return 0;
}
