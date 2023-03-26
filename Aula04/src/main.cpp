#include "robot.h"
#include <iostream>
using namespace std;

int main()
{
	Robot r1,r2;
	r1.pos[0]=0;
	r1.pos[1]=0;
	r2.pos[0]=0;
	r2.pos[1]=0;
	cout<<"Digite a velocidade dos eixos x e y de r1 e r2:"<<endl;
	cin>>r1.speed[0]>>r1.speed[1]>>r2.speed[0]>>r2.speed[1];
	r1.showPos();
	r2.showPos();
	r1.move(1);
	r2.move(1);
	r1.showPos();
	r2.showPos();
}
