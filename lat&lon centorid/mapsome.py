#!/usr/bin/python
import sys
import json

# mapper to calcuate centroid and proportion of location
for line in sys.stdin:
  jOne = json.loads(line.strip())
  # initializing the dictionary to latitude, longitudea and is location present values
  coord_dict = {'lat':0,'long':0,'yes':0}
  # check for "geo" key in the root-level
  if "geo" in jOne.keys() and jOne["geo"] != None:
  	geoJOne = jOne["geo"]
  	coord_dict['lat'] = geoJOne["coordinates"][0]
  	coord_dict['long'] = geoJOne["coordinates"][1]
  	coord_dict['yes'] = 1
  # check for "place" key in the root-level; Calculating centroid of the place (a polygon with array of longitude, latitude information)
  elif "place" in jOne.keys() and jOne["place"] != None and "bounding_box" in jOne["place"].keys() and jOne["place"]["bounding_box"] != None:
    placeJOne = jOne["place"]
    boundingPlaceJOne = placeJOne['bounding_box']
    if "coordinates" in boundingPlaceJOne:
      coordsBPJOne = boundingPlaceJOne['coordinates']
    else:
      coordsBPJOne = [[[0.0, 0.0]]]
    centerBPJOne = [0.0,0.0]
    coordsLen = len(coordsBPJOne)
    for coord in coordsBPJOne[0]:
      centerBPJOne[0] += coord[0]
      centerBPJOne[1] += coord[1]
    coord[0] /= coordsLen
    coord[1] /= coordsLen
    # assigning centroid to dictionary
    coord_dict['lat'] = coord[1]
    coord_dict['long'] = coord[0]
    coord_dict['yes'] = 1
  print "coords\t%s" % ('{"lat": %s, "long": %s, "yes": %s}' %(coord_dict['lat'], coord_dict['long'], coord_dict['yes']))
