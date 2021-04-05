from flask import Flask, url_for
from flask import render_template
from flask import request, jsonify

app = Flask(__name__)

# Data
current_id = 11
bands = [
    "The Beatles",
    "The Rolling Stones",
    "Pink Floyd",
    "Grateful Dead",
    "Led Zeppelin",
    "Fleetwood Mac",
    "Queen",
    "AC/DC",
    "Guns N' Roses",
    "Nirvana"
]
info = [
    {
        "id": 1, 
        "band": "The Beatles",
        "image": "https://cdn.britannica.com/18/136518-050-CD0E49C6/The-Beatles-Ringo-Starr-Paul-McCartney-George.jpg",
        "description": "The Beatles is considered one of the greatest music groups of all time. Members included John Lennon, Paul McCartney, George Harrison, and Ringo Starr.",
        "yearFormed": 1960,
        "albums": [
            {
                "name": "Rubber Soul (1965)",
                "deleted": False,
            },
            {
                "name": "Revolver (1966)",
                "deleted": False,
            },
            {
                "name": "Sgt. Pepper's Lonely Hearts Club Band (1967)",
                "deleted": False,
            }
        ]
    },
    {
        "id": 2, 
        "band": "The Rolling Stones",
        "image": "https://www.rollingstone.com/wp-content/uploads/2019/04/rolling-stones-honk-review.jpg?resize=1800,1200&w=1200",
        "description": "The Rolling Stones were one of the biggest bands in the 60s and pioneered a hard rock sound. Members included Mick Jagger, Keith Richards, Ronnie Woods, and Charlie Watts.",
        "yearFormed": 1962,
        "albums": [
            {
                "name": "Let It Bleed (1969)",
                "deleted": False,
            },
            {
                "name": "Sticky Fingers (1971)",
                "deleted": False,
            },
            {
                "name": "Exile on Main St. (1972)",
                "deleted": False,
            }
        ]
    },
    {
        "id": 3, 
        "band": "Pink Floyd",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/d6/Pink_Floyd_-_all_members.jpg",
        "description": "Pink Floyd pioneered psychedellic rock in the 70s. Members included Syd Barrett, Roger Waters, David Gilmour, Richard Wright, and Nick Mason.",
        "yearFormed": 1965,
        "albums": [
            {
                "name": "The Dark Side of the Moon (1973)",
                "deleted": False,
            },
            {
                "name": "Wish You Were Here (1975)",
                "deleted": False,
            },
            {
                "name": "The Wall (1979)",
                "deleted": False,
            }
        ]
    },
    {
        "id": 4, 
        "band": "Grateful Dead",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6b/Grateful_Dead_%281970%29.png",
        "description": "Grateful Dead was a powerful voice for the phsychedelic revolution in the later 60s and throughout the 70s. Members included Jerry Garcia, Bob Weir, Ron McKernan, Phil Lesh, and Bill Kreutzmann.",
        "yearFormed": 1965,
        "albums": [
            {
                "name": "Workingman's Dead (1970)",
                "deleted": False,
            },
            {
                "name": "American Beauty (1970)",
                "deleted": False,
            },
            {
                "name": "Shakedown Street (1978)",
                "deleted": False,
            }
        ]
    },
    {
        "id": 5, 
        "band": "Led Zeppelin",
        "image": "https://cdn.cnn.com/cnn/interactive/2018/10/entertainment/led-zeppelin-cnnphotos/media/01.jpg",
        "description": "Led Zeppelin is considered \"the biggest band of the Seventies\" by Rolling Stone magazine. Members included Robert Plant, Jimmy Page, John Paul Jones, and John Bonham.",
        "yearFormed": 1968,
        "albums": [
            {
                "name": "Led Zeppelin (1969)",
                "deleted": False,
            },
            {
                "name": "Led Zeppelin III (1970)",
                "deleted": False,
            },
            {
                "name": "Led Zeppelin IV (1971)",
                "deleted": False,
            }
        ]
    },
    {
        "id": 6, 
        "band": "Fleetwood Mac",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/fe/Fleetwood_Mac_Billboard_1977.jpg",
        "description": "Fleetwood Mac was an influential band in the 70s. Members included Stevie Nicks, Mick Fleetwood, John McVie, and Christine McVie.",
        "yearFormed": 1967,
        "albums": [
            {
                "name": "Fleetwood Mac (1975)",
                "deleted": False,
            },
            {
                "name": "Rumours (1977)",
                "deleted": False,
            },
            {
                "name": "Tusk (1979)",
                "deleted": False,
            }
        ]
    },
    {
        "id": 7, 
        "band": "Queen",
        "image": "https://www.biography.com/.image/t_share/MTY2MTk2NTQ5MzY4NDg5OTMx/queen-london-1973-left-to-right-drummer-roger-taylor-singer-freddie-mercury-1946---1991-guitarist-brian-may-and-bassist-john-deacon-photo-by-michael-putlandgetty-images.jpg",
        "description": "Queen is one of the world's best-selling bands. Members included Freddie Mercury, Brian May, John Deacon, and Roger Taylor.",
        "yearFormed": 1970,
        "albums": [
            {
                "name": "Queen (1973)",
                "deleted": False,
            },
            {
                "name": "Queen II (1974)",
                "deleted": False,
            },
            {
                "name": "A Night at the Opera (1975)",
                "deleted": False,
            }
        ]
    },
    {
        "id": 8,
        "band": "AC/DC",
        "image": "https://static.billboard.com/files/2020/10/acdc-2020-press-josh-cheuse-01-1548-1602694716-1024x677.jpg",
        "description": "AC/DC is one of the greatest rock and roll bands to ever exist. Members included Angus Young, Malcolm Young, Bon Scott, and Brian Johnson.",
        "yearFormed": 1973,
        "albums": [
            {
                "name": "Highway to Hell (1979)",
                "deleted": False,
            },
            {
                "name": "Back in Black (1980)",
                "deleted": False,
            },
            {
                "name": "The Razors Edge (1990)",
                "deleted": False,
            }
        ]
    },
    {
        "id": 9, 
        "band": "Guns N' Roses",
        "image": "https://m.wsj.net/video/20160324/032416lunchgunsroses/032416lunchgunsroses_960x540.jpg",
        "description": "Guns N' Roses dominated rock in the late 80s and early 90s. Members included Axl Rose, Slash, Duff McKagan, and Steven Adler.",
        "yearFormed": 1985,
        "albums": [
            {
                "name": "Appetite for Destruction (1987)",
                "deleted": False,
            },
            {
                "name": "Use Your Illusion I (1991)",
                "deleted": False,
            },
            {
                "name": "Use Your Illusion II (1991)",
                "deleted": False,
            }
        ]
    },
    {
        "id": 10, 
        "band": "Nirvana",
        "image": "https://dazedimg-dazedgroup.netdna-ssl.com/1500/azure/dazed-prod/1220/9/1229141.jpg",
        "description": "Nirvana was a powerful voice for Generation X. Members included Kurt Cobain, Krist Novoselic, and Dave Grohl.",
        "yearFormed": 1987,
        "albums": [
            {
                "name": "Bleach (1989)",
                "deleted": False,
            },
            {
                "name": "Nevermind (1991)",
                "deleted": False,
            },
            {
                "name": "In Utero (1993)",
                "deleted": False,
            }
        ]
    }
]

