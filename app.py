# app.py (versão simplificada)

import sqlite3
import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-chave-secreta-muito-dificil'

@app.template_filter('datetimeformat')
def format_datetime(value, format='%d/%m/%Y %H:%M'):
    if value is None:
        return ""
    utc_dt = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    local_dt = utc_dt - datetime.timedelta(hours=3)
    return local_dt.strftime(format)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    equipamentos = conn.execute('SELECT * FROM equipamentos ORDER BY id DESC;').fetchall()
    conn.close()
    # Não passamos mais a lista de cenários
    return render_template('index.html', equipamentos=equipamentos)

@app.route('/create', methods=['POST'])
def create():
    olt = request.form.get('olt')
    gpon = request.form.get('gpon')
    slot = request.form.get('slot')
    porta = request.form.get('porta')
    id_onu = request.form.get('id_onu')
    cvlan = request.form.get('cvlan')
    vlan_rede = request.form.get('vlan_rede')
    vlan_voip = request.form.get('vlan_voip')
    vlan_video = request.form.get('vlan_video')
    observacao = request.form.get('observacao')
    status = request.form.get('status')

    conn = get_db_connection()
    # O comando INSERT agora é mais simples
    conn.execute('INSERT INTO equipamentos (olt, gpon, slot, porta, id_onu, cvlan, vlan_rede, vlan_voip, vlan_video, observacao, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                 (olt, gpon, slot, porta, id_onu, cvlan, vlan_rede, vlan_voip, vlan_video, observacao, status))
    conn.commit()
    conn.close()
    
    flash('Equipamento cadastrado com sucesso!', 'success')
    return redirect(url_for('home'))

@app.route('/delete', methods=['POST'])
def delete():
    id_para_apagar = request.form.get('id')
    conn = get_db_connection()
    conn.execute('DELETE FROM equipamentos WHERE id = ?', (id_para_apagar,))
    conn.commit()
    conn.close()
    flash('Equipamento apagado com sucesso!', 'danger')
    return redirect(url_for('home'))

@app.route('/update/<int:id>')
def update(id):
    conn = get_db_connection()
    equipamento = conn.execute('SELECT * FROM equipamentos WHERE id = ?', (id,)).fetchone()
    conn.close()
    # Não passamos mais a lista de cenários
    return render_template('update.html', equipamento=equipamento)

@app.route('/process_update/<int:id>', methods=['POST'])
def process_update(id):
    olt = request.form.get('olt')
    gpon = request.form.get('gpon')
    slot = request.form.get('slot')
    porta = request.form.get('porta')
    id_onu = request.form.get('id_onu')
    cvlan = request.form.get('cvlan')
    vlan_rede = request.form.get('vlan_rede')
    vlan_voip = request.form.get('vlan_voip')
    vlan_video = request.form.get('vlan_video')
    observacao = request.form.get('observacao')
    status = request.form.get('status')

    conn = get_db_connection()
    # O comando UPDATE agora é mais simples
    conn.execute('UPDATE equipamentos SET olt = ?, gpon = ?, slot = ?, porta = ?, id_onu = ?, cvlan = ?, vlan_rede = ?, vlan_voip = ?, vlan_video = ?, observacao = ?, status = ? WHERE id = ?',
                (olt, gpon, slot, porta, id_onu, cvlan, vlan_rede, vlan_voip, vlan_video, observacao, status, id))
    conn.commit()
    conn.close()

    flash('Equipamento atualizado com sucesso!', 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
