from projet.outils.GrapheDeLieux import GrapheDeLieux
Base = list[list[int]]

class SolEtape1:

    def mise_a_jour_base(g: GrapheDeLieux, nb_couleurs: int) -> tuple[Base, int]:
        base = []
        for sommet in g.getSommets():
            base += clauses_sommet(sommet, nb_couleurs)
            base += clauses_adjacents(sommet, g, nb_couleurs)

        nbVariables = g.getNbSommets() * nb_couleurs

        return base, nbVariables

    def fmt_clause(clause: list[int]) -> str:
        def fmt_variable(variable: int) -> str:
            sommet, couleur, is_not = Variable.decode(variable)
            not_str = "¬" if is_not else ""
            return f"{not_str}s{sommet}_c{couleur}"
        
        return ' v '.join([fmt_variable(variable) for variable in clause])



def clauses_sommet(sommet, nb_couleurs: int):
    clauses = []
    clauses.append([Variable.encode(sommet, couleur) for couleur in range(nb_couleurs)])

    for couleur in range(nb_couleurs):
        next_couleur = (couleur + 1) % nb_couleurs
        clauses.append([
            Variable.encode(sommet, couleur, is_not=True),
            Variable.encode(sommet, next_couleur, is_not=True)
        ])
    
    return clauses

def clauses_adjacents(sommet, g, nb_couleurs: int):
    clauses = []
    for couleur in range(nb_couleurs):
        for neighbour in g.getAdjacents(sommet):
            clauses.append([
                Variable.encode(sommet, couleur, is_not=True),
                Variable.encode(neighbour, couleur, is_not=True)
                ])
    return clauses

class Variable :

    @staticmethod
    def encode(sommet, couleur, is_not=False) -> int:
        sign = -1 if is_not else 1
        return sign * (((sommet+1) << 8) + (couleur+1))

    @staticmethod
    def decode(number) -> tuple[int, int, bool]:
        is_not = number < 0
        number = abs(number)

        sommet = (number >> 8)
        couleur = (number & 0b11111111)

        return (sommet, couleur, is_not)