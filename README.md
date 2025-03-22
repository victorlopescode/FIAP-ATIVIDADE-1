# Projeto FarmTech Solutions 🌱

Este projeto é uma atividade acadêmica desenvolvida para a disciplina de **Inteligência Artificial** da FIAP, simulando um ambiente profissional utilizando **Python** e **R**, com versionamento de código pelo **GitHub**.

## 🚜 Contexto do Projeto

A **FarmTech Solutions** firmou contrato com uma fazenda inovadora para implementar soluções tecnológicas e migrar para a **Agricultura Digital**.

### Objetivos:
- Desenvolver uma aplicação em **Python** para gerenciar áreas plantadas e insumos agrícolas para duas culturas.
- Desenvolver uma aplicação em **R** para realizar análises estatísticas básicas desses dados e consultar uma API meteorológica pública.

## 📌 Funcionalidades Desenvolvidas

### Aplicação Python 🐍

- **Culturas escolhidas:** Cana-de-açúcar e Café

- **Cálculo de Área:**
  - Cana-de-açúcar: Área retangular
  - Café: Área por linhas paralelas

- **Cálculo de Insumos:**
  - Cana-de-açúcar: Fertilizante por hectare
  - Café: Pulverização por metro linear

- **Manipulação de Dados:**
  - Armazenamento e gerenciamento através de vetores
  - Menu interativo para:
    - Entrada de dados
    - Exibição dos dados cadastrados
    - Atualização de dados
    - Deleção de dados

### Aplicação R 📈

- **Leitura dos dados:** Arquivo externo armazenando as entradas dos usuários `dados.db`
- **Análise Estatística:** Média e desvio padrão por cultura (área e insumos)
- **Consulta à API Meteorológica:** Dados climáticos em tempo real utilizando **OpenWeatherMap**

## 🛠️ Tecnologias e Pacotes Utilizados

- **Python:** Lógica de programação estruturada, módulos, listas (vetores), loops e decisões.
- **R:**
  - `httr` e `jsonlite`: Consulta e manipulação dos dados da API climática
  - `dplyr`: Análise estatística

## ⚙️ Estrutura dos Arquivos

FarmTech-Solutions/
```├── python/
│   ├── menu.py                 # Interface principal
│   ├── calculos.py             # Funções para cálculos
│   └── dados2.py               # Dados armazenados em listas
├── R/
│   ├── Analise_Estatistica.r   # Estatísticas dos dados
│   └── DadosClimaticos         # integração com API de dados climaticos
├── dados.db                    # Dados para análise em R
├── documentacao/
│   └── resumo_artigo.docx      # Resumo do artigo acadêmico
└── README.md                   # Este arquivo
```


## 📸 Vídeo Demonstrativo
[Adicione aqui o link do seu vídeo no YouTube (não listado).]

## 👥 Integrantes do Grupo

- [Victor Lopes Marques](URL_DO_LINKEDIN): Desenvolvimento da interface (menu) e lógica principal em Python  
- [Tiago Lopes dos Santos](https://www.linkedin.com/in/tiago-lopes-dos-santos/): Desenvolvimento dos cálculos matemáticos e manipulação dos dados em vetores (Python)  
- [Marcelo Junior Pires Tadaieski](URL_DO_LINKEDIN): Documentação do projeto, resumo acadêmico e gravação do vídeo demonstrativo  
- [Marcelo Nahoum](URL_DO_LINKEDIN): Desenvolvimento das análises estatísticas e integração com API climática (R)


## 🏫 Instituição
Projeto desenvolvido para a FIAP – Curso de Inteligência Artificial.
