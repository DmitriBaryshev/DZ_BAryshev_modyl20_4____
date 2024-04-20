from flask import Flask, render_template
import datetime

app = Flask(__name__)


# Задание 1: Отображение строки из любимой песни
@app.route('/')
def favorite_song():
    song = "We are the champions, my friends"
    artist = "Queen"
    return render_template('favorite_song.html', song=song, artist=artist)


# Задание 2: Перевод строки песни на разные языки
@app.route('/<lang_code>')
def translated_song(lang_code):
    songs = {
        'en': {"song": "We are the champions, my friends", "artist": "Queen"},
        'fr': {"song": "Nous sommes les champions, mes amis", "artist": "Queen"},
        'de': {"song": "Wir sind die Champions, meine Freunde", "artist": "Queen"},
        'es': {"song": "Somos los campeones, mis amigos", "artist": "Queen"}
    }
    if lang_code in songs:
        return render_template('translated_song.html', song=songs[lang_code]['song'], artist=songs[lang_code]['artist'])
    else:
        return "Translation not available for this language"


# Задание 3: Веб-приложение об автомобилях
@app.route('/cars')
def cars():
    car_brands = ['Toyota', 'Ford', 'Chevrolet', 'Honda']
    car_types = ['Sedan', 'SUV', 'Truck', 'Hatchback']
    return render_template('cars.html', car_brands=car_brands, car_types=car_types)


# Задание 4: Отображение текущего дня недели
@app.route('/day_of_week')
def day_of_week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_index = datetime.datetime.today().weekday()
    return render_template('day_of_week.html', day=days[day_index])


# Задание 5: Отображение информации о модели наушников
@app.route('/headphones')
def headphones():
    model = request.args.get('model')
    if model == 'budslive':
        headphone_info = "Samsung Galaxy Buds Live"
    elif model == 'airpods':
        headphone_info = "Apple AirPods"
    else:
        headphone_info = "Model not found"
    return render_template('headphones.html', model=headphone_info)


# Дополнительное задание: Обработка запросов о писателях и годах
@app.route('/writers')
def writers():
    writer = request.args.get('writers')
    year = request.args.get('year')
    if writer == 'Hemingway' and year == '1926':
        return "Books written by Hemingway in 1926"
    elif writer == 'Hemingway' and year == '1940':
        return "Books written by Hemingway in 1940"
    else:
        return redirect(url_for('hemingway'))


@app.route('/cities')
def cities():
    writer = request.args.get('writers')
    year = request.args.get('year')
    if writer == 'Hemingway' and year == '1940':
        return "Books written by Hemingway in 1940"
    else:
        return redirect(url_for('hemingway'))


@app.route('/hemingway')
def hemingway():
    return "Information about Hemingway"


if __name__ == '__main__':
    app.run(debug=True)
