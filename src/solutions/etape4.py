from projet.solvers.SolverCSP import SolverCSP
from projet.outils.GrapheDeLieux import GrapheDeLieux

def etape4(tg: GrapheDeLieux, nb_couleurs: int):
    """  methode de TESTS pour Etape4 """
    solveur = SolverCSP(tg, nb_couleurs)
    return solveur.solve(False)