import json # Importa a biblioteca JSON

# Função que abre um arquivo JSON e retorna os dados
def abrirArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError: # Trata o erro de arquivo não encontrado
        print('Arquivo não encontrado.')
        return None
    except json.decoder.JSONDecodeError:
        print('Arquivo inválido.') # Trata o erro de arquivo inválido
        return None

# Função que salva os dados em um arquivo JSON
def salvarArquivo(nomeArquivo, dados):
    with open(nomeArquivo, 'w') as arquivo:
        json.dump(dados, arquivo)

def main():
    nomeArquivo = 'dados.json'
    dados = abrirArquivo(nomeArquivo)
    if dados is None:
        dados = {}
    dados['nome'] = 'João'
    salvarArquivo(nomeArquivo, dados)

    abrirArquivo(nomeArquivo)
    print(f"O nome é {dados['nome']}")

if __name__ == '__main__':
    main()
