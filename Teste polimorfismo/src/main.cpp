#include <iostream>
class OPb{
    public:
    OPb(int v1, int v2):valor1(v1), valor2(v2){}
    virtual int operacao(){
        return valor1 + valor2;
    }
    protected:
    int valor1;
    int valor2;
};
class OPd:public OPb{
    public:
    OPd(int v1, int v2): OPb(v1,v2){}
    int operacao(){
        return valor1 * valor2;
    }
};

void ExecutaCalculo(OPb ob){
    std::cout << ob.operacao() << std::endl;
}
void ExecutaCalculo(OPb *ptr){
    std::cout << ptr->operacao() << std::endl;
}
int main(){
    OPb opb(3,5);
    OPd opd(7,9);
    ExecutaCalculo(opb);
    ExecutaCalculo(opd);
    ExecutaCalculo(&opb);
    ExecutaCalculo(&opd);
    return 0;
}