/*
perguntar oa utilizador por 1 numeorp
separar os digitos num array
verificar se é palindorma 
imprimir o resultado 
*/



#include <iostream>
#
using namespace std;

int main() {

  int num[5];
  int num_in[5];


  cout << "Escreva 5 numeros  " << endl;

  //  guarda os numeros introdizidos 
  for (int i = 0; i < 5; ++i) {
    cin >> num[i];
  }

  cout << "Os numeros introduzidos são: " << endl;

  //  imprine os nunmeros 
  for (int n = 0; n < 5; ++n) {
    cout << num[n] << "  " ;
  }

  cout <<  "\n Os numeros introduzidos invertidos são: " << endl;

  // inverter o array 
  for (int m = 4; m >= 0; --m){
    cout << num[m]  << "  " ;
  }

  // separar os digitos 
 
  return 0;
}


