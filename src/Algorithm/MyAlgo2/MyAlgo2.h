#ifndef __MYALGO2_H
#define __MYALGO2_H

#include "../AlgorithmBase/AlgorithmBase.h"
#include "../../Network/Graph/Graph.h"
#include "../../config.h"

using namespace std;

class MyAlgo2 : public AlgorithmBase {
    vector<double> alpha;
    vector<vector<double>> beta;
    vector<map<Shape_vector, double>> x;
    vector<vector<vector<double>>> dp;
    vector<vector<vector<bool>>> caled;
    vector<vector<vector<int>>> par;
    double epsilon, obj;
    Shape_vector separation_oracle();
    pair<Shape_vector, double> find_min_shape(int src, int dst, double alp);
    double recursion_calculate_min_shape(int left, int right, int t, vector<int> &path);
    Shape_vector recursion_find_shape(int left, int right, int t, vector<int> &path);
    int request_cnt;
public:
    MyAlgo2(Graph graph, vector<pair<int, int>> requests, map<SDpair, vector<Path>> paths);
    void run();
};

#endif