# Routes
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/", methods=["POST"])
def getData():
    return { "bands": bands, "info": info }

@app.route("/view/<id>", methods=["GET"])
def view(id):
    global info

    obj = None
    for i in info:
        if i["id"] == int(id):
            obj = i

    return render_template("view.html", id=obj["id"], band=obj["band"], description=obj["description"], image=obj["image"], yearFormed=obj["yearFormed"], albums=obj["albums"])

@app.route("/create", methods=["GET"])
def create():
    return render_template("create.html")

@app.route("/search", methods=["GET"])
def searchPage():
    return render_template("search.html")

@app.route("/search", methods=["POST"])
def search():
    global bands, info

    req = request.get_json()
    print(req)

    query = req["query"]

    list = []
    for b in bands:
        if b.lower().find(query.lower()) > -1:
            entry = {}
            entry["band"] = b
            for i in info:
                if i["band"] == b:
                    entry["id"] = i["id"]
                    entry["image"] = i["image"]
            list.append(entry)

    return { "bands": list }

@app.route("/create/submit", methods=["POST"])
def submit():
    global current_id, bands, info

    req = request.get_json()
    print(req)

    band = req["band"]
    description = req["description"]
    image = req["image"]
    yearFormed = req["yearFormed"]
    albums = req["albums"]

    bands.append(band)

    new_info = {
        "id": current_id,
        "band": band,
        "description": description,
        "image": image,
        "yearFormed": yearFormed,
        "albums": [
            {
                "name": albums[0],
                "deleted": False
            },
            {
                "name": albums[1],
                "deleted": False
            },
            {
                "name": albums[2],
                "deleted": False
            }
        ]
    }

    info.append(new_info)

    current_id += 1

    return { "bands": bands, "info": info, "new": new_info }

@app.route("/update", methods=["POST"])
def update():
    global info

    req = request.get_json()
    print(req)

    bid = req["bid"]
    description = req["update"]

    for i in info:
        if i["id"] == int(bid):
            i["description"] = description

    return { "info": info }

@app.route("/delete", methods=["POST"])
def delete():
    global info

    req = request.get_json()
    print(req)

    bid = req["bid"]
    index = int(req["index"])

    for i in info:
        if i["id"] == int(bid):
            i["albums"][index]["deleted"] = True

    return { "info": info }

@app.route("/undo", methods=["POST"])
def undo():
    global info

    req = request.get_json()
    print(req)

    bid = req["bid"]
    index = int(req["index"])

    for i in info:
        if i["id"] == int(bid):
            i["albums"][index]["deleted"] = False

    return { "info": info }