install.packages(c("httr", "jsonlite"), dependencies = TRUE)
library(httr)
library(jsonlite)

# API meteorológica
api_key <- "4e2e76f0c8f9d74a45407d4254827f05"
cidade <- "Sao Paulo"
cidade_url <- URLencode(cidade)
url <- paste0("https://api.openweathermap.org/data/2.5/weather?q=", cidade_url,
              "&appid=", api_key, "&units=metric&lang=pt_br")

# Consulta API
resposta <- GET(url)

# Dados Climáticos
if (status_code(resposta) == 200) {
  clima <- fromJSON(content(resposta, "text", encoding = "UTF-8"))
  
  cat("\n--- Dados Climáticos Atuais ---\n")
  cat("Cidade:", cidade, "\n")
  cat("Temperatura:", clima$main$temp, "°C\n")
  cat("Sensação térmica:", clima$main$feels_like, "°C\n")
  cat("Condição do tempo:", clima$weather$description[1], "\n")
  cat("Umidade:", clima$main$humidity, "%\n")
} else {
  cat("Erro ao consultar a API do clima. Código:", status_code(resposta), "\n")
}

