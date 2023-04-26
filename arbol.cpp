#include <iostream>
#include "arbol.h"
using namespace std;

Arbol::Arbol(){
    raiz = NULL;
}

void Arbol::agregarNodo(int valor){
    Nodo* nuevo = new Nodo(valor);
    if(raiz == NULL){
        raiz = nuevo;
    }else{
        Nodo* actual = raiz;
        while(true){
            if(valor < actual->valor){
                if(actual->izq == NULL){
                    actual->izq = nuevo;
                    break;
                }else{
                    actual = actual->izq;
                }
            }else{
                if(actual->der == NULL){
                    actual->der = nuevo;
                    break;
                }else{
                    actual = actual->der;
                }
            }
        }
    }
}

void Arbol::impInOrden(Nodo* nodo) {
        if (nodo != NULL) {
            impInOrden(nodo->izq);
            cout << nodo->valor << " ";
            impInOrden(nodo->der);
        }
}

void impPreOrden(Nodo* nodo) {
        if (nodo != NULL) {
            cout << nodo->valor << " ";
            impPreOrden(nodo->izq);
            impPreOrden(nodo->der);
        }
}

 void impPostOrden(Nodo* nodo) {
        if (nodo != NULL) {
            impPostOrden(nodo->izq);
            impPostOrden(nodo->der);
            cout << nodo->valor << " ";
        }
}

Nodo Arbol::obtener_raiz(){
    return raiz;
}