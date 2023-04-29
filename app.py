import psycopg2
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort


# Connect to the PostgreSQL database
def get_db_connection():
	conn = psycopg2.connect(
		host="localhost",
		database="fec",
		user="postgres",
		password="sand")
	return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


app = Flask(__name__)

@app.route('/candidates', methods=['GET'])
def candidates():
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

    return render_template('candidates.html', candidates=candidates_a[1:10], navbar1="create candidate",navbar2='none',)


@app.route('/')
def index():
    return render_template('index.html', posts=[])


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_candidate(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/delete/<int:id>', methods=('POST',))
def delete_candidate(id):
    # post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM candidate WHERE CAND_ID = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


# candidates()

if __name__ == '__main__':
  app.run(debug=True)