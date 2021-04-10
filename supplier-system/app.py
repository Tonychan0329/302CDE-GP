from flask import Flask, render_template, request, session, redirect, url_for, send_file
import pymysql

app = Flask(__name__)
app.secret_key = 'development key'

db = pymysql.connect(host = "localhost", user = "root", password ="", database = "supplier", port=8081)

@app.route("/login", methods=['POST', 'GET'])
@app.route("/")
def login():
	error = ''
	if request.method == 'POST':
		email = request.form["email"]
		pwd = request.form["pwd"]

		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		cursor.execute('SELECT email, pwd FROM user WHERE email = %s AND pwd = %s', (email,pwd))
		users = cursor.fetchone()

		if users:
			session['email'] = email
			session['pwd'] = pwd
			return render_template('home.html')
		else:
			error = 'Your password or email is not true, please try again!'
			return render_template('login.html', error = error)
	return render_template('login.html')
	db.close()

@app.route("/logout")
def logout():
	return render_template('login.html')

@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/order", methods=['POST', 'GET'])
def order():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM `orders`")
	data = cursor.fetchall()

	if request.method == "POST":
		order_id = request.form["order_id"]

		cursor = db.cursor()
		cursor.execute('SELECT * FROM `orders` WHERE order_id = %s',(order_id))
		data = cursor.fetchall()

		return render_template('order.html', data = data)

	return render_template('order.html', data = data)

@app.route("/inventory", methods=['POST', 'GET'])
def inventory():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM inventory")
	data = cursor.fetchall()

	if request.method == "POST":
		item_no = request.form["item_no"]

		cursor = db.cursor()
		cursor.execute('SELECT * FROM inventory WHERE item_no = %s',(item_no))
		data = cursor.fetchall()

		return render_template('inventory.html', data = data)

	return render_template('inventory.html', data = data)

@app.route("/update")
def update():
	order_id = request.args.get('order_id')
	cursor = db.cursor()
	cursor.execute("SELECT * FROM `orders` WHERE order_id = %s",str(order_id))
	order = cursor.fetchall()

	return render_template('update.html', order = order)

@app.route("/update_email")
def update_email():
	return render_template('update_email.html')

@app.route("/update_complet")
def update_complet():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM `order`")
	data = cursor.fetchall()

	return render_template('update_complet.html', data = data)

@app.route("/reple_order", methods=['POST', 'GET'])
def reple_order():
	cursor = db.cursor()
	cursor.execute("SELECT * FROM reple_order")
	data = cursor.fetchall()
	
	if request.method == "POST":
		item_no = request.form["item_no"]

		cursor = db.cursor()
		cursor.execute('SELECT * FROM reple_order WHERE item_no = %s',(item_no))
		data = cursor.fetchall()

		return render_template('reple_order.html', data = data)

	return render_template('reple_order.html', data = data)	

@app.route("/invoice",methods=['POST', 'GET'])
def invoice():
	cursor = db.cursor()
	cursor.execute("SELECT id, shop FROM reple_order")
	data = cursor.fetchall()
	return render_template('invoice.html', data = data)

@app.route("/invoice_content")
def invoice_content():
	id = request.args.get('id')
	cursor = db.cursor()
	cursor.execute("SELECT a.id, a.item, a.type, a.supply_demand, a.shop ,a.date, b.price FROM reple_order a, inventory b  WHERE id = %s and  a.item = b.item and a.type = b.item_type",str(id))
	data = cursor.fetchall()
	totalPrice = 0
	for row in data:
		totalPrice =  int(row[3])*int(row[6])
	return render_template('invoice_content.html', data = data, totalPrice= totalPrice)



if __name__ == '__main__':
	app.run(debug = True)