#include <iostream>

#define MAX 5001

using namespace std;

int main() {
    float M[MAX][MAX];
    int i, j, n;
    float r;
    cin >> n;
    M[1][0] = 100;
    for (i = 1; i <= n ; i++) {
        for (j = 0; j <= i ; j++) {
            if (j == 0) {
                M[i + 1][j] =  M[i][j]/2;
            }else if (j == i){
                M[i + 1][j] = M[i][0]/2;
            }else{
                M[i + 1][j] = M[i][j]/2 + M[i][j - 1]/2;
            }
        }

    }
    r = M[n][n/2];
    cout.precision(2);
    cout << fixed << r << endl;

    return 0;
}
