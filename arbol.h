#include <iostream>
#include "Nodo.h"
using namespace std;

class Arbol {
    public:
        Nodo* raiz;

        Arbol();
        void agregarNodo(int valor);
        void impInOrden(Nodo* nodo);
        void impPreOrden(Nodo* nodo);
        void impPostOrden(Nodo* nodo);
        Nodo* obtener_raiz();
        
};