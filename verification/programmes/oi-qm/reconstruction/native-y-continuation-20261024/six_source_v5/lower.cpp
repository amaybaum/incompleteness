// Exact bounded lower-cone propagation. Giant-delay reduction is proved separately.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>
using U=uint64_t;
struct V { U a=0,b=0,d=0; };
V X(V p,V q){return {p.a^q.a,p.b^q.b,p.d^q.d};}
V H(V p){return {p.b,p.d,p.a^(p.b&p.d)};}
std::unordered_map<U,V> cache;
V cluster(int t,int n,int a,int b){
 a=std::abs(a);b=std::abs(b);if(a<b)std::swap(a,b);
 if(t<0 || std::min(std::abs(n),std::abs(n+2))+a+b>t || ((t-n-a-b)&1))return {};
 if(t==0){if(n==0&&a==0&&b==0)return {0,0xaaaa,0};if(n==-2&&a==0&&b==0)return {0xcccc,0xf0f0,0xff00};return {};}
 U key=U(t)|(U(n+256)<<8)|(U(a)<<17)|(U(b)<<25);
 auto it=cache.find(key);if(it!=cache.end())return it->second;
 V sum=X(cluster(t-1,n-1,a,b),cluster(t-1,n+1,a,b));
 sum=X(sum,cluster(t-1,n,a-1,b));sum=X(sum,cluster(t-1,n,a+1,b));
 sum=X(sum,cluster(t-1,n,a,b-1));sum=X(sum,cluster(t-1,n,a,b+1));
 V out=X(cluster(t-2,n,a,b),H(sum));cache.emplace(key,out);return out;
}
U lift(U v){return v|(v<<16)|(v<<32)|(v<<48);}
V lifted(V v){return {lift(v.a),lift(v.b),lift(v.d)};}
bool odd(int a,int b,int c){return !(a&b)&&!(a&c)&&!(b&c);}
int main(int argc,char**argv){
 try{
 bool small=argc==4&&std::string(argv[1])=="--small";
 if(argc!=1&&!small)throw std::runtime_error("usage: lower [--small T d]");
 int T=small?std::atoi(argv[2]):185,d=small?std::atoi(argv[3]):68;
 if(T<2||T>185||d<1||d>68)throw std::runtime_error("parameter bound");
 int radius=d+4,w=2*radius+1;
 size_t size=size_t(w)*w*w;
 std::vector<V> old(size),now(size);
 auto index=[&](int a,int b,int c){return (size_t(a+radius)*w+(b+radius))*w+(c+radius);};
 const U my=0xffff0000ffff0000ULL,mr=0xffffffff00000000ULL;
 auto base=[&](int tau,int dx,int dy,int dz){
  int j=dy-1,z=d+2+dz;
  V value=lifted(cluster(T+tau,T+j,dx,z));
  int ax[3]={std::abs(dx),std::abs(dx-T),std::abs(dx+T)};
  int by[3]={T-j,small?std::abs(j):(-j&1023),small?std::abs(j):(-j&1023)};
  int delta[3]={std::abs(dx)-j+std::abs(z),
               std::abs(dx-T)-T+(small?std::abs(j):-j)+std::abs(z),
               std::abs(dx+T)-T+(small?std::abs(j):-j)+std::abs(z)};
  U bits[3]={my^mr,my,mr};
  for(int k=0;k<3;k++){
   if(delta[k]<tau)throw std::runtime_error("control behind first front");
   if(delta[k]==tau&&odd(ax[k],by[k],std::abs(z))){
    V pulse={0,bits[k],0};for(int m=0;m<(T+tau)%3;m++)pulse=H(pulse);value=X(value,pulse);
   }
  }
  return value;
 };
 for(int x=-radius;x<=radius;x++)for(int y=-radius+std::abs(x);y<=radius-std::abs(x);y++)for(int z=-radius+std::abs(x)+std::abs(y);z<=radius-std::abs(x)-std::abs(y);z++){
  auto i=index(x,y,z);now[i]=base(-1,x,y,z);
  if(std::abs(x)+std::abs(y)+std::abs(z)<=radius-1)old[i]=base(-2,x,y,z);
 }
 for(int tick=0;tick<d;tick++){
  int r=radius-1-tick;
  for(int x=-r;x<=r;x++)for(int y=-r+std::abs(x);y<=r-std::abs(x);y++)for(int z=-r+std::abs(x)+std::abs(y);z<=r-std::abs(x)-std::abs(y);z++){
   auto i=index(x,y,z);V sum=X(now[index(x-1,y,z)],now[index(x+1,y,z)]);
   sum=X(sum,now[index(x,y-1,z)]);sum=X(sum,now[index(x,y+1,z)]);
   sum=X(sum,now[index(x,y,z-1)]);sum=X(sum,now[index(x,y,z+1)]);
   old[i]=X(old[i],H(sum));
  }
  std::swap(old,now);
 }
 std::cout<<"[";bool first=true;
 for(int which=0;which<2;which++){
  int r=which?4:3;auto&grid=which?now:old;
  for(int x=-r;x<=r;x++)for(int y=-r+std::abs(x);y<=r-std::abs(x);y++)for(int z=-r+std::abs(x)+std::abs(y);z<=r-std::abs(x)-std::abs(y);z++){
   if(!first)std::cout<<",";
   first=false;V v=grid[index(x,y,z)];
   std::cout<<"["<<(which?-1:-2)<<",["<<x<<","<<y-1<<","<<z+2<<"],[\""<<std::hex<<v.a<<"\",\""<<v.b<<"\",\""<<v.d<<std::dec<<"\"]]";
  }
 }
 std::cout<<"]\n";std::cerr<<"cluster_cache_states="<<cache.size()<<"\n";
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}
}
