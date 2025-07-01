# app.py (versão reestruturada)

import sqlite3
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-chave-secreta-muito-dificil'

@app.template_filter('datetimeformat')
def format_datetime(value, format='%d/%m/%Y %H:%M'):
    """Formata uma string de data UTC para o formato brasileiro (UTC-3)."""
    if value is None:
        return ""
    utc_dt = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    local_dt = utc_dt - datetime.timedelta(hours=3)
    return local_dt.strftime(format)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# A rota home agora é mais simples, apenas lê os dados da tabela equipamentos
@app.route('/')
def home():
    conn = get_db_connection()
    equipamentos = conn.execute('SELECT * FROM equipamentos ORDER BY id DESC;').fetchall()
    conn.close()
    return render_template('index.html', equipamentos=equipamentos)

# Rota CREATE atualizada para os novos campos
@app.route('/create', methods=['POST'])
def create():
    projeto = request.form.get('projeto')
    usuario = request.form.get('usuario')
    olt_hostname = request.form.get('olt_hostname')
    olt_ip = request.form.get('olt_ip')
    slot = request.form.get('slot')
    porta = request.form.get('porta')
    ont_id = request.form.get('ont_id')
    serial_gpon = request.form.get('serial_gpon')
    tipo_cliente = request.form.get('tipo_cliente')
    tipo_servico = request.form.get('tipo_servico')
    svlan = request.form.get('svlan')
    cvlan = request.form.get('cvlan')
    status = request.form.get('status')
    observacao = request.form.get('observacao')

    conn = get_db_connection()
    conn.execute("""
        INSERT INTO equipamentos 
        (projeto, usuario, olt_hostname, olt_ip, slot, porta, ont_id, serial_gpon, tipo_cliente, tipo_servico, svlan, cvlan, status, observacao) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (projeto, usuario, olt_hostname, olt_ip, slot, porta, ont_id, serial_gpon, tipo_cliente, tipo_servico, svlan, cvlan, status, observacao))
    conn.commit()
    conn.close()
    
    flash('Equipamento cadastrado com sucesso!', 'success')
    return redirect(url_for('home'))

# A rota DELETE continua a mesma
@app.route('/delete', methods=['POST'])
def delete():
    id_para_apagar = request.form.get('id')
    conn = get_db_connection()
    conn.execute('DELETE FROM equipamentos WHERE id = ?', (id_para_apagar,))
    conn.commit()
    conn.close()
    flash('Equipamento apagado com sucesso!', 'danger')
    return redirect(url_for('home'))

# A rota UPDATE (para mostrar a página de edição) continua a mesma
@app.route('/update/<int:id>')
def update(id):
    conn = get_db_connection()
    equipamento = conn.execute('SELECT * FROM equipamentos WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('update.html', equipamento=equipamento)

# Rota PROCESS_UPDATE atualizada para os novos campos
@app.route('/process_update/<int:id>', methods=['POST'])
def process_update(id):
    projeto = request.form.get('projeto')
    usuario = request.form.get('usuario')
    olt_hostname = request.form.get('olt_hostname')
    olt_ip = request.form.get('olt_ip')
    slot = request.form.get('slot')
    porta = request.form.get('porta')
    ont_id = request.form.get('ont_id')
    serial_gpon = request.form.get('serial_gpon')
    tipo_cliente = request.form.get('tipo_cliente')
    tipo_servico = request.form.get('tipo_servico')
    svlan = request.form.get('svlan')
    cvlan = request.form.get('cvlan')
    status = request.form.get('status')
    observacao = request.form.get('observacao')

    conn = get_db_connection()
    conn.execute("""
        UPDATE equipamentos SET 
        projeto = ?, usuario = ?, olt_hostname = ?, olt_ip = ?, slot = ?, porta = ?, ont_id = ?, 
        serial_gpon = ?, tipo_cliente = ?, tipo_servico = ?, svlan = ?, cvlan = ?, status = ?, observacao = ?
        WHERE id = ?
        """,
        (projeto, usuario, olt_hostname, olt_ip, slot, porta, ont_id, serial_gpon, tipo_cliente, tipo_servico, svlan, cvlan, status, observacao, id))
    conn.commit()
    conn.close()

    flash('Equipamento atualizado com sucesso!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
