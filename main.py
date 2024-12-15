from flask import Flask, jsonify, request

app = Flask(__name__)

# Rota principal


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bem-vindo à API De cumprimento do Jurídico!"}), 200

# Rota para bloquear uma conta


@app.route("/BDT/accounts/<int:account_id>/block", methods=["POST"])
def block_account(account_id):
    data = request.get_json()
    if data.get("success"):
        return jsonify({"message": f"Conta {account_id} bloqueada com sucesso."}), 200
    else:
        return jsonify({"error": f"Falha ao bloquear a conta {account_id}."}), 400

# Rota para desbloquear uma conta


@app.route("/BDT/accounts/<int:account_id>/unblock", methods=["POST"])
def unblock_account(account_id):
    data = request.get_json()
    if data.get("success"):
        return jsonify({"message": f"Conta {account_id} desbloqueada com sucesso."}), 200
    else:
        return jsonify({"error": f"Falha ao desbloquear a conta {account_id}."}), 400

# Rota para transferir entre contas


@app.route("/BDT/accounts/transfer", methods=["POST"])
def transfer():
    data = request.get_json()
    if data.get("success"):
        return jsonify({"message": "Transferencia realizada com sucesso.", "details": data}), 200
    else:
        return jsonify({"error": "Falha ao realizar a transferencia.", "details": data}), 400

# Rota para requisição de informações de contas


@app.route("/REQ/accounts/<int:account_id>/info", methods=["GET"])
def request_account_info(account_id):
    data = request.get_json()
    if data.get("authorized"):
        return jsonify({"message": f"Informacoes da conta {account_id} acessadas com sucesso.", "details": {"account_id": account_id, "balance": 1000.0, "status": "active"}}), 200
    else:
        return jsonify({"error": f"Acesso nao autorizado as informacoes da conta {account_id}."}), 403

# Rota para quebra de sigilo bancário


@app.route("/SIMBA/accounts/<int:account_id>/breach", methods=["POST"])
def breach_account_secrecy(account_id):
    data = request.get_json()
    if data.get("court_order"):
        return jsonify({"message": f"Quebra de sigilo bancario da conta {account_id} realizada com sucesso.", "details": {"account_id": account_id, "transactions": ["txn1", "txn2", "txn3"]}}), 200
    else:
        return jsonify({"error": f"Falha ao realizar quebra de sigilo bancario da conta {account_id}. Ordem judicial nao apresentada."}), 400


if __name__ == "__main__":
    app.run(debug=True)
