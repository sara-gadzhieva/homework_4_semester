#include <fstream>
#include <cstdlib>
using namespace std;

int main() {
    ofstream f("gnuplot2.gp");
      f<<"set xrange [-6:6]"<<endl
      <<"set yrange [-6:6]"<<endl
      <<"set zrange [-10:10]"<<endl
      <<"set grid"<<endl
      <<"set key off"<<endl
      <<"do for [a=0:360:1] {"<<endl
      <<"	set view 45, a"<<endl
      <<"	splot x**2-y**2 with pm3d"<<endl
      <<"	pause 0.01"<<endl
      <<"}"<<endl;
    system("gnuplot plot.gp");
    return 0;
	}
