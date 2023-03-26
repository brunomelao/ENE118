#ifndef CONTA_H
#define CONTA_H

class Robot
{
private: 
	
public://Podem ser acessados direto no main
    float id;
	float pos[2];
    float speed[2];
    void showPos();
    void move(float t);
    void changeSpeed(float, float)
};


#endif
