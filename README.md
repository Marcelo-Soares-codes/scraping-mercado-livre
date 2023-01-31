# Web Scraping de Produtos
Este projeto tem como objetivo capturar dados de produtos de uma página da web, incluindo nome, preço e link de redirecionamento.

## Requisitos
- Python 3.8
- Biblioteca `requests`
- Biblioteca `bs4` (BeautifulSoup)
- Biblioteca `prettytable` (opcional, para exibir os dados em formato de tabela)

## Instalação
1. Instale o Python 3.8 (se ainda não tiver instalado).
2. Instale as bibliotecas necessárias usando o gerenciador de pacotes `pip`:
    pip install requests bs4 prettytable

## Uso
1. Edite o código-fonte (arquivo `scraper.py`) para especificar a URL da página da web que você deseja capturar.
2. Execute o código-fonte:
    python scraper.py

## Código-fonte
O código-fonte faz uso da biblioteca `requests` para fazer uma solicitação GET à página da web e da biblioteca `bs4` para analisar o HTML da página. Em seguida, usa o método `find_all` do BeautifulSoup para procurar todos os elementos de produto na página. Para cada produto, o código captura o nome, o preço e o link de redirecionamento usando os métodos `find`.

O código também usa a biblioteca `prettytable` para exibir os dados em formato de tabela.

Lembre-se de que você pode precisar ajustar o código para se adequar à estrutura da página da web que você está capturando, dependendo do site e do formato de dados.

## Observações
- Este projeto é apenas para fins educacionais e não deve ser usado para capturar dados de forma não autorizada ou ilegal.
- Algumas páginas da web podem bloquear ou limitar o acesso a robôs de raspagem de dados. Verifique a política de uso da página da web antes de usar este projeto.
- A precisão e atualidade dos dados capturados dependem da estrutura da página da web e da qualidade dos dados fornecidos. Verifique a fonte dos dados antes de usá-los para fins críticos.
