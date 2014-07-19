from flask import Flask, jsonify, request

app = Flask(__name__)

skilled_workers = [
    {
        'id': 1,
        'name': u'Shahrukh Khan',
        'category': u'Plumber',
        'price': 100,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },
    {
        'id': 2,
        'name': u'Salman Khan',
        'category': u'Plumber',
        'price': 150,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },
    {
        'id': 3,
        'name': u'Amir Khan',
        'category': u'Plumber',
        'price': 50,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },
    {
        'id': 4,
        'name': u'Sohail Khan',
        'category': u'Plumber',
        'price': 170,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },
    {
        'id': 5,
        'name': u'Arbaaz Khan',
        'category': u'Plumber',
        'price': 30,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },
    {
        'id': 6,
        'name': u'Fardeen Khan',
        'category': u'Electrician',
        'price': 100,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },
    {
        'id': 7,
        'name': u'Chunky Pandey',
        'category': u'Electrician',
        'price': 120,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },
    {
        'id': 8,
        'name': u'Shakti Kapoor',
        'category': u'Electrician',
        'price': 50,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },
    {
        'id': 9,
        'name': u'Gulshan Grover',
        'category': u'Electrician',
        'price': 180,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },
    {
        'id': 10,
        'name': u'Hritik Roshan',
        'category': u'Electrician',
        'price': 200,
        'rating': 0,
        'reviews': 0,
        'phone': 9999888822,
    },

]


@app.route('/fetch/worker', methods=['GET'])
def get_workers():
    category = request.args.get('category')
    filtered_list = []
    for item in skilled_workers:
        if item['category'] == category:
            filtered_list.append(item)

    return jsonify({'workers': filtered_list})

if __name__ == '__main__':
    app.run(debug = True)