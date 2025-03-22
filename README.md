# Projeto de Gestão Agrícola

Este projeto consiste em um sistema de gestão agrícola que permite a entrada, exibição, atualização e exclusão de dados relacionados a culturas agrícolas, bem como a análise estatística e consulta de dados climáticos.

## Estrutura do Projeto

### menu3.py
Este arquivo contém o menu principal do programa e as funções para entrada, exibição, atualização e exclusão de dados agrícolas. As principais funcionalidades incluem:
- Entrada de dados de culturas (Cana-de-açúcar e Café)
- Exibição de dados cadastrados
- Atualização de dados existentes
- Exclusão de dados

### database.py
Este arquivo gerencia a conexão com o banco de dados SQLite e a criação da tabela `dados`. As principais funcionalidades incluem:
- Criação de conexão com o banco de dados
- Criação da tabela `dados` se não existir

### calculos.py
Este arquivo contém funções para calcular a área e os insumos necessários para as culturas de Cana-de-açúcar e Café. As principais funcionalidades incluem:
- Cálculo da área e fertilizante para Cana-de-açúcar
- Cálculo da área e pulverização para Café

### Análise_Estatística.r
Este script R realiza a análise estatística dos dados agrícolas armazenados no banco de dados SQLite. As principais funcionalidades incluem:
- Conexão ao banco de dados e carregamento dos dados
- Cálculo da média e desvio padrão da área e dos insumos
- Exibição dos resultados

### DadosClimáticos.r
Este script R consulta uma API meteorológica para obter dados climáticos atuais de uma cidade específica. As principais funcionalidades incluem:
- Consulta à API do OpenWeatherMap
- Exibição dos dados climáticos atuais, como temperatura, sensação térmica, condição do tempo e umidade

## Como Executar

1. Certifique-se de ter o Python e R instalados em seu sistema.
2. Execute o script `menu3.py` para interagir com o sistema de gestão agrícola.
3. Utilize os scripts R para realizar análises estatísticas e consultar dados climáticos.

## Dependências

- Python
- SQLite
- R
- Pacotes R: `RSQLite`, `dplyr`, `httr`, `jsonlite`


--usar o arquivo "requirements.txt" para baixar a biblioteca SQLite--
--pip install requirements.txt--
