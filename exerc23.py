import mincemeat
import glob
import csv

text_files = glob.glob('exerc\\trab1\\*')


def mapfn(k, v):
    # o k eh caminho do arquivo do dfs e o v e o conteudo do arquivo
    # carrega lista de palavras a serem removidas
    from stopwords import allStopWords
    # varre cada uma das linhas
    for line in v.splitlines():
        # quebra o registro nos campos de interesse
        quebra_registro = line.split(":::")
        autores = quebra_registro[1]
        titulo = quebra_registro[2]
        # varre os diferentes autores
        for autor in autores.split("::"):
            # varre as diferentes palavras do titulo
            for word in titulo.split():
                # se a palavra nao estiver na lista de proibidas
                if (word not in allStopWords):
                    # remocao de caracteres nao informativos
                    word = word.replace(".", "").replace(",", "").replace(":", "").replace("(", "").replace(")", "")
                    yield autor, word


def reducefn(k, v):
    import operator
    # o k eh o retorno do map(nome do autor) e o v eh um vetor com as ocorrencias das palavras nos titulos dos livros
    print 'reduce k=' + k
    my_dict = {i: v.count(i) for i in v}
    # ordena com base nos valores da chave (itemgetter-1), sentido descendente
    sorted_x = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_x


def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()


source = dict((file_name, file_contents(file_name))for file_name in text_files)
s = mincemeat.Server()
# a fonte de dados pode ser qualquer objeto do tipo dicionario
s.datasource = source
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
w = csv.writer(open("exerc\\RESULT_trab1.csv", "w"))
for k, v in results.items():
    w.writerow([k, v])
