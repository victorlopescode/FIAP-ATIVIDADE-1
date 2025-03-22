# Declaração de variáveis (listas vazias)

# Funções para calcular área e fertilizante - Cana-de-açúcar
def calcular_area_cana(largura, comprimento):
    return largura * comprimento

def calcular_fertilizante_cana(area, kg_hectare):
    return (area / 10000) * kg_hectare

# Funções para calcular área e pulverização - Café
def calcular_area_cafe(numero_linhas, comprimento_linha, espacamento_linhas):
    return numero_linhas * comprimento_linha * espacamento_linhas

def calcular_pulverizacao_cafe(litros_por_metro, numero_linhas, comprimento_linha):
    return litros_por_metro * numero_linhas * comprimento_linha