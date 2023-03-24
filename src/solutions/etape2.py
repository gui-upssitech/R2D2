from projet.outils.GrapheDeLieux import GrapheDeLieux, Fils, Lieu
from projet.etape2.Etat import Etat

class EtatCas1(Etat) :
    def estSolution(self) :
        return self.etat_courant == self.etat_fin
    
    def successeurs(self) :
        create_etat = lambda sommet: EtatCas1(self.tg, sommet, self.etat_fin)
        return [ create_etat(sommet) for sommet in self.tg.getAdjacents(self.etat_courant) ]
    
    def h(self) :
        return GrapheDeLieux.dist(self.etat_courant, self.etat_fin, self.tg)
    
    def k(self, e) :
        return self.tg.getCoutArete(self.etat_courant, e.etat_courant)
    
    #######################################################################################
    
    def displayPath(self, pere) :
        chemin = []
        cur = self
        while cur != None:
            chemin.append(cur.etat_courant)
            cur = pere[cur]

        print("resultat trouve :", chemin)

    def __init__(self, tg : GrapheDeLieux, etat_courant: int = 0, etat_fin: int = None) :
        self.tg = tg

        self.etat_courant = etat_courant
        self.etat_fin = etat_fin if (etat_fin is not None) else tg.getNbSommets() - 1
    def __hash__(self) :
        summary_num = self.etat_fin * 1000 + self.etat_courant
        return summary_num.__hash__() 
    def __eq__(self, o) :
        if not isinstance(o, EtatCas1):
            return False

        e: EtatCas1 = o
        return (
            self.etat_courant == e.etat_courant and 
            self.etat_fin == e.etat_fin
        )   
    def __str__(self) :
        return f"Etat[etat_courant={self.etat_courant}, etat_fin={self.etat_fin}]"
    

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
    
    def displayPath(self, pere = None) :
        print("resultat trouve :", self.visited[::-1])

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


class EtatCas3(EtatCas2):

    def successeurs(self) :
        keep_successeur = lambda sommet: (sommet not in self.visited) or (self.all_visited() and sommet == self.etat_depart)
        create_etat = lambda sommet: EtatCas3(self.tg, self.etat_depart, self.visited + [sommet])

        return [ create_etat(sommet) for sommet in range(self.tg.getNbSommets()) if keep_successeur(sommet) ]
    
    def h(self) :
        moves_left = self.tg.getNbSommets() - len(set(self.visited)) + 1
        return moves_left * self.tg.getPoidsMinAir()
    
    def k(self, e) :
        return GrapheDeLieux.dist(self.etat_courant, e.etat_courant, self.tg)