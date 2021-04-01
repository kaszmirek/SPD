#include "RandomNumberGenerator.h"
#include <iostream>

using namespace std;

int seed = 0;
int n;

int main()
{
    cout << "Wprowadz zrodlo losowania: ";
    cin >> seed;
    cout << endl
         << "Wprowadz rozmiar problemu: ";
    cin >> n;
    cout << endl;

    RandomNumberGenerator rng(seed);

    int j[n];
    int r[n]; // prepare time
    int p[n]; // process time
    int S[n]; // start time
    int C[n]; // finish time
    int A = 0;

    for (int i = 0; i < n; i++)
        p[i] = rng.nextInt(1, 29);

    for (int i = 0; i < n; i++)
        A += p[i]; // dodawanie do sumy kolejnego elementu

    for (int i = 0; i < n; i++)
        r[i] = rng.nextInt(1, A);

    cout << "j: ";
    for (int i = 0; i < n; i++)
        cout << i + 1 << " ";

    cout << endl
         << "r: ";
    for (int i = 0; i < n; i++)
        cout << r[i] << " ";

    cout << endl
         << "p: ";
    for (int i = 0; i < n; i++)
        cout << p[i] << " ";

    return 0;
}
