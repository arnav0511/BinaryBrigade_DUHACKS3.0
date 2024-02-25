#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    cout<<"-----------DIELECTRIC CONSTANT - CURIE TEMPERATURE-----------\n"<<endl;
    cout<<"AIM: "<<endl;;
    cout<<"To study the variation of dielectric constant with temperature and to find the Curie’s temperature of the given sample.\n"<<endl;
    cout<<"APPARATUS USED: \nSample of barium titanate (BaTiO3) \nApparatus that includes probe arrangement \nSample \nOven \nOven controller \nDigital capacitance meter\n"<<endl;
    cout<<"FORMULA USED: "<<endl;
    cout<<"The value of the dielectric constant E, of the barium titanate sample is given by: "<<endl;
    cout<<"E = C/C1"<<endl;
    cout<<"where, C and C1 are capacitance with and without the dielectric in between the plates.\n"<<endl;

    cout<<"------NOW IT's TIME FOR THE OBSERVATIONS------"<<endl;
    cout<<"Input observations (Temperature in celsius and Capacitance in pF)"<<endl;
    float temp[20];
	float capa[20];
	float dconst[20];
	for(int i=0;i<20;i++){
    cout<<"Enter temperature: ";
    cin>>temp[i];
    cout<<"Enter capacitance for the given temperature: ";
    cin>>capa[i];
    dconst[i]=capa[i]/(0.0299);
    //cout<<"Dielectric constant: "<<dconst[i]<<endl<<endl;
    }
	cout<<"Observations (as input) : "<<endl;
    cout<<"Temperature(C) | Capacitance(pF) | Dielectric constant"<<endl;
    for(int j=0;j<7;j++){
    cout<<temp[j]<<"             | "<<capa[j]<<"              | "<<dconst[j]<<endl;
    }
    for(int j=8;j<20;j++){
    cout<<temp[j]<<"            | "<<capa[j]<<"             | "<<dconst[j]<<endl;
    }
    float max = *max_element(dconst, dconst+20);
	int x;
	for (int i = 0; i < 20; i++) {
	    if(dconst[i]==max){
	        x = i;
	        break;
	    }
	}
	cout<<"Maximum dielectric constant is : "<<dconst[x]<<endl;
	cout<<"Temperature with maximum dielectric constant : "<<temp[x]<<endl;

    cout<<"Result:"<<endl<<"The curie temperature is "<<temp[x];

    return 0;
}
