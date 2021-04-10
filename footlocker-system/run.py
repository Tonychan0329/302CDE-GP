from flask import Flask, render_template, redirect, url_for, request, session
import pymysql
import re
import datetime

app = Flask(__name__)
app.secret_key = 'random string'

db = pymysql.connect(host="localhost", user="root", password="", database="footlocker", port=8081)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/men')
def men():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products WHERE item_type = 'men'")
    detail = cursor.fetchall()
    return render_template('men.html', detail=detail)

@app.route('/women')
def women():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products WHERE item_type = 'women'")
    detail = cursor.fetchall()
    return render_template('women.html', detail=detail)

@app.route('/kids')
def kids():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products WHERE item_type = 'kids'")
    detail = cursor.fetchall()
    return render_template('kids.html', detail=detail)

@app.route('/new_season')
def new_season():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products WHERE item_type = 'newseason'")
    detail = cursor.fetchall()
    return render_template('new_season.html', detail=detail)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = db.cursor()
        cursor.execute("SELECT * FROM customers WHERE username = '{0}' AND password = '{1}'".format(username, password))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = username
            return redirect(url_for("index"))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST':
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = db.cursor()
        cursor.execute('SELECT * FROM customers WHERE username = %s', (username))
        user = cursor.fetchone()
        # If account exists show error and validation checks
        if user:
            msg = 'Account already exists!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            return 'Username must contain only characters and numbers!'
        elif not username or not password :
            return 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO customers (username, password) VALUES (%s, %s)', (username, password))
            db.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        return 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('signup.html', msg=msg)
    db.close()

@app.route('/user')
def user():
    if 'username' in session:
        username = session['username']
        cursor = db.cursor()
        cursor.execute("SELECT * FROM orders WHERE username = '{0}'".format(username))
        detail = cursor.fetchall()
        return render_template('user.html', detail=detail)
    return redirect(url_for('login'))

@app.route('/detail')
def detail():
    msg=''
    if 'username' in session:
        invoice = request.args.get('invoice')
        cursor = db.cursor()
        sql = ("SELECT a.order_id, b.id, b.product_id, b.size, c.item, c.image, c.price FROM orders a, order_detail b, products c WHERE b.order_id = a.order_id and b.product_id = c.item_no and a.order_id = '{0}'".format(invoice))
        cursor.execute(sql)
        detail = cursor.fetchall()
        try:          
            db.commit()
            msg = "successfully"
        except:
            db.rollback()
            msg = "error occured"
        return render_template('order_detail.html', msg=msg, detail=detail)
        cursor.close()
    else:
        return redirect(url_for('login'))

@app.route('/user_information', methods=['GET', 'POST'])
def user_information():
    if 'username' in session:
        username = session['username']
        cursor = db.cursor()
        cursor.execute("SELECT * FROM customers WHERE username = '{0}'".format(username))
        detail = cursor.fetchone()

        msg = ''
        error=''
        if request.method == 'POST':
            address = request.form['address']
            email = request.form['email']
            phone = request.form['phone']
            username = session['username']
                    
            cur = db.cursor()
            cur.execute("""UPDATE customers SET address = '{0}', email = '{1}', phone_no = '{2}' WHERE username = '{3}'""".format(address, email, phone, username))

            try:
                db.commit()
                msg = "Saved Successfully"
            except:
                db.rollback()
                error = "Error occured"
        return render_template('user_information.html', detail=detail, msg=msg, error=error)
        db.close()
    return redirect(url_for('login'))

@app.route('/inqirty', methods=['GET', 'POST'])
def inqirty():
    if 'username' in session:
        error = ''
        msg = ''
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            question = request.form['question']
                    
            cur = db.cursor()
            cur.execute("INSERT INTO inqirty (name, email, question) VALUES (%s, %s, %s)", (name, email, question))

            try:
                db.commit()
                msg = "Send Successfully"
            except:
                db.rollback()
                error = "Error occured"
        return render_template('inqirty.html', msg=msg, error=error)
        db.close()
    return redirect(url_for('login'))

