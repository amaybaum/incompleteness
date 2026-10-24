#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using V=std::array<int,3>;
int main(){
 const std::array<V,6> d={V{-1,0,0},V{1,0,0},V{0,-1,0},V{0,1,0},V{0,0,-1},V{0,0,1}};
 std::map<V,int> sites;
 int at[6][6];
 for(int j=0;j<6;j++)for(int k=0;k<6;k++){
  V v;for(int z=0;z<3;z++)v[z]=d[j][z]+d[k][z];
  if(v==V{0,0,0}) at[j][k]=-1;
  else {if(!sites.count(v)){int n=sites.size();sites[v]=n;}at[j][k]=sites.at(v);}
 }
 if(sites.size()!=18)return 1;
 std::map<V,int> orbits;
 for(int x=0;x<64;x++){V c={0,0,0};for(int j=0;j<3;j++)c[((x>>(2*j))&1)+((x>>(2*j+1))&1)]++;orbits[c]=0;}
 int ix=0;for(auto &p:orbits)p.second=ix++;
 int survivors=0;
 for(int code=0;code<1024;code++){
  int f[64],weight=0;
  for(int x=0;x<64;x++){V c={0,0,0};for(int j=0;j<3;j++)c[((x>>(2*j))&1)+((x>>(2*j+1))&1)]++;f[x]=(code>>orbits[c])&1;weight+=f[x];}
  if(f[0]||!f[1]||weight!=32)continue;
  survivors++;
  uint64_t counts[2][2]={{0,0},{0,0}};
  for(int b=0;b<(1<<18);b++){
   int g[2]={0,0};
   for(int h=0;h<2;h++)for(int j=0;j<6;j++){
    int mask=0;for(int k=0;k<6;k++)mask|=(at[j][k]<0?h:((b>>at[j][k])&1))<<k;
    g[h]|=f[mask]<<j;
   }
   for(int a=0;a<64;a++){int h=f[a];int h3=f[a^g[h]]^h;counts[h][h3]++;}
  }
  std::cout<<code;for(auto &row:counts)for(auto n:row)std::cout<<" "<<n;std::cout<<" / 16777216\n";
 }
 return survivors==6?0:2;
}
