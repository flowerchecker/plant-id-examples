#include<iostream>
using namespace std;
struct Node{
	int coeff;
	int power;
	Node* next;
};
Node* addNode(Node* n, int c, int p) {
	Node* newNode = new Node();
	newNode->coeff = c;
	newNode->power = p;
	newNode->next = NULL;
	if (!n)return newNode;
	Node* pt = n;
	while(pt->next != NULL) {
		pt = pt->next;
	}
	pt->next = newNode;

	return n;
}
void printPolynomial(Node* n) {
	while (n->next) {
		cout << n->coeff << "x^" << n->power << "+";
		n = n->next;
	}
	cout << n->coeff << "\n";
}

void removeduplicate(Node* a) {
	Node* p1, * p2, * dup;
	p1 = a;
	while (p1 && p1->next)
	{
		p2 = p1;
		while (p2->next) {
			if (p1->power == p2->next->power) {
				p1->coeff = p1->coeff + p2->next->coeff;
				dup = p2->next;
				p2->next = p2->next->next;
				delete(dup);
			}
			else
				p2 = p2->next;
		}

		p1 = p1->next;

	}
}


Node* multiply(Node* a, Node* b, Node* c) {
	Node* p1, * p2;
	p1 = a;
	p2 = b;
	while (p1)
	{
		while (p2)
		{
			int co, po;

			co = p1->coeff * p2->coeff;
			po = p1->power + p2->power;
			c = addNode(c, co, po);

			p2 = p2->next;
		}
		p2 = b;
		p1 = p1->next;
	}

	removeduplicate(c);
	return c;
}

int main() {
	Node* poly1 = NULL; Node* poly2 = NULL; Node* poly3 = NULL;

	poly1 = addNode(poly1, 3, 2);
	poly1 = addNode(poly1, 5, 1);
	poly1 = addNode(poly1, 6, 0);

	poly2 = addNode(poly2, 6, 1);
	poly2 = addNode(poly2, 8, 0);

	cout << "1st Polynomial :";
	printPolynomial(poly1);
	cout << "2nd Polynomial :";
	printPolynomial(poly2);
	poly3 = multiply(poly1, poly2, poly3);
	cout << "resultant Polynomial : ";
	printPolynomial(poly3);
	return 0;

}
