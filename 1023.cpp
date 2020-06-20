#include <stdio.h>
#include <map>
#include <math.h>
using namespace std;
int main()
{
	map<int,int> d;
	int ci = 1, chaves[201];
	int i = 0, n;
	while(true)
	{
		scanf("%d", &n);
		if(n == 0)
			return 0;
		while(i< 201)
		{
			chaves[i] = 0;
			i++;
		}
		int x, y;
		unsigned long long habitantes = 0, gasto =0, total;
		int tam = 0, menor = -1, calc;
		i = 0;
		while(i < n)
		{
			scanf("%d %d", &x, &y);
			calc = y/x;
			if(calc < menor || menor == -1)
				menor = calc;
			habitantes += x;
			gasto += y;
			if(d.count(calc) > 0)
				d[calc] += x;
			else
			{
				tam += 1;
				chaves[calc] = 1;
				d[calc] = x;
			}
			i++;
		}
		if(ci > 1)
			printf("\n");
		printf("Cidade# %d:\n", ci);
		int contador = 0;
		while(menor < 201 && contador < tam-1)
		{		
			if(chaves[menor] == 0)
			{
				menor++;
				continue;
			}
			printf("%d-%d ", d[menor], menor);
			chaves[menor] = 0;
			contador++;
			menor++;
		}
		menor--;
		while(menor < 201)
		{
			if(chaves[menor] == 0)
			{
				menor++;
				continue;
			}
			printf("%d-%d\n", d[menor], menor);
			chaves[menor] = 0;
			break;
		}
	    unsigned long long result = 100*((double)gasto/habitantes);
	    printf("Consumo medio: %llu.%02llu m3.\n", result/100, result%100);
		ci++;
		d.clear();
	}
}
