Projeto FarmTech Solutions 🌱

Este projeto é uma atividade acadêmica desenvolvida para a disciplina de Inteligência Artificial da FIAP, simulando um ambiente profissional utilizando Python e R, com versionamento de código pelo GitHub.

🚜 Contexto do Projeto

A FarmTech Solutions firmou contrato com uma fazenda inovadora, com o objetivo de implementar soluções tecnológicas para migrar para a Agricultura Digital.

O objetivo foi desenvolver:

Uma aplicação em Python para gerenciar áreas plantadas e insumos agrícolas para duas culturas.

Uma aplicação em R para realizar estatísticas básicas sobre esses dados e consultar uma API meteorológica pública.

📌 Funcionalidades Desenvolvidas

Aplicação Python 🐍

Culturas escolhidas: Cana-de-açúcar e Café

Cálculo de área:

Retangular (cana-de-açúcar)

Linhas paralelas (café)

Cálculo de insumos:

Fertilizante por hectare (cana-de-açúcar)

Pulverização por metro linear (café)

Manipulação dos dados:

Armazenamento e gerenciamento via vetores

Menu interativo para entrada, exibição, atualização e deleção de dados

Aplicação R 📈

Leitura de dados: Arquivo externo .txt

Análise Estatística: Média e desvio padrão da área e insumos

Consulta à API meteorológica: Dados climáticos em tempo real (OpenWeatherMap)

🛠️ Tecnologias e Pacotes Utilizados

Python: Lógica de programação, estruturação em módulos, listas, loops e decisões.

R: Pacotes utilizados:

httr e jsonlite (API)

dplyr (estatísticas)

here (caminhos relativos)

⚙️ Estrutura dos arquivos

FarmTech-Solutions/
├── python/
│   ├── menu.py          # Interface principal
│   ├── calculos.py      # Funções para cálculos
│   └── dados2.py        # Dados armazenados em listas
├── R/
│   └── aplicacaoR.r     # Script com estatísticas e API meteorológica
├── dados_cultura.txt    # Arquivo com dados para o R
├── documentacao/
│   └── resumo_artigo.docx # Resumo do artigo acadêmico
└── README.md            # Este arquivo


🚩 Como executar o projeto

Python:
cd python
python menu.py

R:
Abra o script aplicacaoR.r no RStudio ou VSCode e execute-o diretamente:
source("aplicacaoR.r", encoding = "UTF-8")

Certifique-se que todas as dependências estão instaladas:
install.packages(c("httr", "jsonlite", "dplyr", "here"))

📸 Vídeo demonstrativo
[Adicione aqui o link do seu vídeo no YouTube (não listado).]


👥 Integrantes do grupo

Integrante 1: Desenvolvimento do menu e lógica em Python

Integrante 2: Desenvolvimento dos cálculos matemáticos e manipulação em vetores

Integrante 3: Documentação, resumo acadêmico e vídeo

Integrante 4: Estatísticas e integração da API em R

🏫 Instituição

Projeto realizado para a FIAP - Curso de Inteligência Artificial.