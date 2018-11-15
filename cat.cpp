#include <iostream>
#include <fstream>
using namespace std;

int main()
  ifstream archivo("C:/Users/criger/Desktop/Proyecto I/input.in", ios::noreplace);
  char linea[128];
  while(!archivo.eof())
  {
      archivo.getline(linea, sizeof(linea));
      cout << linea << '\n';
  }
  archivo.close();
  return 0;
}
