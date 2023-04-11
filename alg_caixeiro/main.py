import numpy as np
import itertools

class CaixeiroViajante:
    def __init__(self, n_cidades):
        self.n_cidades = n_cidades
        self.cidades = np.zeros((n_cidades, 2))
        self.distancias = np.zeros((n_cidades, n_cidades))
    
    def distancia(self, i, j):
        dx = self.cidades[i, 0] - self.cidades[j, 0]
        dy = self.cidades[i, 1] - self.cidades[j, 1]
        return np.sqrt(dx*dx + dy*dy)
    
    def gerar_cidades_aleatorias(self, limite_superior):
        self.cidades = np.random.uniform(0, limite_superior, (self.n_cidades, 2))
    
    def calcular_distancias(self):
        for i in range(self.n_cidades):
            for j in range(i+1, self.n_cidades):
                dist = self.distancia(i, j)
                self.distancias[i, j] = dist
                self.distancias[j, i] = dist
    
    def caixeiro_viajante(self):
        indices = list(range(self.n_cidades))
        menor_distancia = float('inf')
        rota_mais_curta = []
        for rota in itertools.permutations(indices):
            distancia_atual = 0.0
            for i in range(self.n_cidades-1):
                distancia_atual += self.distancias[rota[i], rota[i+1]]
            distancia_atual += self.distancias[rota[self.n_cidades-1], rota[0]]
            if distancia_atual < menor_distancia:
                menor_distancia = distancia_atual
                rota_mais_curta = rota
        return rota_mais_curta, menor_distancia

# Exemplo de uso
cv = CaixeiroViajante(10)
cv.gerar_cidades_aleatorias(100)
cv.calcular_distancias()
rota_mais_curta, distancia_total = cv.caixeiro_viajante()
print("Rota mais curta:", rota_mais_curta)
print("Distancia total:", distancia_total)
