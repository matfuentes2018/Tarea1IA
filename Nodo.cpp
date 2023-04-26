#include <iostream>
#include "Nodo.h"
using namespace std;

Nodo::Nodo(int valor){
    this -> valor = valor;
    izq = NULL;
    der = NULL;
}
