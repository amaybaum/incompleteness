import sys,re,unicodedata
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    s=s.replace('’',"'").replace('“','"').replace('”','"')
    return re.sub(r'\s+',' ',s).strip()
txtdir=sys.argv[1]
Q=[
('agievich','We consider a self-decimated generator of pseudorandom numbers and examine the preperiod λ and the period µ of its state sequence.'),
('agievich','R. Rueppel in the paper [4] examined the case when the word s is deter- mined from a linear recurrence sequence'),
('agievich','Rueppel showed that if the characteristic polynomial of the sequence'),
('rsv','Oblivious branching programs choose which input bit to read depending only on the time step i, and not on the current state.'),
('rsv','Permutation branching programs are a further restriction, where we require that for each setting of the input string, the mappings between layers are permutations.'),
('rsv','Let X be a ε-biased random variable'),
('aghp_goldreich','This linear combination can be either identically zero or not.'),
('aghp_goldreich','means that the polynomial f (t) divides the polynomial g (t)'),
('aghp_goldreich','being a non constant combination of the si \'s is unbiased when the si \'s are uniformly selected. Hence the bias of'),
('aghp_goldreich','equals the probability that the polynomial f (t) divides the polynomial g (t).'),
('bdvy','Let G be an ε-PRG against degree-k polynomials'),
('bdvy','read-once width-2 branching programs that read one bit at a time can be fooled by linear generators'),
('arxiv1005_0095','it is assumed that the feedback polynomial of the target LFSR is known'),
('arxiv1005_0095','is an intercepted keystream segment'),
('arxiv1005_0095','The use of these models implies that the known plaintext attack is applicable'),
('zwfb','if we choose a special ciphertext fed into the decryption circuits such that the corresponding decrypted message'),
('zwfb','is of finite length, then we can retrieve the secret keys'),
('zwfb','Since our attack only work in the chosen ciphertext scenario, the security of that generator is not influenced by our attack.'),
('hac6','Another variant of the stop-and-go generator is the step-1/step-2 generator due to Gollmann and Chambers [496].'),
('hac6','If the output of R1 is 0, then R2 is clocked once; if the output of R1 is 1, then R2 is clocked twice'),
('hac6','proposed an embedding correlation attack on R2'),
('hac6','A recent survey of techniques for attacking clock-controlled generators is given by Gollmann [495].'),
]
for f,q in Q:
    t=norm(open(f"{txtdir}/{f}.txt",encoding='utf-8',errors='replace').read())
    qq=norm(q)
    ok = qq in t
    if not ok:
        # tolerant: drop spaces
        ok2 = qq.replace(' ','') in t.replace(' ','')
        print(('SPACE-ONLY ' if ok2 else 'MISSING    ')+f+': '+q[:90])
    else: print('OK         '+f+': '+q[:90])
