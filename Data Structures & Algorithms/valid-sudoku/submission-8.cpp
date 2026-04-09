class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int,unordered_set<char>> row;
        unordered_map<int,unordered_set<char>> col;
        map<pair<int,int>,unordered_set<char>> sq;
        int r = board.size();
        int c = board[0].size();

        for(int i = 0 ; i < r ; i++){
            for(int j = 0 ; j < c ; j++){
                if(board[i][j] == '.'){
                    continue;
                }
                pair<int,int> key = { i/3 , j/3 };
                if(row[i].count(board[i][j]) or col[j].count(board[i][j]) or sq[key].count(board[i][j])){
                    return false;
                }
                row[i].insert(board[i][j]);
                col[j].insert(board[i][j]);
                sq[key].insert(board[i][j]);
            }
        }
        return true;
    }
};
