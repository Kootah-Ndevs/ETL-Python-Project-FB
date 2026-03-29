# ETL-Python-Project-FB
# Pipeline ETL: Membros da Família Sohma (Fruits Basket) 🍙

Este projeto foi desenvolvido como parte do desafio de *Pipeline de ETL com Python* da Santander Dev Week na plataforma [DIO](https://www.dio.me/). 

Para tornar o aprendizado mais próximo dos meus interesses, decidi adaptar o contexto original (bancário) para o universo do anime *Fruits Basket*, simulando um sistema que processa o status espiritual dos membros da Família Sohma.

## 📋 Objetivo do Projeto
Demonstrar o fluxo completo de um processo *ETL* (Extract, Transform, Load):
1. *Extração:* Leitura de dados de personagens a partir de um arquivo CSV.
2. *Transformação:* Aplicação de lógica condicional para gerar mensagens personalizadas sobre o status da maldição do Zodíaco Chinês.
3. *Carregamento:* Exportação dos dados transformados para um novo arquivo CSV consolidado.

## 🛠️ Tecnologias Utilizadas
* *Python 3*
* *Pandas:* Para manipulação e transformação de dados.
* *Biblioteca OS:* Para gerenciamento de caminhos de arquivos (Path handling).

## 🚀 Desafios Superados
Durante o desenvolvimento, lidei com conceitos fundamentais de engenharia de dados, como:
* *Tratamento de Indentação:* Organização de blocos de código e funções.
* *Caminhos Absolutos:* Uso do módulo os para garantir que o script localize os arquivos CSV independentemente do diretório de execução.
* *Sintaxe Python:* Implementação correta de métodos especiais como __name__ == "__main__".

## 📂 Como Executar
1. Certifique-se de ter o Python e a biblioteca Pandas instalados.
2. Mantenha os arquivos projeto_FB.py e personagens_FB.csv na mesma pasta.
3. Execute o script Python.
4. O arquivo final_Sohma.csv será gerado automaticamente com os resultados.
