#include "KNN.hpp"

void KNN::setTree(list<int *> T)
{
    KD_Tree *temp = new KD_Tree;
    Node *root = new Node;
    temp->newTree(root);
    root = temp->build_KDtree(T, 0);
}

float KNN::distance(int a[2], int b[2])
{
    float dist = sqrt((a[0] - b[0]) ^ 2 + (a[1] + b[1]) ^ 2);
    return dist;
}

void KNN::k_NN(list<int> aux, int *x, Node *R, int k)
{
    int *p_2;
    if (R == NULL)
        return;
    else if (R->isLeaf())
    {
        p_2 = R->getPoint();
        aux.push_back(distance(x, p_2));
    }
    else
    {
        if (aux.size() == k)
        {
            p_2 = R->getPoint();
            aux.pop_back();
            aux.push_back(distance(x, p_2));
            aux.sort();
            k_NN(aux, x, R->getLeft());
            k_NN(aux, x, R->getRight());
        }
        else
        {
            p_2 = R->getPoint();
            aux.push_back(distance(x, p_2));
            aux.sort();
            k_NN(aux, x, R->getLeft());
            k_NN(aux, x, R->getRight());
        }
    }
    priority_list.push_back(aux);
}

void KNN::k_NN_all(list<int *> A, int k)
{
    list<int *>::iterator it;
    list<int> aux;
    for (it = A.begin(); it != A.end(); ++it)
        k_NN(aux, *it, kd_tree->root, k);
}
