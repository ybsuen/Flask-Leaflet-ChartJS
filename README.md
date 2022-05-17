# Flask-Leaflet-ChartJS
This demonstration was inspired by a Python Flask and ChartJS tutorial hosted on pythonspot.com titled "Flask and great looking charts using Chart.js". What I added was the Leaflet map and MySQL integration so that the data array and object used for rendering the charts and map inside the HTML CANVAS and DIV area can be stored and retrieved from MySQL tables. By updating the values in the tables, the rendered map and charts can be updated dynamically.

## To Replicate the Demonstration
Setup MySQL database and tables by executing the SQL commands inside the "datavizdemo.sql" file.
Then run "sudo python app.py" at the command prompt. In the browser, type in "localhost:5002", which is the port number defined in the app.py file, to view the demo in local mode (Assuming the Python Flask web server is running). 
