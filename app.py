from flask import Flask, render_template, redirect, url_for, request
from collections import defaultdict

app = Flask(__name__)

# Essa parte simula um banco de dados
componentes_db = [
    {'id': 1, 'nome': 'Intel Core i5-13400F', 'tipo': 'Processador', 'marca': 'Intel', 'modelo': 'Core i5-13400F', 'preco': 1299.99, 'quantidade_estoque': 10},
    {'id': 2, 'nome': 'AMD Ryzen 7 5700X', 'tipo': 'Processador', 'marca': 'AMD', 'modelo': 'Ryzen 7 5700X', 'preco': 1199.90, 'quantidade_estoque': 15},
    
    {'id': 3, 'nome': 'ASUS Prime B660M', 'tipo': 'Placa-mãe', 'marca': 'ASUS', 'modelo': 'Prime B660M', 'preco': 899.99, 'quantidade_estoque': 8},
    {'id': 4, 'nome': 'Gigabyte B550M Aorus Elite', 'tipo': 'Placa-mãe', 'marca': 'Gigabyte', 'modelo': 'B550M Aorus Elite', 'preco': 849.90, 'quantidade_estoque': 12},

    {'id': 5, 'nome': 'Corsair Vengeance 16GB DDR4', 'tipo': 'Memória RAM', 'marca': 'Corsair', 'modelo': 'Vengeance 16GB DDR4', 'preco': 379.99, 'quantidade_estoque': 30},
    {'id': 6, 'nome': 'Kingston Fury Beast 32GB DDR5', 'tipo': 'Memória RAM', 'marca': 'Kingston', 'modelo': 'Fury Beast 32GB DDR5', 'preco': 799.90, 'quantidade_estoque': 20},

    {'id': 7, 'nome': 'NVIDIA GeForce RTX 3060 12GB', 'tipo': 'Placa de Vídeo', 'marca': 'NVIDIA', 'modelo': 'GeForce RTX 3060 12GB', 'preco': 2199.99, 'quantidade_estoque': 5},
    {'id': 8, 'nome': 'AMD Radeon RX 6600 8GB', 'tipo': 'Placa de Vídeo', 'marca': 'AMD', 'modelo': 'Radeon RX 6600 8GB', 'preco': 1799.90, 'quantidade_estoque': 7},
]

@app.route("/")
def tela_inicial():
    """Renderiza a página inicial."""
    return render_template("index.html")

@app.route("/selecao", methods=["GET", "POST"])
def tela_selecao():
    """Renderiza a página de seleção e processa a compra."""
    if request.method == "POST":
        tipos_necessarios = {'Processador', 'Placa-mãe', 'Memória RAM', 'Placa de Vídeo'}
        if tipos_necessarios.issubset(request.form.keys()):
            return redirect(url_for("tela_agradecimento"))
        
        return redirect(url_for("tela_selecao"))

    pecas_agrupadas = defaultdict(list)
    for peca in componentes_db:
        if peca['quantidade_estoque'] > 0: 
            pecas_agrupadas[peca['tipo']].append(peca)
            
    return render_template("selecao.html", pecas_agrupadas=pecas_agrupadas)

@app.route("/agradecimento")
def tela_agradecimento():
    """Renderiza a página de agradecimento."""
    return render_template("agradecimento.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)