#include <fstream>
#include <cmath>
using namespace std;

int main() {
    ofstream d("output.txt");
    ofstream f("gnuplot.gp");
    for (double x=-4*M_PI;x<=4*M_PI;x+=0.01) d<<x<<" "<<sin(x)+cos(2*x)<<endl;
	f<<"set title \"f(x)=sin(x)+cos(2x)\""<<endl
	<<"set xlabel \"x\""<<endl
	<<"set ylabel \"y\""<<endl
	<<"set grid"<<endl
	<<"set key off"<<endl
	<<"plot \"output.txt\" using 1:2 with lines"<<endl
	<<"pause -1"<<endl;
    return 0;
	}
