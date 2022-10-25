from app import app

@app.route('/', methods=['GET'])
def home():
    app.logger.info('home')
    return {"status":"Welcome to Sushi API"}

@app.route('/ping', methods=['GET'])
def ping():
    app.logger.info('ping')
    return {"status":"good"}