-- Deleta a tabela 'equipamentos' se ela já existir, para evitar erros.
DROP TABLE IF EXISTS equipamentos;

-- Cria a nova tabela 'equipamentos' com todas as novas colunas.
CREATE TABLE equipamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    projeto TEXT,
    usuario TEXT,
    olt_hostname TEXT,
    olt_ip TEXT,
    slot INTEGER,
    porta INTEGER,
    ont_id INTEGER,
    serial_gpon TEXT,
    tipo_cliente TEXT,
    tipo_servico TEXT,
    svlan INTEGER,
    cvlan INTEGER,
    status TEXT NOT NULL DEFAULT 'Disponível',
    observacao TEXT,
    data_criacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
