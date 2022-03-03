#include "KD_Tree.hpp"

using namespace std;

//---------------------Metodos da classe node-----------------------//

void Node::newNode(int n)
{
    k = n;
    point = (int *)malloc(k * sizeof(int));
    left = NULL;
    right = NULL;
}

int *Node::getPoint()
{
    return point;
}

void Node::setPoint(int *cordinates)
{
    for (int i = 0; i < (sizeof(cordinates) / sizeof(*cordinates)); i++)
    {
        point[i] = cordinates[i];
    }
}

bool isLeftNull()
{
    if (left == NULL)
        return true;
    else
        return false;
}

bool isRightNull()
{
    if (right == NULL)
        return true;
    else
        return false;
}

Node *Node::getLeft()
{
    return left;
}

Node *Node::getRight()
{
    return right;
}

void Node::setLeft(Node *l)
{
    left = l;
}

void Node::setRight(Node *r)
{
    right = r;
}

bool Node::isLeaf()
{
    if (left == NULL && right == NULL)
        return true;
    else
        return false;
}

//---------------------Metodos da classe KD_Tree---------------------//

void KD_Tree::newTree(Node *n)
{
    root = n;
}

Node *KD_Tree::build_KDtree(list<int *> points, int depth)
{
    Node *temp = new Node;
    temp->newNode(2);
    temp->setPoint(points.front());
    list<int *> p_1;
    list<int *> p_2;
    if (points.front() == points.back())
        return temp;
    else
    {
        list<int *>::iterator it;
        if (depth % 2 == 0)
        {
            for (it = points.begin(); it != points.end(); ++it)
            {
                int *p = *it;
                int *q = temp->getPoint();
                if (p[0] <= q[0])
                    p_1.push_back(*it);
                else
                    p_2.push_back(*it);
            }
        }
        else
        {
            for (it = points.begin(); it != points.end(); ++it)
            {
                int *p = *it;
                int *q = temp->getPoint();
                if (p[1] <= q[1])
                    p_1.push_back(*it);
                else
                    p_2.push_back(*it);
            }
        }
    }
    temp->setLeft(build_KDtree(p_1, depth + 1));
    temp->setRight(build_KDtree(p_2, depth + 1));
    return temp;
}
