import sqlite3

# Funções de banco de dados
def conectar():
    return sqlite3.connect("lury.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cliente TEXT NOT NULL,
        data_reserva TEXT NOT NULL,
        numero_pessoas INTEGER NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()

# Operações CRUD
def adicionar_reserva(nome_cliente, data_reserva, numero_pessoas):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        INSERT INTO reservas (nome_cliente, data_reserva, numero_pessoas)
        VALUES (?, ?, ?)
        """, (nome_cliente, data_reserva, numero_pessoas))
        conexao.commit()
        print("Reserva criada com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar reserva: {e}")
    finally:
        conexao.close()

def listar_reservas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM reservas")
        reservas = cursor.fetchall()
        if not reservas:
            print("Nenhuma reserva encontrada.")
        return reservas
    except Exception as e:
        print(f"Erro ao listar reservas: {e}")
        return []
    finally:
        conexao.close()

def atualizar_reserva(id_reserva, nome_cliente, data_reserva, numero_pessoas):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("""
        UPDATE reservas 
        SET nome_cliente = ?, data_reserva = ?, numero_pessoas = ?
        WHERE id = ?
        """, (nome_cliente, data_reserva, numero_pessoas, id_reserva))
        conexao.commit()
        print("Reserva atualizada com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar reserva: {e}")
    finally:
        conexao.close()

def excluir_reserva(id_reserva):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM reservas WHERE id = ?", (id_reserva,))
        conexao.commit()
        print("Reserva excluída com sucesso!")
    except Exception as e:
        print(f"Erro ao excluir reserva: {e}")
    finally:
        conexao.close()

# Menu
def menu():
    while True:
        print("\nSistema de Reservas - Lury")
        print("1. Adicionar reserva")
        print("2. Listar reservas")
        print("3. Atualizar reserva")
        print("4. Excluir reserva")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            data = input("Data da reserva (YYYY-MM-DD): ")
            try:
                pessoas = int(input("Quantidade de pessoas: "))
                adicionar_reserva(nome, data, pessoas)
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "2":
            reservas = listar_reservas()
            for reserva in reservas:
                print(f"ID: {reserva[0]}, Nome: {reserva[1]}, Data: {reserva[2]}, Pessoas: {reserva[3]}")
        elif opcao == "3":
            try:
                id_reserva = int(input("ID da reserva a atualizar: "))
                nome = input("Novo nome do cliente: ")
                data = input("Nova data da reserva (YYYY-MM-DD): ")
                pessoas = int(input("Novo número de pessoas: "))
                atualizar_reserva(id_reserva, nome, data, pessoas)
            except ValueError:
                print("Por favor, insira valores válidos.")
        elif opcao == "4":
            try:
                id_reserva = int(input("ID da reserva a excluir: "))
                excluir_reserva(id_reserva)
            except ValueError:
                print("Por favor, insira um ID válido.")
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicializar sistema
criar_tabela()
menu()