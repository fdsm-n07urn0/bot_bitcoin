import ssl
import json
import websocket
import bitstamp.client
import credenciais

def cliente():
    return trading_client.Trading(username=credenciais.USERNAME,
                                  key=credenciais.KEY,
                                  secret=credenciais.SECRET)

def comprar(quantidade):
    trading_client = cliente()
    trading_client.buy_market_order(quantidade)

def vender(quantidade):
    trading_client = cliente()
    trading_client.self_market_order(quantidade)

def ao_abrir(ws):
    print('Abriu a conexão')
    json_subscribe = """
{
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
    }
}    
"""
    ws.send(json_subscribe)


def ao_fechar(ws, close_status_code, close_msg):
    print('Fechou a conexão')


def erro(ws, erro):
    print(erro)


def ao_receber_mensagem(ws, mensagem):
    mensagem = json.loads(mensagem)
    price = mensagem['data']['price']
    print(price)

    if price > 60000:
        vender()
    elif price < 30000:
        comprar()
    else:
        print('Aguardar')


if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                on_open=ao_abrir,
                                on_close=ao_fechar,
                                on_message=ao_receber_mensagem,
                                on_error=erro)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


# Git é programa de versionamento (permite criar varias versões do programa e até voltar para versão anterior)

# O git constuma vir instalado no linux
# Para colocar o git no projeto -> Abrir o terminal (pode ser o do pycharm mesmo) (precisa estar dentro da pasta do projeto)
# Digitar o comando: git init
# Deve aparecer -> Initialized empty Git repository in /home/noturno/python-profissional/projeto5/.git/
# Digitando ls -la mostra os arquivos ocultos -> Ex: .git e .idea
# Digitar: git status -> Mostra se ta fazer tracked dos arquivos
# Criar um arquivo (não clicar python file criar o arquivo clicando em file
# Colocar o nome do arquivo de .gitignore
# Digitar dentro desse arquivo o nome da pasta a ser ignorada Ex: .idea/
# Voltar no terminal -> Digitar: git status
# Mostra que o arquivo .idea/ foi ignorado
# Digitar: git add .  -> Para adicionar todos os arquivos ou git add nome do arquivo
# Digitar: git commit -m "commit inicial"  -> Para salvar
# Quando criar outro commit colocar outro nome Ex: git commit -m "novo commit"
# Se fez alguma coisa errado ou apago e quiser desfazer digitar:  git status e despois git restore bot_bitcoin.py
# Digitar: git log -> Mostra todos os commit
# Digitar: git branch  -> Mostra todos os branch
# Criar um novo branch -> git checkout -b "nova-logica" / Cria uma copia do programa (fazer as alterações na copia)
# Despois de criar me envia pra o novo branch
# git checkout master -> permite navegar nos branch (master é o branch principal)
# git branch --help -> Mostra todos os comandos do branch
# git branch -D nomedobranch -> deleta o branch- Deve mudar para outro branch (Caso esteje no branch a ser deletado)

'''Criar arquivo credenciais.py colocar meus dados nesse arquivo
   Colocar o arquivo credenciais.py dentro do arquivo .gitignore.
   Se eu passar o codigo pra outra pessoa meus dados no arquivo 
   credenciais.py não vai junto'''

'''Para juntar os branch continuar dentro do outro branch 
(sem ser o master) -> digitar: git merge master (vai juntar o codigo do master no outro branch)
Depois digitar git checkout master para ir pro  master e fazer o processo contrario: git merge compra_e_venda
(nome do outro branch) (vai juntar o codigo do outro branch no master)'''