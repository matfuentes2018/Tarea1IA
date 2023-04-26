#include <iostream>
#include <vector>
#include <unordered_set>
#include <ctime>
#include <cstdlib>

using namespace std;

struct Nodo{
    int val;
    vector<Nodo*> sucesores;

    Nodo(int v){
        val = v;
    }

    void addSucesor(Nodo* n){
        sucesores.push_back(n);
    }

    vector<Nodo*> getSucesores(){
        return sucesores;
    }
};

class Arbol{
public:
    Nodo* raiz;

    Arbol(Nodo* r){
        raiz = r;
    }

    void dfsRandom(Nodo* n, Nodo* goal, unordered_set<Nodo*>& visited, vector<Nodo*>& path, int& cost, int& expanded){
        visited.insert(n);
        expanded++;

        if(n == goal){
            path.push_back(n);
            return;
        }

        // Obtener sucesores
        vector<Nodo*> sucesores = n->getSucesores();

        // Escoger sucesor al azar
        int randomIdx = rand() % sucesores.size();
        Nodo* randomSucesor = sucesores[randomIdx];

        if(visited.count(randomSucesor) == 0){
            path.push_back(n);
            cost++;
            dfsRandom(randomSucesor, goal, visited, path, cost, expanded);
        } else {
            dfsRandom(n, goal, visited, path, cost, expanded);
        }
    }

    vector<Nodo*> dfsRandom(Nodo* start, Nodo* goal){
        unordered_set<Nodo*> visited;
        vector<Nodo*> path;
        int cost = 0;
        int expanded = 0;

        dfsRandom(start, goal, visited, path, cost, expanded);

        // Reverse the path
        reverse(path.begin(), path.end());

        // Print results
        cout << "camino encontrado: ";
        for(auto n : path){
            cout << n->val << " ";
        }
        cout << goal->val << endl;
        cout << "Costo: " << cost << endl;
        cout << "nodos expandidos: " << expanded << endl;

        return path;
    }
};
int main(){
    // Crear nodos
    Nodo* A = new Nodo(1);
    Nodo* B = new Nodo(2);
    Nodo* C = new Nodo(3);
    Nodo* D = new Nodo(4);
    Nodo* E = new Nodo(5);
    Nodo* F = new Nodo(6);
    Nodo* G = new Nodo(7);
    Nodo* H = new Nodo(8);

    // Agregar sucesores
    A->addSucesor(B);
    A->addSucesor(C);
    B->addSucesor(D);
    B->addSucesor(E);
    C->addSucesor(F);
    C->addSucesor(G);
    D->addSucesor(H);
    E->addSucesor(H);
    F->addSucesor(H);
    G->addSucesor(H);

    // Crear árbol con raíz en A
    Arbol arbol(A);

    // Buscar camino de A a H utilizando DFS (escogiendo sucesor al azar)
    srand(time(NULL));
    arbol.dfsRandom(A, H);

    return 0;
}