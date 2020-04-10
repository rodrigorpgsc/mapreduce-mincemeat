# mapreduce-mincemeat
Exemplo de uso de mapreduce sendo executado localmente em um pc, utilizando a implementação mincemeat.
A descrição da tarefa a ser realizada é descrito no pdf em anexo ao repositório.

## Repositório
  - O repositório contém os arquivos a serem lidos;
  - O Framework map-reduce, com implementação mincemeat;
  - Funções de map e reduce;
 

## Execução

  - A aplicação requer a execução do servidor e do cliente(pode ter 1 ou mais clientes), então será necessário a abertura de 1 prompt para o servidor e 1 prompt para cliente adicional.
### Execução de servidor
  - Abra um prompt de comando e execute o seguinte comando na raiz do projeto 
  - python exerc23.py 
  - O prompt ficará travado esperando que um ou mais clientes conectem que as tarefas sejam finalizadas.
### Execução de cliente
  - Para cada cliente abra um prompt de comando e execute o seguinte comando na raiz do projeto
  - python mincemeat.py -p changeme localhost
  - O cliente foi configurado para mostrar as chaves reduce no prompt de comando
## Resultados
  - Ao término da execução é gerado um arquivo com os resultados no caminho exerc/RESULT_trab1.csv

## Configuração
  - O código executa em python 2.7.x (garantidamente com 2.7.17)
  - Foi executado em ambiente Windows 10
