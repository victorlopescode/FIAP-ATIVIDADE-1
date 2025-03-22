from calculos import calcular_area_cafe, calcular_area_cana, calcular_fertilizante_cana, calcular_pulverizacao_cafe
from database import create_connection

def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1 - Entrada de Dados")
        print("2 - Exibir Dados")
        print("3 - Atualizar Dados")
        print("4 - Deletar Dados")
        print("5 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            entrada_dados()
        elif escolha == '2':
            exibir_dados()
        elif escolha == '3':
            atualizar_dados()
        elif escolha == '4':
            deletar_dados()
        elif escolha == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida!")

def get_next_id():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM dados ORDER BY id')
    ids = [row[0] for row in cursor.fetchall()]
    conn.close()
    if 1 not in ids:
        return 1
    elif 2 not in ids:
        return 2
    else:
        return None

# Entrada dos dados
def entrada_dados():
    next_id = get_next_id()
    if next_id is None:
        print("Já existem dois dados cadastrados. Por favor, delete um dado antes de adicionar outro.")
        return

    print("\nEscolha a cultura para inserir dados:")
    print("1 - Cana-de-açúcar")
    print("2 - Café")
    opcao_cultura = input("Digite a opção: ")
    
    if opcao_cultura == '1':
        largura = float(input('Largura da área (m): '))
        comprimento = float(input('Comprimento da área (m): '))
        area = calcular_area_cana(largura, comprimento)
        fertilizante = calcular_fertilizante_cana(area, 150) # 150 kg/hectare (exemplo)

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO dados (id, cultura, area, insumo) VALUES (?, ?, ?, ?)', (next_id, 'Cana-de-açúcar', area, fertilizante))
        conn.commit()
        conn.close()

        print("Dados de Cana-de-açúcar cadastrados com sucesso!")

    elif opcao_cultura == '2':
        n_linhas = int(input('Número de linhas: '))
        comprimento_linha = float(input('Comprimento das linhas (m): '))
        espacamento = float(input('Espaçamento entre linhas (m): '))
        area = calcular_area_cafe(n_linhas, comprimento_linha, espacamento)
        pulverizacao = calcular_pulverizacao_cafe(0.5, n_linhas, comprimento_linha) # 0.5 litros/m (exemplo)

        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO dados (id, cultura, area, insumo) VALUES (?, ?, ?, ?)', (next_id, 'Café', area, pulverizacao))
        conn.commit()
        conn.close()

        print("Dados do Café cadastrados com sucesso!")

    else:
        print("Opção inválida!")

# Exibir dados cadastrados
def exibir_dados():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dados')
    rows = cursor.fetchall()
    conn.close()

    if len(rows) == 0:
        print("\nNenhum dado cadastrado.")
        return

    print("\n--- Dados Cadastrados ---")
    for row in rows:
        print(f"{row[0]}. Cultura: {row[1]}")
        print(f"   Área: {row[2]:.2f} m²")
        if row[1] == 'Cana-de-açúcar':
            print(f"   Fertilizante: {row[3]:.2f} kg")
        elif row[1] == 'Café':
            print(f"   Pulverização: {row[3]:.2f} litros")

# Atualizar dados existentes
def atualizar_dados():
    exibir_dados()
    id = int(input("\nDigite o Numero(1 ou 2) da cultura que deseja atualizar: "))

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dados WHERE id = ?', (id,))
    row = cursor.fetchone()

    if row:
        if row[1] == 'Cana-de-açúcar':
            largura = float(input('Nova largura da área (m): '))
            comprimento = float(input('Novo comprimento da área (m): '))
            area = calcular_area_cana(largura, comprimento)
            fertilizante = calcular_fertilizante_cana(area, 150)
            cursor.execute('UPDATE dados SET area = ?, insumo = ? WHERE id = ?', (area, fertilizante, id))
            conn.commit()
            print("Dados atualizados com sucesso!")

        elif row[1] == 'Café':
            n_linhas = int(input('Novo número de linhas: '))
            comprimento_linha = float(input('Novo comprimento das linhas (m): '))
            espacamento = float(input('Novo espaçamento entre linhas (m): '))
            area = calcular_area_cafe(n_linhas, comprimento_linha, espacamento)
            pulverizacao = calcular_pulverizacao_cafe(0.5, n_linhas, comprimento_linha)
            cursor.execute('UPDATE dados SET area = ?, insumo = ? WHERE id = ?', (area, pulverizacao, id))
            conn.commit()
            print("Dados atualizados com sucesso!")
    else:
        print("Nenhum dado foi cadastrado")
    
    conn.close()

# Deletar dados existentes
def deletar_dados():
    exibir_dados()
    id = int(input("\nDigite o Número(1 ou 2) da cultura que deseja deletar: "))

    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dados WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    print("Dados deletados com sucesso!")

# Execução do programa
menu()