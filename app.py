import psycopg2
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_toastr import Toastr

# Connect to the PostgreSQL database
def get_db_connection():
	conn = psycopg2.connect(
		host="localhost",
		database="fec",
		user="postgres",
		password="sand")
	return conn

app = Flask(__name__)
toastr = Toastr(app)

# @app.route('/candidate/<int:id>', methods=['GET'])
def get_candidate(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql_select_candidate = "SELECT * FROM candidate WHERE CAND_ID = %s"
    cursor.execute(sql_select_candidate, (id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        abort(404)
    candidate = {
        'id': row[0],
        'name': row[1],
        'party_affiliation': row[2],
        'election_year': row[3],
        'office_state': row[4],
        'office': row[5],
        'office_district': row[6],
        'ici': row[7],
        'status': row[8],
        'pcc': row[9],
        'st1': row[10],
        'st2': row[11],
        'city': row[12],
        'st': row[13],
        'zip': row[14]
    }
    return candidate




@app.route('/candidates', methods=['GET'])
def get_all_candidates():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Retrieve all candidates from the database
    candidates_a = []
    sql_select_candidates = "SELECT * FROM candidate"
    cursor.execute(sql_select_candidates)
    rows = cursor.fetchall()
    for row in rows:
        candidate = {
			'id': row[0],
			'name': row[1],
			'party_affiliation': row[2],
			'election_year': row[3],
			'office_state': row[4],
			'office': row[5],
			'office_district': row[6],
			'ici': row[7],
			'status': row[8],
			'pcc': row[9],
			'st1': row[10],
			'st2': row[11],
			'city': row[12],
			'st': row[13],
			'zip': row[14]
   		}
        candidates_a.append(candidate)

    return render_template('candidates/candidates.html', candidates=candidates_a[-10:], navbar1="create candidate", navbar2='none',navbar1Link=url_for("create_candidate"),)


@app.route('/')
def index():
    return render_template('index.html', navbar1Link=url_for("index"),)


# @app.route('/<int:post_id>')
# def post(post_id):
#     post = get_candidate(post_id)
#     return render_template('post.html', post=post)


@app.route('/candidates/create', methods=('GET', 'POST'))
def create_candidate():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        party_affiliation = request.form['party_affiliation']
        election_year = request.form['election_year']
        office_state = request.form['office_state']
        office = request.form['office']
        office_district = request.form['office_district']
        ici = request.form['ici']
        status = request.form['status']
        pcc = request.form['pcc']
        st1 = request.form['st1']
        st2 = request.form['st2']
        city = request.form['city']
        state = request.form['st']
        zip_code = request.form['zip']
        sql_insert_candidate = "INSERT INTO candidate (CAND_ID, CAND_NAME, CAND_PTY_AFFILIATION, CAND_ELECTION_YR, CAND_OFFICE_ST, CAND_OFFICE, CAND_OFFICE_DISTRICT, CAND_ICI, CAND_STATUS, CAND_PCC, CAND_ST1, CAND_ST2, CAND_CITY, CAND_ST, CAND_ZIP) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        if not name:
            flash('Name is required!')
            return redirect(url_for('create_candidate'))
        elif not id:
            flash('ID is required!')
            return redirect(url_for('create_candidate'))
        elif not office:
            flash('Office is required!')
            return redirect(url_for('create_candidate'))
        elif not city:
            flash('City is required!')
            return redirect(url_for('create_candidate'))
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql_insert_candidate, (id, name, party_affiliation, election_year, office_state, office, office_district, ici, status, pcc, st1, st2, city, state, zip_code))
            conn.commit()
            conn.close()
            flash('"{}" was successfully created!'.format(name), 'success')
            return redirect(url_for('index'))

    return render_template('candidates/create_candidate.html',navbar1Link=url_for("create_candidate"),)


@app.route('/candidates/edit/<string:id>', methods=('GET', 'POST'))
def edit_candidate(id):
    candidate = get_candidate(id)

    if request.method == 'POST':
        name = request.form['name']
        party_affiliation = request.form['party_affiliation']
        election_year = request.form['election_year']
        office_state = request.form['office_state']
        office = request.form['office']
        office_district = request.form['office_district']
        ici = request.form['ici']
        status = request.form['status']
        pcc = request.form['pcc']
        st1 = request.form['st1']
        st2 = request.form['st2']
        city = request.form['city']
        state = request.form['st']
        zip_code = request.form['zip']

        if not name:
            flash('Name is required!')
        elif not office:
            flash('Office is required!')
        elif not city:
            flash('City is required!')
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE candidate SET CAND_NAME = %s, CAND_PTY_AFFILIATION = %s, CAND_ELECTION_YR = %s, CAND_OFFICE_ST = %s, CAND_OFFICE = %s, CAND_OFFICE_DISTRICT = %s, CAND_ICI = %s, CAND_STATUS = %s, CAND_PCC = %s, CAND_ST1 = %s, CAND_ST2 = %s, CAND_CITY = %s, CAND_ST = %s, CAND_ZIP = %s WHERE CAND_ID = %s",
                           (name, party_affiliation, election_year, office_state, office, office_district, ici, status, pcc, st1, st2, city, state, zip_code, id))
            conn.commit()
            cursor.close()
            conn.close()
            flash('"{}" was successfully edited!'.format(candidate['name']), 'success')
            return redirect(url_for('index'))

    return render_template('candidates/edit_candidate.html', candidate=candidate, navbar1Link=url_for("edit_candidate", id=id ),)

@app.route('/candidates/delete/<string:id>', methods=['GET', 'POST'])
def delete_candidate(id):
    candidate = get_candidate(id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM candidate WHERE CAND_ID = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('"{}" was successfully deleted!'.format(candidate['name']), 'success')
    return redirect(url_for('index'),navbar1Link=url_for("index"),)


import os

app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'memcached'
if __name__ == '__main__':
    app.run(debug=True)
	# app.run()