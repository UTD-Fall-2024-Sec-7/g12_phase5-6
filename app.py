from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datastorage import datastorage
from transactionClass import transactionClass
from newsHandler import newsHandler
import json


app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Secret key for session management

# Initialize services
storage = datastorage()
transaction_service = transactionClass()
news_service = newsHandler("ct1nmb9r01qoprggpfk0ct1nmb9r01qoprggpfkg")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if storage.register_user(username, password):
            return redirect(url_for('login'))
        return render_template('register.html', message="Username already exists.")
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if storage.validate_login(username, password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        return render_template('login.html', message="Invalid username or password.")
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']  # Get the logged-in user's username
    followed = storage.get_followed_congressmen(username)  # Retrieve followed congressmen for the user

    return render_template('dashboard.html', username=username, followed=followed)



@app.route('/follow', methods=['POST'])
def follow():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    congressman = request.form['congressman']
    if storage.follow_congressman(username, congressman):
        trades = transaction_service.get_recent_trades(congressman)
        return render_template('dashboard.html', trades=trades, message=f"You are now following {congressman}.")
    return render_template('dashboard.html', message="Failed to follow congressman.")


@app.route('/news', methods=['GET'])
def news():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    category = request.args.get('category', 'general')  # Default to "general"
    news_service = newsHandler("ct1nmb9r01qoprggpfk0ct1nmb9r01qoprggpfkg")
    news_items = news_service.getNews(category)  # Fetch news from API
    
    return render_template('news.html', news=news_items)



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/news')
def view_news():
    if 'username' not in session:
        return redirect(url_for('login'))
    category = request.args.get('category', 'general')
    news_items = news_service.getNews(category)
    return render_template('news.html', news=news_items)



@app.route('/follow_congressmen', methods=['GET', 'POST'])
def follow_congressmen():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    
    if request.method == 'POST':
        # Get the selected congressman from the form
        congressman = request.form.get('congressman')
        if congressman:
            if storage.follow_congressman(username, congressman):
                message = f"You are now following {congressman}!"
            else:
                message = "Failed to follow congressman."
        else:
            message = "Please select a congressman."
        # Get updated list of followed congressmen
        followed = storage.get_followed_congressmen(username)
        return render_template('follow_congressmen.html', all_congressmen=storage.list_all_congressmen(), followed=followed, message=message)

    # GET request: Show the form
    followed = storage.get_followed_congressmen(username)
    return render_template('follow_congressmen.html', all_congressmen=storage.list_all_congressmen(), followed=followed)

@app.route('/recent_trades')
def recent_trades():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    followed = storage.get_followed_congressmen(username)  # Get congressmen the user follows

    all_trades = []
    for congressman in followed:
        try:
            trades = transaction_service.get_recent_trades(congressman)  # Use the same method as interactive query
            if isinstance(trades, list):  # Ensure trades are a list
                for trade in trades:
                    trade['congressman'] = congressman  # Add congressman to each trade
                all_trades.extend(trades)
        except Exception as e:
            print(f"Error fetching trades for {congressman}: {e}")

    # Sort trades by reported date (if available)
    all_trades.sort(key=lambda x: x.get("ReportDate", ""), reverse=True)

    return render_template('recent_trades.html', trades=all_trades, username=username)





@app.route('/interactive_query', methods=['GET', 'POST'])
def interactive_query():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Get user inputs
        ticker = request.form.get('ticker', '').strip()
        representative = request.form.get('representative', '').strip()
        representative = representative.replace(" ", "+")
        
        # Perform the API request
        transaction_service = transactionClass()
        transaction_service.conn.request(
            "GET",
            f"/beta/bulk/congresstrading?page=10&page_size=10&representative={representative}&ticker={ticker}",
            headers=transaction_service.headers
        )
        res = transaction_service.conn.getresponse()
        data = res.read().decode("utf-8")  # Decode response to string
        
        return render_template(
            'interactive_query.html',
            ticker=ticker,
            representative=representative,
            data=json.loads(data)  # Parse the JSON response
        )
    
    # Render the page for GET requests
    return render_template('interactive_query.html', data=None)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

