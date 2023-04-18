#include <iostream>
#include <iomanip>
#include "mylib.h"

using namespace std;


void foo(int &a){
	a++;
}
int main()
{
	int a=10;
	int* aptr=&a;
	foo(a);
	cout<<a<<endl;
}

