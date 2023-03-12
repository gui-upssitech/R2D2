"""
module pour l'état de l'etape 2 ds le cas 2
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.Etat import Etat


class EtatCas2(Etat) :

    def estSolution(self) :
        is_start = self.etat_courant == self.etat_depart
        return self.all_visited() and len(self.visited) == self.tg.getNbSommets() + 1 and is_start
    
    def successeurs(self) :
        keep_successeur = lambda sommet: (sommet not in self.visited) or (self.all_visited() and sommet == self.etat_depart)
        create_etat = lambda sommet: EtatCas2(self.tg, self.etat_depart, self.visited + [sommet])

        return [ create_etat(sommet) for sommet in self.tg.getAdjacents(self.etat_courant) if keep_successeur(sommet) ]

    def h(self) :
        moves_left = self.tg.getNbSommets() - len(set(self.visited)) + 1
        return moves_left * self.tg.getPoidsMinTerre()
    
    def k(self, e) :
        return self.tg.getCoutArete(self.etat_courant, e.etat_courant)
    
    def displayPath(self, pere) :
        chemin = []
        cur = self
        while cur != None:
            chemin.append(cur.etat_courant)
            cur = pere[cur]

        print("resultat trouve :", chemin)

    #######################################################################################

    def all_visited(self) :
        return len(set(self.visited)) == self.tg.getNbSommets()
    
    def __init__(self, tg : GrapheDeLieux, etat_depart: int = 0, visited: list = []) :
        self.tg = tg

        self.etat_depart = etat_depart
        self.visited = visited
        if len(visited) == 0:
            self.visited.append(etat_depart)

        self.etat_courant = visited[-1]

    def __hash__(self) :
        return ''.join([str(num) for num in self.visited]).__hash__()
    
    def __eq__(self, o) :
        if not isinstance(o, EtatCas2):
            return False

        e: EtatCas2 = o
        return self.etat_courant == e.etat_courant and self.etat_depart == e.etat_depart and self.visited == e.visited
    
    def __str__(self) :
        return f"Etat[etat_courant={self.etat_courant}, etat_depart={self.etat_depart}, visited={self.visited}]"