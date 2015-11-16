#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream> 
#include <cmath> 
using namespace std;

bool is_armstrong_number(int number) {
    ostringstream ostr;
    ostr << number; 
    string number_string = ostr.str();
    int len = number_string.length();
    int sum = 0;

    for (int i=0; i<len; i++) {
        char c = number_string[i];
        int num = c - '0';
        sum += pow(num, len);
    }

    if (sum == number)
        return true;
    else 
        return false;
}

int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    int number;
    while (getline(stream, line)) {
        number = atoi(line.c_str());
        if (is_armstrong_number(number))
            cout << "True" << endl;
        else
            cout << "False" << endl;
    }

    return 0;
}

