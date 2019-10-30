# Laura

### Projeto criado durante o processo seletivo para a vaga de Backend Developer na empresa Laura

## import_data.py
Script Python responsável por:
- Carregar configs presentes no arquivo "env_file.env";
- Ler dados do dataset (.csv) disponibilizado;
- Conectar-se com o banco de dados MongoDB Atlas;
- Inserir registros do dataset no banco de dados;
**OBS: Ao rodar o script mais de uma vez, o mesmo apaga todos os dados e faz a reinserção de acordo com os registros do dataset**

## app.py
Controller Python com os endpoints da API. Endpoints:

1. **http://localhost:5000/estudantes**
  - Listar todos os itens de uma modalidade em um período, ordenados por data.
  - **a.** Tipo da requisição: **GET**
  - **b.** Parâmetros: modalidade, data de início e data de fim
  - **c.** Retorno: lista de todos os itens com modalidade, filtrando pelo período passado e ordenando de forma decrescente pela data dos documentos.

2. **http://localhost:5000/cursos**
  - Listar todos os cursos de um campus
  - **a.** Tipo da requisição: **GET**
  - **b.** Parâmetros: campus
  - **c.** Retorno: lista de cursos do campus

3.**http://localhost:5000/alunos** 
  - Descobrir número total de alunos num campus em um dado período
  - **a.** Tipo de requisição: **GET**
  - **b.** Parâmetros: campus, data de início e data de fim
  - **c.** Retorno: número de alunos do campus no período

4. **http://localhost:5000/cadastrar** 
  - Cadastrar alunos
  - **a.** Tipo da requisição: **POST**
  - **b.** Parâmetros: nome, idade_ate_31_12_2016, ra, campus, município, curso, modalidade, nivel_do_curso, data_inicio
  - **c.** Retorno: sucesso/erro

5. **http://localhost:5000/aluno** 
  - Buscar aluno
  - **a.** Tipo da requisição: **GET**
  - **b.** Parâmetro: ra
  - **c.** Retorno: todos os dados do aluno

6. **http://localhost:5000/remover** 
  - Remover aluno do banco
  - **a.** Tipo da requisição: **DELETE**
  - **b.** Parâmetros: ra, campus
  - **c.** Retorno: sucesso/erro
