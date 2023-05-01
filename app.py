import random
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


@app.route('/')
def index():
    return render_template('index.html', navbar1Link=url_for("index"),)


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

def get_all_candidate_ids():
    conn = get_db_connection()
    cursor = conn.cursor()
    candidates_a = []
    sql_select_candidates = "SELECT * FROM candidate"
    cursor.execute(sql_select_candidates)
    rows = cursor.fetchall()
    for row in rows:
        candidate = {
			'id': row[0],
			'name': row[1]
   		}
        candidates_a.append(candidate)
    conn.close()
    cursor.close()
    return candidates_a[-10:]

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
            return redirect(url_for('get_all_candidates'))

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
            return redirect(url_for('get_all_candidates'))

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
    return redirect(url_for('get_all_candidates'))


def get_committee(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql_select_committee = "SELECT * FROM committee WHERE CMTE_ID = %s"
    cursor.execute(sql_select_committee, (id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        abort(404)
    committee = {
			'cmte_id': row[0],
			'cmte_nm': row[1],
			'tres_nm': row[2],
			'cmte_st1': row[3],
			'cmte_st2': row[4],
			'cmte_city': row[5],
			'cmte_st': row[6],
			'cmte_zip': row[7],
			'cmte_dsgn': row[8],
			'cmte_tp': row[9],
			'cmte_pty_affiliation': row[10],
			'cmte_filing_freq': row[11],
			'org_tp': row[12],
			'connected_org_nm': row[13],
			'cand_id': row[14]
		}
    return committee


def get_all_committee_ids():
    conn = get_db_connection()
    cursor = conn.cursor()
    committees_a = []
    sql_select_committees = "SELECT * FROM committee"
    cursor.execute(sql_select_committees)
    rows = cursor.fetchall()
    for row in rows:
        committee = {
			'cmte_id': row[0],
   			'cmte_nm': row[1],
		}
        committees_a.append(committee)
    conn.close()
    cursor.close()
    return committees_a[-10:]


@app.route('/committees', methods=['GET'])
def get_all_committees():
    conn = get_db_connection()
    cursor = conn.cursor()
    committees_a = []
    sql_select_committees = "SELECT * FROM committee"
    cursor.execute(sql_select_committees)
    rows = cursor.fetchall()
    for row in rows:
        committee = {
			'cmte_id': row[0],
			'cmte_nm': row[1],
			'tres_nm': row[2],
			'cmte_st1': row[3],
			'cmte_st2': row[4],
			'cmte_city': row[5],
			'cmte_st': row[6],
			'cmte_zip': row[7],
			'cmte_dsgn': row[8],
			'cmte_tp': row[9],
			'cmte_pty_affiliation': row[10],
			'cmte_filing_freq': row[11],
			'org_tp': row[12],
			'connected_org_nm': row[13],
			'cand_id': row[14]
		}

        committees_a.append(committee)
    conn.close()
    return render_template('committees/committees.html', committees=committees_a[-10:], navbar1='create committee', navbar2='none', navbar1Link=url_for("create_committee"))

@app.route('/committees/create', methods=('GET', 'POST'))
def create_committee():
    if request.method == 'POST':
        cmte_id = request.form['cmte_id']
        cmte_name = request.form['cmte_nm']
        tres_name = request.form['tres_nm']
        cmte_st1 = request.form['cmte_st1']
        cmte_st2 = request.form['cmte_st2']
        cmte_city = request.form['cmte_city']
        cmte_st = request.form['cmte_st']
        cmte_zip = request.form['cmte_zip']
        cmte_dsgn = request.form['cmte_dsgn']
        cmte_tp = request.form['cmte_tp']
        cmte_pty_affiliation = request.form['cmte_pty_affiliation']
        cmte_filing_freq = request.form['cmte_filing_freq']
        org_tp = request.form['org_tp']
        connected_org_nm = request.form['connected_org_nm']
        cand_id = request.form['cand_id']
        sql_insert_committee = "INSERT INTO committee (CMTE_ID, CMTE_NM, TRES_NM, CMTE_ST1, CMTE_ST2, CMTE_CITY, CMTE_ST, CMTE_ZIP, CMTE_DSGN, CMTE_TP, CMTE_PTY_AFFILIATION, CMTE_FILING_FREQ, ORG_TP, CONNECTED_ORG_NM, CAND_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        if not cmte_name:
            flash('Committee name is required!')
            return redirect(url_for('create_committee'))
        elif not cmte_id:
            flash('Committee ID is required!')
            return redirect(url_for('create_committee'))
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql_insert_committee, (cmte_id, cmte_name, tres_name, cmte_st1, cmte_st2, cmte_city, cmte_st, cmte_zip, cmte_dsgn, cmte_tp, cmte_pty_affiliation, cmte_filing_freq, org_tp, connected_org_nm, cand_id))
            conn.commit()
            conn.close()
            flash('Committee "{}" was successfully created!'.format(cmte_name), 'success')
            return redirect(url_for('get_all_committees'))

    return render_template('committees/create_committee.html',navbar1Link=url_for("create_committee"), candidate_ids=get_all_candidate_ids())


@app.route('/committees/edit/<string:id>', methods=('GET', 'POST'))
def edit_committee(id):
    committee = get_committee(id)

    if request.method == 'POST':
        cmte_id = request.form['cmte_id']
        cmte_nm = request.form['cmte_nm']
        tres_nm = request.form['tres_nm']
        cmte_st1 = request.form['cmte_st1']
        cmte_st2 = request.form['cmte_st2']
        cmte_city = request.form['cmte_city']
        cmte_st = request.form['cmte_st']
        cmte_zip = request.form['cmte_zip']
        cmte_dsgn = request.form['cmte_dsgn']
        cmte_tp = request.form['cmte_tp']
        cmte_pty_affiliation = request.form['cmte_pty_affiliation']
        cmte_filing_freq = request.form['cmte_filing_freq']
        org_tp = request.form['org_tp']
        connected_org_nm = request.form['connected_org_nm']
        cand_id = request.form['cand_id']

        if not cmte_id:
            flash('Committee ID is required!')
        elif not cmte_nm:
            flash('Committee Name is required!')
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE committee SET CMTE_ID = %s, CMTE_NM = %s, TRES_NM = %s, CMTE_ST1 = %s, CMTE_ST2 = %s, CMTE_CITY = %s, CMTE_ST = %s, CMTE_ZIP = %s, CMTE_DSGN = %s, CMTE_TP = %s, CMTE_PTY_AFFILIATION = %s, CMTE_FILING_FREQ = %s, ORG_TP = %s, CONNECTED_ORG_NM = %s, CAND_ID = %s WHERE CMTE_ID = %s",
                           (cmte_id, cmte_nm, tres_nm, cmte_st1, cmte_st2, cmte_city, cmte_st, cmte_zip, cmte_dsgn, cmte_tp, cmte_pty_affiliation, cmte_filing_freq, org_tp, connected_org_nm, cand_id, id))
            conn.commit()
            cursor.close()
            conn.close()
            flash('"{}" was successfully edited!'.format(committee['cmte_nm']), 'success')
            return redirect(url_for('get_all_committees'))

    return render_template('committees/edit_committee.html', committee=committee, navbar1Link=url_for("edit_committee", id=id), candidate_ids=get_all_candidate_ids())

@app.route('/committees/delete/<string:id>', methods=['GET', 'POST'])
def delete_committee(id):
    committee = get_committee(id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM committee WHERE CMTE_ID = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('"{}" was successfully deleted!'.format(committee['cmte_nm']), 'success')
    return redirect(url_for('get_all_committees'))


def get_candidate_committee(linkage_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql_select_candidate_committee = "SELECT * FROM candidate_committee WHERE LINKAGE_ID = %s"
    cursor.execute(sql_select_candidate_committee, (linkage_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        abort(404)
    candidate_committee = {
			'cand_id': row[0],
			'cand_election_yr': row[1],
			'fec_election_yr': row[2],
			'cmte_id': row[3],
			'cmte_tp': row[4],
			'cmte_dsgn': row[5],
			'linkage_id': row[6]
		}
    return candidate_committee



@app.route('/candidates_committees', methods=['GET'])
def get_all_candidates_committees():
    conn = get_db_connection()
    cursor = conn.cursor()
    candidates_committees_a = []
    sql_select_candidates_committees = "SELECT * FROM candidate_committee"
    cursor.execute(sql_select_candidates_committees)
    rows = cursor.fetchall()
    for row in rows:
        candidates_committee = {
			'cand_id': row[0],
			'cand_election_yr': row[1],
			'fec_election_yr': row[2],
			'cmte_id': row[3],
			'cmte_tp': row[4],
			'cmte_dsgn': row[5],
			'linkage_id': row[6]
		}
        candidates_committees_a.append(candidates_committee)
    conn.close()
    return render_template('candidates_committees/candidates_committees.html', candidates_committees=candidates_committees_a[-10:], navbar1='create candidate committee', navbar2='none', navbar1Link=url_for("create_candidate_committee"))


@app.route('/candidates_committees/create', methods=('GET', 'POST'))
def create_candidate_committee():
    if request.method == 'POST':
        cand_id = request.form['cand_id']
        cand_election_yr = request.form['cand_election_yr']
        fec_election_yr = request.form['fec_election_yr']
        cmte_id = request.form['cmte_id']
        cmte_tp = request.form['cmte_tp']
        cmte_dsgn = request.form['cmte_dsgn']
        linkage_id = random.randint(1000000, 9999999)
        
        sql_insert_candidate_committee = "INSERT INTO candidate_committee (CAND_ID, CAND_ELECTION_YR, FEC_ELECTION_YR, CMTE_ID, CMTE_TP, CMTE_DSGN, LINKAGE_ID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        if not cand_id:
            flash('Candidate ID is required!')
            return redirect(url_for('create_candidate_committee'))
        elif not cmte_id:
            flash('Committee ID is required!')
            return redirect(url_for('create_candidate_committee'))
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(sql_insert_candidate_committee, (cand_id, cand_election_yr, fec_election_yr, cmte_id, cmte_tp, cmte_dsgn, linkage_id))
            conn.commit()
            conn.close()
            flash('Candidate-Committee link was successfully created!', 'success')
            return redirect(url_for('get_all_candidates_committees'))

    return render_template('candidates_committees/create_candidate_committee.html',navbar1Link=url_for("create_candidate_committee"), committees_ids=get_all_committee_ids(), candidate_ids=get_all_candidate_ids())



@app.route('/candidates_committees/edit/<string:id>', methods=('GET', 'POST'))
def edit_candidate_committee(id):
    candidate_committee = get_candidate_committee(id)

    if request.method == 'POST':
        cand_id = request.form['cand_id']
        cand_election_yr = request.form['cand_election_yr']
        fec_election_yr = request.form['fec_election_yr']
        cmte_id = request.form['cmte_id']
        cmte_tp = request.form['cmte_tp']
        cmte_dsgn = request.form['cmte_dsgn']

        if not cand_id:
            flash('Candidate ID is required!')
        elif not cmte_id:
            flash('Committee ID is required!')
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE candidate_committee SET CAND_ID = %s, CAND_ELECTION_YR = %s, FEC_ELECTION_YR = %s, CMTE_ID = %s, CMTE_TP = %s, CMTE_DSGN = %s WHERE LINKAGE_ID = %s",
                           (cand_id, cand_election_yr, fec_election_yr, cmte_id, cmte_tp, cmte_dsgn, id))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Candidate-Committee link was successfully edited!', 'success')
            return redirect(url_for('get_all_candidates_committees'))

    return render_template('candidates_committees/edit_candidate_committee.html', candidate_committee=candidate_committee, navbar1Link=url_for("edit_candidate_committee", id=id), committees_ids=get_all_committee_ids(), candidate_ids=get_all_candidate_ids())

@app.route('/candidates_committees/delete/<string:id>', methods=('GET', 'POST'))
def delete_candidate_committee(id):
    candidate_committee = get_candidate_committee(id)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM candidate_committee WHERE LINKAGE_ID = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('"{}" was successfully deleted!'.format(candidate_committee['linkage_id']), 'success')
    return redirect(url_for('get_all_candidates_committees'))


import os

app.secret_key = os.urandom(24)
app.config['SESSION_TYPE'] = 'memcached'
if __name__ == '__main__':
    app.run(debug=True)
