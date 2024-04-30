#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int stepFunction(double z, double theta)
{
    return (z >= theta) ? 1 : 0;
}

void Perceptron(vector<vector<int>> &X, vector<int> &y, vector<double> &weights, double alpha, double theta)
{
    for(int epochs = 0; epochs < 3; epochs++){
        for(int i = 0; i < X.size(); i++)
        {
            double sum = 0;
            for(int j = 0; j < X[i].size(); j++)
            {
                sum += X[i][j] * weights[j];
            }
            int output = stepFunction(sum, theta);
            if(y[i] - output != 0)
            {
                for(int j = 0; j < X[i].size(); j++)
                {
                    weights[j] += alpha * (y[i] - output) * X[i][j];
                }
            }
        }

        for(int i = 0; i < weights.size(); i++)
        {
            cout << weights[i] << " ";
        }
        cout << endl;
    }

}

int main()
{
    vector<vector<int>> X = {{1, 0}, {1, 1}, {0, 1}, {0, 0}};  //inputs
    vector<int> y = {1, 0, 1, 0}; // outputs
    vector<double> weights = {0.5, -0.5};
    double alpha = 0.1;     // Learning rate
    double theta = 0.1;     // Threshold

    Perceptron(X, y, weights, alpha, theta);

    return 0;
}