@app.route('/setting', methods=['GET', 'POST'])
def setting():
    if 'username' in session:
        msg=''
        if request.method == "POST":
            oldPassword = request.form['oldpassword']
            newPassword = request.form['newpassword']
            
            cursor = db.cursor()
            cursor.execute("SELECT user_id, password FROM customers WHERE username = '" + session['username'] + "'")
            user_id, password = cursor.fetchone()
            if (password == oldPassword):
                try:
                    cursor.execute("UPDATE customers SET password = '{0}' WHERE user_id = '{1}'".format(newPassword, user_id))
                    db.commit()
                    msg="Changed successfully"
                except:
                    db.rollback()
                    msg = "Failed"
                return render_template("setting.html", msg=msg)
            else:
                msg = "Wrong password"
            
        return render_template("setting.html", msg=msg) 
        db.close()
    return redirect(url_for('login'))

@app.route('/shoppingcart')
def shoppingcart():
    if 'username' in session:
        cursor = db.cursor()
        cursor.execute("SELECT a.cart_id, b.item, b.image, b.price FROM cart a, products b where a.product_id = b.item_no and a.username = '" + session['username'] + "' ORDER BY a.cart_id  ")
        data = cursor.fetchall()
        totalPrice = 0
        now = datetime.date.today()
        for row in data:
            totalPrice += int(row[3])
        return render_template('shopping_cart.html', data = data, totalPrice = totalPrice, now =now)
    else:
        return redirect(url_for('login'))

@app.route('/addtocart', methods=['GET', 'POST'])
def addtocart():
    msg = ''
    if 'username' in session:
        if request.method == "POST":
            P_ID = request.form['product_id']
            size = request.form['size']
            username = session['username']
            cursor = db.cursor()
            try:
                sql = ("INSERT INTO cart (username, product_id, size) VALUES ('{0}', '{1}','{2}')".format(username, P_ID, size))      
                cursor.execute(sql)
                sql_1 = ("INSERT INTO order_detail (username, product_id, status, size) VALUES ('{0}', '{1}', 'unpayed', '{2}')".format(username, P_ID, size))
                cursor.execute(sql_1)
                db.commit()
                msg = "Added successfully"
            except:
                db.rollback()
                msg = "Error occured" 
        cursor.close()               
        return redirect(url_for('shoppingcart', msg = msg))
        
    return redirect(url_for('login'))

@app.route('/removefromcart')
def removefromcart():
    if 'username' in session:
        C_ID = request.args.get('C_ID')
        cursor = db.cursor()
        try:
            sql = ("DELETE FROM cart WHERE cart_id = '{0}'" .format(C_ID))
            cursor.execute(sql)
            sql_1 = ("DELETE FROM order_detail WHERE id = '{0}'" .format(C_ID))
            cursor.execute(sql_1)
            db.commit()
            msg = "removed successfully"
        except:
            db.rollback()
            msg = "error occured"
    cursor.close()
    return redirect(url_for('shoppingcart', msg= msg))

@app.route('/payment')
def payment():
    if 'username' in session:
        cursor = db.cursor()
        cursor.execute("SELECT a.cart_id, b.item, b.image, b.price FROM cart a, products b where a.product_id = b.item_no and a.username = '" + session['username'] + "' ORDER BY a.cart_id  ")
        data = cursor.fetchall()
        cursor.execute("SELECT * FROM orders WHERE status = 'unpayed' and username = '" + session['username'] + "'")
        data1 = cursor.fetchone()
        totalPrice = 0
        for row in data:
            totalPrice += int(row[3])
        return render_template('payment.html', data = data, totalPrice = totalPrice, data1=data1)
    else:
        return redirect(url_for('login'))

@app.route('/checkout', methods=["GET", "POST"])
def checkout():
    msg = ''
    if request.method == "POST":
        date = request.form['date']
        totalprice = request.form['totalprice']
        username = session['username']
        
        cursor = db.cursor()
        sql = ("insert into orders (username, date, totalprice, status) VALUES ('{0}', '{1}', '{2}', 'unpayed')".format(username, date, totalprice))      
        cursor.execute(sql)
        try:
            db.commit()
            msg = "order successfully"
        except:
            db.rollback()
            msg = "Error occured"
    return redirect(url_for('payment', msg = msg))
    db.close()

