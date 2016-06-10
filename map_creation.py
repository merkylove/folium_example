# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import folium
import pandas as pd
import os


LISBON_COORDS = (38.736946, -9.142685)

def create_popup(name, description, path_to_image, link):
	return u'''<!DOCTYPE html>
    	<html>
    	<body style="width:100%;height:90%;">
    	<h2>{}</h2>
    	<a href='{}' target='_blank'>
    	<img src="{}" style="width:100%;height:228px;">
    	</a>
    	<p>{}</p>
    	</body>
    	</html>'''.format(name, link, path_to_image, description)

def add_markers(m, markers_info_df):
    for index, marker in markers_info_df.iterrows():
        popup = create_popup(marker.placename, marker.description, os.path.join('img', marker.image), marker.link)
        m.simple_marker(location=[marker.lat, marker.lon], popup=popup)
    return m

def make_map(infile, outfile):
	df = pd.DataFrame.from_csv(infile, index_col=None, encoding='utf-8')
	lisbon_map = folium.Map(location=LISBON_COORDS, zoom_start=13)
	lisbon_map = add_markers(lisbon_map, df)
	lisbon_map.create_map(outfile)
	return lisbon_map


if __name__ == '__main__':
	make_map('lisbon.csv', 'index.html')
