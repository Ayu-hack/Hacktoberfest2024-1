
class Solution {
public:
    int minOperations(vector<string>& logs) {

        int n = logs.size();
        // will be storing the size of the logs vector!

        stack<string> st;
        // in order to check for the directory we are currently in, as it follows LIFO Principle

        for(int i = 0; i < n; i++){

            if(logs[i] == "../" && !st.empty()){
            // if this condition occurs, and stack is non empty aswell, we need to go back to previous directory
                st.pop();
            }
            else if(logs[i] != "../" && logs[i] != "./"){
            // if the element of logs folder is neither of above two string, we need to push the element as we are switching to this directory
                st.push(logs[i]);
            }
        }

        int count = 0;
        // to store the count of how much operations we need to come back to the main folder which was the first folder we were at!

        while(!st.empty()){

            
            count++;
            st.pop();
        }
        
        return count;
    }
};
