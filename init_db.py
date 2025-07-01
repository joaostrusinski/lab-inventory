# init_db.py (Nova Estrutura)

import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Inserimos um equipamento de exemplo com os novos campos
cur.execute("""
    INSERT INTO equipamentos 
    (projeto, usuario, olt_hostname, olt_ip, slot, porta, ont_id, serial_gpon, tipo_cliente, tipo_servico, svlan, cvlan, status, observacao) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        'Projeto Alpha', 'João Silva', 'OLT_LAB_01', '10.20.30.40', 1, 4, 13, 
        'TLCM00005FA0', 'B2B', 'INTERNET', 100, 200, 'Em Uso', 'Teste inicial do novo layout'
    )
)

# Inserimos um segundo equipamento de exemplo
cur.execute("""
    INSERT INTO equipamentos 
    (projeto, usuario, olt_hostname, olt_ip, slot, porta, ont_id, serial_gpon, tipo_cliente, tipo_servico, svlan, cvlan, status, observacao) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        'Projeto Beta', 'Maria Souza', 'OLT_LAB_02', '10.20.30.50', 2, 1, 5, 
        'ASKY001294EF', 'B2C', 'VOD', 101, 202, 'Disponível', 'Equipamento em prateleira'
    )
)

connection.commit()
connection.close()

print("Banco de dados reestruturado e inicializado com sucesso!")
