#ifndef KDTREE_H
#define KDTREE_H

#include <stdlib.h>
#include <iostream>
#include <vector>
#include <list>

using namespace std;

//-----------------Classe auxiliar node para armazenar os pontos na arvore-------------------//

class Node
{
private:
    int k = 0;   // dimensao dos pontos da arvore
    int *point;  // vetor contendo as coordenadas do ponto armazenado no node
    Node *left;  // ponteiro para o node filho da esquerda
    Node *right; // pontteiro para o node filho da direita

public:
    void newNode(int n);        // construtor que recebe a dimensao do espaco e atribui nulo para os nodes filhos
    int *getPoint();            // metodo que retorna as coordenadas do ponto
    void setPoint(int *points); // metodo que atribui as coordenadas do ponto armazenado no node
    bool isLeftNull();          // metodo que checa se existe filho a esquerda
    bool isRightNull();         // metodo que checa se existe filho a direita
    Node *getLeft();            // metodo que retorna o filho a esquerda
    Node *getRight();           // metodo que retorna o filho a direita
    void setLeft(Node *l);      // metodo que insere um node a esquerda
    void setRight(Node *r);     // metodo que insere um node a direita
    bool isLeaf();              // metodo que checa se um node eh folha
};

//-----------------Classe arvore KD------------------//

class KD_Tree
{
public:
    Node *root = NULL;                                 // ponteiro para o node da raiz da arvore
    void newTree(Node *n);                             // contrutor da arvore que atribui um node a raiz
    Node *build_KDtree(list<int *> points, int depth); // metodo para contruir uma kd-tree com base num conjuntos de pontos
};

#endif
