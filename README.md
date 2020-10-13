# RSA-L2
Generarea cheii publice:

generează numărul aleator P, P trebuie să fie prim
generează numărul Q, de asemenea, aleatoriu și, de asemenea, prim
calculează N, înmulțirea lui P cu Q
N = P * Q
calculează totientul lui N, phi (N), unde Q-1 * P-1, deoarece acestea sunt prime
phi (N) = (Q-1) * (P-1)
generează numărul E, de asemenea aleatoriu, trebuind să satisfacă egalitatea 1 <E <phi (N)
după generarea lui E, mdc între E și phi (N) trebuie să fie egal cu 1
mdc (phi (N), E) == 1, dacă nu este satisfăcut, va trebui generat un alt număr aleatoriu E
Cheia publică este formată din N și E
Generarea cheii private:

pentru a găsi D, trebuie să satisfaceți egalitatea modului (D ^ E, phi (N)) == 1
funcția modulară este dată de restul diviziunii dintre D ^ E și phi (N)
dacă este egal cu 1, găsit D, dacă nu, D este incrementat până când îndeplinește condiția

