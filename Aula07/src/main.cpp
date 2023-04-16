#include <iostream>
#include "sensorindustrial.h"
#include <string>
#include "medicao.h"
#include "sensorcomajuste.h"

using namespace std;
void foo(SensorIndustrial& s)
{
    s.imprimeDados();
}
int main(){
    Medicao meds[]={{"10:00::00", 10}, {"10:00::01", 11}, {"10:00::02", 12}, {"10:00::03", 13} ,{"10:00::04", 14},
    {"10:00::05", 15}, {"10:00::06", 16}, {"10:00::07", 17}, {"10:00::08", 18} ,{"10:00::09", 19}};

    int numMed = sizeof(meds)/sizeof(meds[0]);
    // SensorIndustrial si("S01V", "L/s");
    // si.lerDados(meds, numMed);

    SensorComAjuste sa("S02AJ", "L/s");
    sa.lerDados(meds, numMed);
    double coefs[] = {0.5,1.2};
    sa.setCoef(coefs, 2);
    
    // SensorIndustrial* sensores[]={&si, &sa};
    // for(int i=0; i<sizeof(sensores)/sizeof(sensores[0]);i++)
    // {
    //     sensores[i]->imprimeDados();
    // }
    //foo(si);
    foo(sa);
    return 0;
}