"""
module pour l'état de l'etape 2 ds le cas 3
"""
from projet.outils.GrapheDeLieux import GrapheDeLieux
from projet.etape2.EtatCas2 import EtatCas2

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
    
