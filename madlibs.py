# from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."


# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet', methods=["POST"])
def greet_person():
    player = request.form.get("person")
    return render_template("compliment.html", person=player)

@app.route('/game')
def show_game_form():
    game = request.args.get("playgame")
    if game == "yes":
        return render_template('game.html')
    else:
        return render_template('goodbye.html')

@app.route('/madlib')
def show_madlib():
    color = request.args.get("color")
    noun = request.args.get("noun")
    name = request.args.get("person")
    adjective = request.args.get("adjective")
    return render_template('madlib.html',
                           color=color,
                           noun=noun,
                           name=name,
                           adjective=adjective)

    # AWESOMENESS = [
    #     'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    #     'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    # compliment = choice(AWESOMENESS)

# return render_template("compliment.html", person=player)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
