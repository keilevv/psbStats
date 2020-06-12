
import numpy as np
import requests as r
import mpu

def psb_list(PSB):

    lat_list = []
    lon_list = []
    add_list = [] 
    nei_list = []

    for i in range(len(PSB)):
        lat_list.append(float(PSB[i]["latitude"]))
        lon_list.append(float(PSB[i]["longitude"]))
        add_list.append(PSB[i]["address"])
        nei_list.append(PSB[i]["neighborhood"])

    dist = []  ## Distance Maxtrix between PSB's
    ## mpu.haversine_distance((lat_list[0], lon_list[0]), (lat_list[3], lon_list[3]))

    for i in range(len(PSB)):
        dist.append([]) 
        for j in range(len(PSB)):
            dist[i].append(mpu.haversine_distance((lat_list[i], lon_list[i]), (lat_list[j], lon_list[j])))

    return(dist, lat_list, lon_list, add_list, nei_list)

def avg_dist(dist): ## Average Distance between PSB

    for i in range(len(dist)):
        avg = np.mean(dist)
    
    return avg

def density(dist, lat_list, lon_list): # number of PSB in a 1km circle from current PSB.
    n = []
    for i in range(len(dist)):
        cant = 0
        for j in range(len(dist[i])):
            if( dist[i][j] < 1):
                cant += 1
        n.append(cant)
    
    result = []
    for i in range(len(dist)):
        den  = {
            "latitude": lat_list[i],
            "longitude": lon_list[i],
            "density": n[i]
        }

        result.append(den)
    return result


def nei_psb(PSB, nei_list): # number of PSB per neighborhood 
    aux = []
    nei = []
    
    for i in range(len(PSB)):
        if(PSB[i]["neighborhood"] not in nei):
            nei.append(PSB[i]["neighborhood"])
    
    for i in range(len(nei)):   
        aux.append(nei_list.count(nei[i]))

    result = dict(zip(nei,aux))
    return (result)


"""  PSB = response.json()
    array = psb_list(PSB)

    for i in range(len(PSB)):"""
