#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {

  public: int lengthOfLongestSubstring( string s ) {

    unordered_map <char, int> seen;

    int ret = 0, low = 0, n = s.size();

    for ( int index = 0; index < n; ++index ) {
      if ( seen.count( s[index] ) != 0 ){ 
        low = max( low, seen[ s[index] ] + 1 );
      }
      seen[ s[index] ] = index;
      ret = max( ret, index - low + 1 );
    }
    return ret;

  }

};

int main(){

  Solution soln;
  int example;

  example = soln.lengthOfLongestSubstring("pwwkew");

  cout << example << endl;

  return 0;
}