@app.route('/process', methods=['GET', 'POST'])
def process():
    msg = ''
    if request.method == "POST":
        order_id = request.form['order_id']
        username = session['username']
        
        cursor = db.cursor()
        sql_1 =("UPDATE order_detail SET order_id = '{0}' WHERE username = '{1}' and status = 'unpayed'".format(order_id, username))
        cursor.execute(sql_1)
        sql_3 =("UPDATE order_detail SET status = 'Payment Completed' WHERE status = 'unpayed'")
        cursor.execute(sql_3)
        sql_2 = ("UPDATE orders SET status = 'Payment Completed' WHERE username = '{0}'".format(username))
        cursor.execute(sql_2)
        sql_4 =("DELETE FROM cart WHERE username = '{0}'".format(username))
        cursor.execute(sql_4)
        try:
            db.commit()
            msg = "order successfully"
        except:
            db.rollback()
            msg = "Error occured"
    return redirect(url_for('user', msg = msg))
    db.close()

@app.route("/product")
def product():
    productId = request.args.get('productId')
    
    cursor = db.cursor()
    cursor.execute('SELECT * FROM products WHERE item_no = ' + productId)
    data = cursor.fetchone()
    return render_template("product.html", data=data)
    db.close()

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    session.pop('id', None)
    return render_template('index.html')

##########################################################################################################################

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST':
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = db.cursor()
        cursor.execute("SELECT * FROM admin WHERE admin_email = '{0}' AND admin_password = '{1}'".format(email, password))
        # Fetch one record and return result
        user = cursor.fetchone()
        # If account exists in accounts table in out database
        if user:
            #Create session data, we can access this data in other routes
            session['adminlogin'] = True
            session['adminemail'] = email
            return redirect(url_for("adminhome"))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('adminlogin.html', msg=msg)

@app.route("/adminlogout")
def adminlogout():
    session.pop('adminlogin', None)
    session.pop('adminemail', None)
    return render_template('adminlogin.html')

@app.route("/adminhome")
def adminhome():
    if 'adminlogin' in session:
	    return render_template('adminhome.html')
    return redirect(url_for('adminlogin'))

@app.route("/adminuser")
def adminuser():
    if 'adminlogin' in session:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM customers ")
        detail = cursor.fetchall()
        return render_template('adminuser.html', detail=detail)
    return redirect(url_for('adminlogin'))

@app.route("/adminorder")
def adminorder():
    if 'adminlogin' in session:
        cursor = db.cursor()
        cursor.execute("SELECT a.order_id, a.username, b.item, b.price, c.totalprice FROM order_detail a, products b, orders c where a.product_id = b.item_no and a.order_id = c.order_id ORDER BY a.order_id ")
        detail = cursor.fetchall()
        return render_template('adminorder.html', detail=detail)
    return redirect(url_for('adminlogin'))

@app.route("/adminproduct")
def adminproduct():
    if 'adminlogin' in session:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM products ")
        detail = cursor.fetchall()
        return render_template('adminproduct.html', detail=detail)
    return redirect(url_for('adminlogin'))

@app.route("/adminaddproduct")
def adminaddproduct():
    if 'adminlogin' in session:
        return render_template('adminaddproduct.html')
    return redirect(url_for('adminlogin'))

@app.route("/admin_add" , methods=['GET', 'POST'])
def admin_add():
    msg=''
    if request.method == "POST":
        itemtype = request.form['itemtype']
        item = request.form['item']
        price = request.form['price']
        size = request.form['size']
        
        cursor = db.cursor()
        sql =("insert into products (item_type, item, price, size) values ('{0}', '{1}', '{2}', '{3}')".format(itemtype, item, price, size))
        cursor.execute(sql)
        try:
            db.commit()
            msg = "order successfully"
        except:
            db.rollback()
            msg = "Error occured"
    return render_template('adminaddproduct.html', msg = msg)
    db.close()
    
@app.route("/adminwarehouse")
def adminwarehouse():
    if 'adminlogin' in session:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM warehouse ")
        detail = cursor.fetchall()
        return render_template('adminwarehouse.html', detail=detail)
    return redirect(url_for('adminlogin'))

