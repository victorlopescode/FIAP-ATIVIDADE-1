library(RSQLite)
library(dplyr)

# Conectar ao banco de dados SQLite
con <- dbConnect(SQLite(), dbname = "d:/FIAP ATIVIDADE 1/dados.db")

# Carregar os dados da tabela 'dados'
dados <- dbGetQuery(con, "SELECT * FROM dados")

# Fechar a conexão com o banco de dados
dbDisconnect(con)

# Exibir os dados carregados
print(dados)

# Calcular a média e o desvio padrão da área e do insumo usando summarise
estatisticas <- dados %>%
  summarise(
    media_area = mean(area),
    desvio_area = sd(area),
    media_insumo = mean(insumo),
    desvio_insumo = sd(insumo)
  )

# Exibir os resultados

cat("Média da área:", estatisticas$media_area, "\n")
cat("Desvio padrão da área:", estatisticas$desvio_area, "\n")
cat("Média do insumo:", estatisticas$media_insumo, "\n")
cat("Desvio padrão do insumo:", estatisticas$desvio_insumo, "\n")