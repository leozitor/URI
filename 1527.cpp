#include <iostream>
#include <vector>

class Node;

class Node
{
public:
	int wins;
	int pontos;
	std::vector<Node>::iterator parent, myIterator;
	int rank;
	bool player0;

	Node(int ponto) : wins{ 0 }, rank { 0 }, player0 { false }
	{
		pontos = ponto;
	}

	void setParent(std::vector<Node>::iterator it)
	{
		parent = it;
		myIterator = it;
	}

	std::vector<Node>::iterator findSet()
	{
		if (parent != myIterator)
			parent = parent->findSet();
		return parent;
	}

};

void link(std::vector<Node>::iterator x, std::vector<Node>::iterator y)
{
	if (x->rank > y->rank)
	{
		y->parent = x->myIterator;
		x->pontos = x->pontos + y->pontos;
		if (y->player0)
			x->wins = y->wins;
	}
	else
	{
		x->parent = y->myIterator;
		y->pontos = x->pontos + y->pontos;
		if (x->rank == y->rank)
			y->rank = y->rank + 1;
		if (x->player0)
			y->wins = x->wins;
	}
}

void uniao(Node *x, Node *y)
{
	link(x->findSet(), y->findSet());
}

int main()
{
	int n, m, pontosJogador, q, a, b;

	while (true)
	{
		std::vector<Node> players;
		std::cin >> n >> m;
		if (n != 0 && m != 0)
		{
			for (int i = 0; i < n; i++)
			{
				std::cin >> pontosJogador;
				Node *newPlayer = new Node(pontosJogador);
				players.push_back(*newPlayer);
			}
			for (std::vector<Node>::iterator aux = players.begin(); aux != players.end(); ++aux)
			{
				aux->setParent(aux);
			}
			players[0].player0 = true;
			for (int i = 0; i < m; i++)
			{
				std::cin >> q >> a >> b;
				if (q == 1)
				{
					if(b < a)
						uniao(&players[a - 1], &players[b - 1]);
					else
						uniao(&players[b - 1], &players[a - 1]);
				}
				else if (q == 2)
				{
					if (players[a - 1].findSet()->pontos > players[b - 1].findSet()->pontos)
					{
						players[a - 1].findSet()->wins++;
					}
					else if (players[a - 1].findSet()->pontos < players[b - 1].findSet()->pontos)
					{
						players[b - 1].findSet()->wins++;
					}
				}
			}

			std::cout << players[0].findSet()->wins << std::endl;
		}
		else
			break;
	}
	return 0;
}
