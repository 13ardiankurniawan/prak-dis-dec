from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    # Menggunakan localhost (127.0.0.1) karena diakses dari luar container (Windows)
    conn = psycopg2.connect(
        host='127.0.0.1',
        database='yugabyte',
        user='yugabyte',
        password='',
        port='5433'
    )
    return conn

@app.route('/api/mahasiswa', methods=['GET'])
def get_mahasiswa():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, nama, jurusan FROM mahasiswa;')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        # Format data menjadi JSON list
        data = [{'id': r[0], 'nama': r[1], 'jurusan': r[2]} for r in rows]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/matakuliah', methods=['GET'])
def get_matakuliah():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT id, nama_mk, sks FROM mata_kuliah;')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        # Format data menjadi JSON list
        data = [{'id': r[0], 'nama_mk': r[1], 'sks': r[2]} for r in rows]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Berjalan di port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)