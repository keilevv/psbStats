from tools import psb_list, avg_dist, density, nei_psb
import requests as r
from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/psb/statistics")
def genStats():
    response = r.get("http://localhost/api/psb/statistics")
    PSB = response.json() 
    array = psb_list(PSB)

    stats = [
        {
        "avg_dist": avg_dist(array[0]),
        "nei_psb": nei_psb(PSB, array[4]),
        "density": density(array[0], array[1], array[2])
        }
    ]
    return(jsonify(stats))

@app.route("/psb/statistics/<latitude>/<longitude>")
def stats(latitude, longitude):
    response = r.get("http://localhost/api/psb/statistics")
    PSB = response.json()
    array = psb_list(PSB)   
    
    aux = density(array[0], array[1], array[2])
    for i in range(len(aux)):
        if(aux[i]["latitude"] == latitude, aux[1]["longitude"] == longitude):
            lat = aux[i]["latitude"]
            lon = aux[i]["longitude"]
            den = aux[i]["density"]
            dist = array[0][i]
    psb_stats = [
        {
        "longitude":lon,
        "latitude": lat,
        "density": den,
        "distance":dist
        }
    ]

    return(jsonify(psb_stats))


