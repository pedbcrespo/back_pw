from flask import request
from flask_restful import Resource, reqparse
from config import api
from controller import *
import json


class Inicial(Resource):
    def get(self):
        return {"status":"rodando"}

# ------------- PRODUTO ------------- #
class ProdutoInfo(Resource):
    produto = ProdutoController()
    def get(self, id_produto):
        return self.produto.buscar(id_produto)

    def delete(self, id_produto):
        return self.produto.deletar(id_produto)

    def put(self, id_produto):
        dados_atualizados = json.loads(request.data)
        return self.produto.atualizar_produto(id_produto, dados_atualizados)

class ImagemProduto(Resource):
    produto = ProdutoController()
    def get(self, id_produto):
        return self.produto.download_imagem(id_produto)

    def post(self, id_produto):
        imagem = request.files['file']
        # if imagem:
        #     # self.produto.upload_imagem(id_produto, imagem)
        #     print(request.files)
        return {"mensagem": imagem}

class ProdutoRota(Resource):
    produto = ProdutoController()
    def get(self):
        return self.produto.buscar_todos()

    def post(self):
        novo_produto = request.form
        return self.produto.adicionar(
            novo_produto["nome"], 
            int(novo_produto["categoria"]),
            float(novo_produto["preco"]),
            int(novo_produto['quantidade']),
            novo_produto['imagem'],
        )
        # return novo_produto



# ------------- CATEGORIA ------------- #
class CategoriaRota(Resource):
    categoria = CategoriaController()
    def get(self):
        return self.categoria.buscar_todos()        

    def post(self):
        nova_categoria = json.loads(request.data)
        return self.categoria.adicionar(
            nova_categoria['nome']
        )

# ------------- CLIENTE ------------- #
class ClienteRota(Resource):
    cliente = ClienteController()
    def get(self):
        return self.cliente.buscar_todos()

    def post(self):
        novo_cliente = json.loads(request.data)
        return self.cliente.adicionar(novo_cliente['id'])

class ClienteInfo(Resource):
    cliente = ClienteController()
    def get(self, id_cliente):
        return self.cliente.buscar_cliente(id_cliente)

class ClienteComDados(Resource):
    cliente = ClienteController()
    def get(self, id_cliente):
        # Retorna {id, ativo}
        return self.cliente.estado_cliente(id_cliente)

    def delete(self, id_cliente):
        return self.cliente.deletar(id_cliente)

class InfoCliente(Resource):
    cliente = ClienteController()
    def get(self):
        return self.cliente.buscar_todos_cliente_info()

    def post(self):
        dados_cliente = json.loads(request.data)
        return self.cliente.adiciona_info(
            dados_cliente['email'],
            dados_cliente['endereco'],
            dados_cliente['cep'],
            dados_cliente['idCliente']
        )

    def get(self):
        return self.cliente.buscar_todos_cliente_info()

class ClienteDados(Resource):
    cliente = ClienteController()
    def get(self, id_cliente):
        return self.cliente.buscar_cliente(id_cliente)


# ------------- CARRINHO ------------- #
class CarrinhoRota(Resource):
    carrinho = CarrinhoController()

    def get(self):
        return self.carrinho.buscar_todos()

    def post(self):
        novo_carrinho = json.loads(request.data)
        return self.carrinho.adicionar_lista_produtos(
            novo_carrinho["idCliente"],
            novo_carrinho["lista"]
        )

class CarrinhoInfo(Resource):
    carrinho = CarrinhoController()
    def get(self, id_cliente):
        return self.carrinho.buscar(id_cliente)

    def put(self, id_cliente):
        dado_carrinho = json.loads(request.data)
        return self.carrinho.finalizar_compra(id_cliente)

class CarrinhoProduto(Resource):
    carrinho = CarrinhoController()
    def delete(self, id_cliente, id_produto, indice):
        return self.carrinho.remover_produto(id_cliente, id_produto, indice)

class FinalizarCompra(Resource):
    carrinho = CarrinhoController()
    def get(self, id_cliente):
        return self.carrinho.finalizar_compra(id_cliente)

# ------------- ESTOQUE ------------- #
class EstoqueRota(Resource):
    produto = ProdutoController()
    def get(self):
        return self.produto.buscar_todo_estoque()




# Definindo o caminho para a API


api.add_resource(Inicial, "/")#GET

# ------------- PRODUTO ------------- #

api.add_resource(ProdutoRota, "/produtos")#GET, POST
api.add_resource(ProdutoInfo, "/produto/<int:id_produto>")#GET, PUT
api.add_resource(ImagemProduto, "/imagem/<int:id_produto>")#GET, POST

# ------------- CATEGORIA ------------- #

api.add_resource(CategoriaRota, "/categorias")#GET, POST

# ------------- CLIENTE ------------- #

api.add_resource(ClienteRota, "/clientes")#GET, POST(só o id)
api.add_resource(ClienteComDados, "/cliente/<int:id_cliente>")#GET, DELETE(só o id)
api.add_resource(InfoCliente, "/info_cliente")#GET, POST
api.add_resource(ClienteDados, "/dados_cliente/<int:id_cliente>")#POST

# ------------- CARRINHO ------------- #

api.add_resource(CarrinhoRota, "/carrinhos")#GET, POST
api.add_resource(CarrinhoInfo, "/carrinho/<int:id_cliente>")#GET, PUT
api.add_resource(CarrinhoProduto, "/carrinho_del/<int:id_cliente>/<int:id_produto>/<int:indice>")#DELETE

api.add_resource(FinalizarCompra, "/finalizar_compra/<int:id_cliente>")

# ------------- ESTOQUE ------------- #

api.add_resource(EstoqueRota, "/estoque")#GET