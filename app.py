from flask import Flask, render_template, request, redirect
import datetime
import json
from datetime import datetime
import random


app = Flask(__name__)


@app.route('/1/<position_book>/<user>/1')
def get_index(position_book, user):
    with open('my_db.json', 'r', encoding='utf-8') as read_book:
        read_book = json.load(read_book)
        print("Position_book: ", position_book, "User: ", user)
        print(read_book[1])
        print("pass")
        position_book = int(position_book)
        status = read_book[1][position_book]["status"]
        print(status)
        if read_book[1][position_book]["status"] == "True":
            # user = int(user)
            # read_book[1][position_book]["count_now"] -= 1
            # read_book[2][user]["id_book"].append(read_book[1][position_book]["id_book"])
            # read_book[2][user]["id_user"].extend(read_book[2][user]["id_user"])
            #
            # time = datetime.now().strftime('%d.%m.%y')
            # read_book[2][user]["time_on"].append(time)
            read_book[1][position_book]["status"] = "False"

            with open('my_db.json', 'w', encoding='utf-8') as Achange_book:
                Achange_book.write(json.dumps(read_book))
                return render_template("index.html")

        else:
            read_book[1][position_book]["status"] = "True"
            with open('my_db.json', 'w', encoding='utf-8') as change_book:
                change_book.write(json.dumps(read_book))
                return render_template("putsucces.html")

    # return render_template("index.html")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id




def deg_book():
    with open('my_db.json', 'r', encoding='utf-8') as read_book:
        read_book = json.load(read_book)
        user = int(user)
        read_book[1][position_book]["count_now"] -= 1
        read_book[2][user]["id_book"].append(read_book[1][position_book]["id_book"])
        read_book[2][user]["id_user"].extend(read_book[2][user]["id_user"])



@app.route('/action', methods=['POST'])
def get_success():

    #     with open('my_db.json', 'r', encoding='utf-8') as read_book:
    #         read_book = json.load(read_book)
    #
    #         mail = request.form['mail']
    #         user = random.randint(1, 2)
    #
    #         read_book[0][user]["knigaVzial"].extend(mail)
    #
    #         time = datetime.now().strftime('%d.%m.%y')
    #         read_book[2][user]["time_on"].append(time)
    #         # read_book[1][position_book]["count_now"] -= 1
    #     return render_template("getsuccess.html")
    return render_template("getsuccess.html")


@app.route("/")
def get_library():
    return render_template("library.html")

@app.route("/org")
def get_org():
    return render_template("org.html")

@app.route("/putsucces")
def get_putsucces():
    return render_template("putsucces.html")


if __name__ == "__main__":
    app.run(debug=True, port=777)