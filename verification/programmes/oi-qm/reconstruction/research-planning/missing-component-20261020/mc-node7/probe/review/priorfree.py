import sys
src=open(sys.argv[1]).read().replace("if __name__ == '__main__':\n    main()","")
g={'__name__':'x','__file__':sys.argv[1]}; exec(src,g)
F=g['F']
for j in range(10):
    bx=g['le_box_lamprior'](F(j,9))
    print(j, 'Smax',g['s_max'](bx),'nosig',g['nosig'](bx), 'margB(a,b=1)',[sum(bx.get((a,1,q,0),0) for q in (0,1)) for a in (0,1)])
bx=g['le_box_lamprior'](F(1,2)); print('p0=1/2', g['s_max'](bx), g['nosig'](bx))
# LE(1,1) bijectivity on Omega
R=g['le_real'](1,1,1,1); print('check_O LE(1,1)', g['check_O'](R))
