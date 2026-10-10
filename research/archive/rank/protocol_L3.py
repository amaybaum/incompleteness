import sys
sys.path.insert(0, '.')
from protocol_rank import protocol_matrix
from lattice_rank import rank_mod, P1, P2
for rule in ('linear', 'nonlinear'):
    for alph, name in ((('o',), 'passive'), (('o', 'i'), 'obs+idle'), (('o', 's'), 'obs+swap'),
                       (('o', 'f'), 'obs+flip'), (('o', 'i', 'f', 's'), 'full')):
        J = protocol_matrix(3, alph, rule)
        print(f'PROTOCOL {rule} L=3 {name}: preparations={len(J)} rank_Fp={rank_mod(J, P1)},{rank_mod(J, P2)}',
              flush=True)
print('DONE')
