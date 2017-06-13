from flask import Flask, render_template, json, request, redirect, session
from flask import Markup
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
from flask import session

mysql = MySQL()
app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.secret_key = 'My secret key?'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'datavizdemo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/chart')
def chart():
    legend = "Tempature by Month"
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute("SELECT month from temperature")
        # data = cursor.fetchone()
        rows = cursor.fetchall()
        labels = list()
        i = 0
        for row in rows:
            labels.append(row[i])
        
        cursor.execute("SELECT temperature from temperature")
        rows = cursor.fetchall()
        # Convert query to objects of key-value pairs
        values = list()
        i = 0
        for row in rows:
            values.append(row[i])
        cursor.close()
        conn.close()
        
    except:
        print "Error: unable to fetch items"    

    return render_template('chart.html', values=values, labels = labels, legend=legend)

@app.route('/chart2')
def chart2():
    legend = "Tempature by Month"
    # Python list to be passed to the front-end html template 
    # labels = ["January","February","March","April","May","June","July","August"]
    # values = [10,9,8,7,6,4,7,8]
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute("SELECT month from temperature")
        # data = cursor.fetchone()
        rows = cursor.fetchall()
        labels = list()
        i = 0
        for row in rows:
            labels.append(row[i])
        
        cursor.execute("SELECT temperature from temperature")
        rows = cursor.fetchall()
        # Convert query to objects of key-value pairs
        values = list()
        i = 0
        for row in rows:
            values.append(row[i])
        cursor.close()    
        conn.close()
        
    except:
        print "Error: unable to fetch items"
    return render_template('chart2.html', values=values, labels = labels, legend=legend)

@app.route('/chart3')
def chart3():
    legend = "Tempature by Month"
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute("SELECT month, temperature, color from temperature")
        rows = cursor.fetchall()
        dataitems = list()
        fld = {} 
        i = 0       
        ##################################
        for row in rows:
            fld['month'] = row[0]
            fld['temperature'] = row[1]
            fld['color'] = row[2]
            dataitems.append(fld.copy()) 
        ##################################
        # print dataitems
        cursor.close()
        conn.close()
        # original json object
        # dataitems = [{"month": 'Jan', "temperature": 20, "color":'##3498db'},{"month": 'Feb', "temperature": 15, "color":'#e74c3c'}]
        # return render_template('chart3.html', dataitems=dataitems)
    except:
        print "Error: unable to fetch items"
    return render_template('chart3.html', dataitems=dataitems)


@app.route('/chart4')
def chart4():
    # original json object
    # markers = [
    #       {
    #         "name": "Victoria Peak",
    #         "url": "https://en.wikipedia.org/wiki/Victoria_Peak",
    #         "lat": 22.2759,
    #         "lng": 114.1455
    #       },
    #       {
    #         "name": "Happy Valley",
    #         "url": "https://en.wikipedia.org/wiki/Happy_Valley,_Hong_Kong",
    #         "lat": 22.2684,
    #         "lng": 114.1865
    #       }
    # ]
    conn = mysql.connect()
    cursor =conn.cursor()
    try:
        cursor.execute("SELECT name, url, lat, lng from destination")
        rows = cursor.fetchall()
        markers = list()
        fld = {} 
        i = 0       
        ##################################
        for row in rows:
            fld['name'] = row[0]
            fld['url'] = row[1]
            fld['lat'] = row[2]
            fld['lng'] = row[3]
            markers.append(fld.copy()) 
        ##################################
        # print dataitems
        cursor.close()
        conn.close()
        # original json object
        # dataitems = [{"month": 'Jan', "temperature": 20, "color":'##3498db'},{"month": 'Feb', "temperature": 15, "color":'#e74c3c'}]
        # return render_template('chart3.html', dataitems=dataitems)
    except:
        print "Error: unable to fetch items"
    return render_template('chart4.html',markers=markers)    

if __name__ == "__main__":
    app.run(port=5002)
