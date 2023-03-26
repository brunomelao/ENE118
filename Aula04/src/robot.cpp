#include <robot.h>
#include <iostream>
using namespace std;

void Robot:: showPos(){
    cout << "Posicao: " << this->pos[0] << " " << this->pos[1] << endl;
}
void Robot:: move(float t){
    this->pos[0] += this->speed[0]*t;
    this->pos[1] += this->speed[1]*t;
}
void Robot:: changeSpeed(float x, float y){
    this->speed[0] = x;
    this->speed[1] = y;
}