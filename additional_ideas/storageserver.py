import pickle
import os

# os.system("clear")


def storageserver():
    jokes = [{
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "id": "XiqYaw7YS7mIbDL6JG5Raw",
        "url": "",
        "value": "A cobra once bit Chuck Norris. After five days of excruciating pain, the cobra died"
    }, {
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "id": "bXavkEi8RmWFka1WGJAAZg",
        "url": "",
        "value": "a blind man once walked in to Chuck Norris chuck said do you know who i am im Chuck Norris. the mere mention of his name cured his blindness but sadly the first last and only thing he saw was a deadly round house kick to the face"
    }, {
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "id": "JgSv8y_9So6DMQK2uAKbaA",
        "url": "",
        "value": "You know why Chuck Norris-movies suck? Because the movies are nervous about Chuck Norris in 'em."
    }, {
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "id": "k7B66hllT7Oee_hkuQF-Fg",
        "url": "",
        "value": "Chuck Norris wears a full samurai suit as pajamas."
    }, {
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "id": "PK0iYvrnRNWXBKCop8ILmg",
        "url": "",
        "value": "If it looks like a duck, walks like a duck and even quacks like a duck but Chuck Norris says it's a rare red-breasted sapsucker in heat... It's a rare red-breasted sapsucker and be thankful Chuck let you agree with him."
    }, {
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "id": "ropmm-mhrtotnxq95rsdrg",
        "url": "",
        "value": "On the set of Walker Texas Ranger Chuck Norris brought a dying lamb back to life by nuzzling it with his beard. As the onlookers gathered, the lamb sprang to life. Chuck Norris then roundhouse kicked it, killing it instantly. This was just to prove that the good Chuck givet"
    }]

    pickle.dump(jokes, open("jokes.dat", "wb"))
    jokes = pickle.load(open("jokes.dat", "rb"))

    # print(jokes[1]['value'])
storageserver()
