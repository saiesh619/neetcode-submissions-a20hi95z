class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        map<int,set<char>> row ;
        map<int,set<char>> col ;
        map<pair<int,int>,set<char>> sqaure;
        for(int i = 0 ; i < 9 ; i++){
            for(int j = 0 ; j < 9 ; j++){
                pair<int,int> key = {i/3, j/3};
                if(board[i][j]=='.'){
                    continue;
                }
                if(row[i].find(board[i][j]) != row[i].end()){
                    return false ;                     
                }                
                else if(col[j].find(board[i][j]) != col[j].end()){
                    return false ;                     
                }
                else if(sqaure[key].find(board[i][j]) != sqaure[key].end()) {                    
                    return false ;
                }
                row[i].insert(board[i][j]);
                col[j].insert(board[i][j]);
                sqaure[key].insert(board[i][j]);
            }    
        }
     return true ;   
    }
};