@app.route("/adminreplen_submit", methods=['GET', 'POST'])
def adminreplen_submit():
    if 'adminlogin' in session:
        msg=''
        if request.method == "POST":
            item_name = request.form['item_name']
            item_type = request.form['item_type']
            stock = request.form['stock']
            shop = request.form['shop']
            
            cursor = db.cursor()
            cursor.execute("insert into replenishment (item_name, item_type, supply_demand, shop) values ('{0}', '{1}', '{2}', '{3}')".format(item_name, item_type, stock, shop))
            try:
                db.commit()
                msg = "order successfully"
            except:
                db.rollback()
                msg = "Error occured"
        return redirect(url_for('adminreplen_list', msg = msg))
        db.close()          
    return redirect(url_for('adminlogin'))  

@app.route("/adminreplen")
def adminreplen():
    if 'adminlogin' in session:
        item_no = request.args.get('item_no')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM warehouse WHERE item_no = '{0}'".format(item_no))
        data = cursor.fetchone()
        return render_template('adminreplen.html', data = data)
    return redirect(url_for('adminlogin'))   

@app.route("/adminreplen_list")
def adminreplen_list():
    if 'adminlogin' in session:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM replenishment")
        data = cursor.fetchall()
        cursor.close()
        return render_template('adminreplen_list.html', data = data)
    return redirect(url_for('adminlogin'))  
    

@app.route('/deletereplen')
def deletereplen():
    if 'adminlogin' in session:
        replen_id = request.args.get('replen_id')
        cursor = db.cursor()
        try:
            sql = ("DELETE FROM replenishment WHERE replen_id = '{0}'" .format(replen_id))
            cursor.execute(sql)
            db.commit()
            msg = "removed successfully"
        except:
            db.rollback()
            msg = "error occured"
        cursor.close()
        return redirect(url_for('adminreplen_list', msg= msg))
    return redirect(url_for('adminlogin'))  

@app.route('/deleteorder')
def deleteorder():
    if 'adminlogin' in session:
        order_id = request.args.get('order_id')
        cursor = db.cursor()
        try:
            sql = ("DELETE FROM orders WHERE order_id = '{0}'" .format(order_id))
            cursor.execute(sql)
            db.commit()
            msg = "removed successfully"
        except:
            db.rollback()
            msg = "error occured"
        cursor.close()
        return redirect(url_for('adminorder', msg= msg))
    return redirect(url_for('adminlogin'))  


@app.route('/deleteproduct')
def deleteproduct():
    if 'adminlogin' in session:
        product_id = request.args.get('product_id')
        cursor = db.cursor()
        try:
            sql = ("DELETE FROM products WHERE item_no = '{0}'" .format(product_id))
            cursor.execute(sql)
            db.commit()
            msg = "removed successfully"
        except:
            db.rollback()
            msg = "error occured"
        cursor.close()
        return redirect(url_for('adminproduct', msg= msg))
    return redirect(url_for('adminlogin'))  
    

@app.route('/delete_user_record')
def delete_user_record():
    if 'username' in session:
        order_id = request.args.get('order_id')
        username = session['username']
        cursor = db.cursor()
        try:
            sql = ("DELETE FROM orders WHERE order_id = '{0}' and username = '{1}'" .format(order_id, username))
            cursor.execute(sql)
            db.commit()
            msg = "removed successfully"
        except:
            db.rollback()
            msg = "error occured"
        cursor.close()
        return redirect(url_for('user', msg= msg))
    return redirect(url_for('login'))  

'''@app.route('/update_status', methods=['GET', 'POST'])
def update_status():
    if 'adminlogin' in session:
        msg=''
        if request.method == 'POST':
            replen_id = request.args.get('replen_id')
            status = request.form['status']
            cursor = db.cursor()
            cursor.execute("UPDATE replenishment SET status='{0}' WHERE replen_id = '{1}'".format(status, replen_id))
            try:
                db.commit()
                msg = "Saved Successfully"
            except:
                db.rollback()
                msg = "Error occured" 
        return redirect(url_for('adminreplen_list', msg=msg))
        cursor.close()
    else:
        return redirect(url_for('admin_login'))'''


if __name__ == '__main__':
    app.run(debug=True)