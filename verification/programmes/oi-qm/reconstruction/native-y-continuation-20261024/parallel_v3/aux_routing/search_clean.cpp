#include <array>
#include <vector>
#include <map>
#include <iostream>
using namespace std; using V=array<int,3>;using Q=array<unsigned char,3>;
V add(V a,V b){for(int i=0;i<3;i++)a[i]+=b[i];return a;}int norm(V a){return abs(a[0])+abs(a[1])+abs(a[2]);}
Q h(Q a){return {a[1],a[2],(unsigned char)(a[0]^(a[1]&a[2]))};}Q mask(int v){return {(unsigned char)((v&4)?255:0),(unsigned char)((v&2)?255:0),(unsigned char)((v&1)?255:0)};}
vector<V> dirs={{1,0,0},{-1,0,0},{0,1,0},{0,-1,0},{0,0,1},{0,0,-1}};
int main(){for(V target:vector<V>{{1,1,0},{2,1,0},{1,1,1},{2,2,0},{3,1,0},{2,1,1},{3,2,0},{2,2,1},{3,3,0}}){int T=norm(target);vector<V> points;map<V,int> idx;vector<array<int,6>> links;
for(int r=T;r>=0;r--)for(int x=-r;x<=r;x++)for(int y=-r;y<=r;y++)for(int z=-r;z<=r;z++)if(abs(x)+abs(y)+abs(z)==r){V v={x,y,z};idx[v]=points.size();points.push_back(v);}int n=points.size(),nb=0;while(norm(points[nb])==T)nb++;links.resize(n);
for(int i=nb;i<n;i++){links[i].fill(-1);for(int j=0;j<6;j++){V w=add(points[i],dirs[j]);if(norm(w)==norm(points[i])+1)links[i][j]=idx.at(w);}}
V neg={-target[0],-target[1],-target[2]};int input=idx.at(neg);vector<Q> a(n);
auto test=[&](int c,int cv,int d,int dv){fill(a.begin(),a.begin()+nb,Q{0,0,0});a[input]={240,204,170};if(c>=0)a[c]=mask(cv);if(d>=0)a[d]=mask(dv);for(int i=nb;i<n;i++){Q sum={0,0,0};for(int p:links[i])if(p>=0)for(int j=0;j<3;j++)sum[j]^=a[p][j];a[i]=h(sum);}Q out=a.back();bool useful=false;for(int j=0;j<3;j++){if(out[j]!=0&&out[j]!=240)return false;if(out[j]==240)useful=true;}if(!useful)return false;
cout<<"FOUND target "<<target[0]<<","<<target[1]<<","<<target[2]<<" input Q; ";for(auto [p,m]:vector<pair<int,int>>{{c,cv},{d,dv}})if(p>=0){V v=add(points[p],target);cout<<"control "<<v[0]<<","<<v[1]<<","<<v[2]<<"="<<m<<" ";}cout<<"output "<<(int)out[0]<<","<<(int)out[1]<<","<<(int)out[2]<<endl;return true;};
bool found=false;for(int c=0;c<nb&&!found;c++)if(c!=input)for(int cv=1;cv<8;cv++)if(test(c,cv,-1,0)){found=true;break;}if(!found)for(int c=0;c<nb&&!found;c++)if(c!=input)for(int d=c+1;d<nb&&!found;d++)if(d!=input)for(int cv=1;cv<8&&!found;cv++)for(int dv=1;dv<8;dv++)if(test(c,cv,d,dv)){found=true;break;}cerr<<"DONE "<<T<<" target "<<target[0]<<","<<target[1]<<","<<target[2]<<" found "<<found<<" boundary "<<nb<<" nodes "<<n<<endl;if(found)return 0;}}
