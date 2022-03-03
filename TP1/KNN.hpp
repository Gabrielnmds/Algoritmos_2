#ifndef KNN_H
#define KNN_H

#include "KD_Tree.hpp"

//------------------Classe que monta arvore kd e calcula k-vizinhanca-----------------------//

class KNN
{
private:
    KD_Tree *kd_tree;              // arvore kd
    list<list<int>> priority_list; // lista dos k vizinhos mais proximos dos pontos do conjunto teste

public:
    void setTree(list<int *> T);                      // metodo para receber a arvore kd
    float distance(int a[2], int b[2]);               // metodo para calcular a distancia euclidiana entre dois pontos
    void k_NN(list<int> aux, int *x, Node *R, int k); // metodo para calcular os k vizinhos mais proximos
    void k_NN_all(list<int *> A, int k);              // metodo para calcular os k vizinhos mais proximos de um conjunto de pontos
};

#endif
