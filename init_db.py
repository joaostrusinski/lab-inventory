# init_db.py (versão simplificada)

import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Inserimos os dados de exemplo sem nenhuma referência a cenários.
cur.execute("INSERT INTO equipamentos (olt, gpon, status, observacao) VALUES (?, ?, ?, ?)",
            ('CTA_LAB_GPON_VLAN_116', 'TLCM00005FA0', 'Disponível', 'Equipamento de prateleira')
            )

cur.execute("INSERT INTO equipamentos (olt, gpon, status, observacao) VALUES (?, ?, ?, ?)",
            ('CTA_LAB_GPON_VLAN_116', 'ASKY001294EF', 'Em Uso', 'Alocado para o cenário de Teste XYZ')
            )

connection.commit()
connection.close()

print("Banco de dados simplificado e inicializado com sucesso!")
