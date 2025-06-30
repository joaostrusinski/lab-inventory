-- Deleta a tabela 'equipamentos' se ela já existir, para evitar erros.
DROP TABLE IF EXISTS equipamentos;

-- Cria a tabela 'equipamentos' na sua forma final e simplificada.
CREATE TABLE equipamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    olt TEXT NOT NULL,
    gpon TEXT NOT NULL,
    slot INTEGER,
    porta INTEGER,
    id_onu INTEGER,
    cvlan INTEGER,
    vlan_rede INTEGER,
    vlan_voip INTEGER,
    vlan_video INTEGER,
    observacao TEXT,
    status TEXT NOT NULL DEFAULT 'Disponível',
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
