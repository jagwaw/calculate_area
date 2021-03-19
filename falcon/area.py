import os
import falcon
import math
import json

from pprint import pprint, pformat
import logging


logging.basicConfig(level=logging.INFO, format='%(message)s')

class ComputeArea(object):

    def convert_to_centimeters(self,area,area_measurement):
        converted_area=""
        if area_measurement == "meters":  
            converted_area=area*100

        elif area_measurement == "inches":
            converted_area=area*2.54

        elif area_measurement == "centimeters":
            converted_area=area

        return round(converted_area,2)

    def convert_to_inches(self,area,area_measurement):
        converted_area=""
        if area_measurement == "centimeters":
            converted_area=area/2.54
        elif area_measurement == "meters":

            converted_area=area*39.37
        elif area_measurement == "inches":
            converted_area=area

        return round(converted_area,2)

    def convert_to_meters(self,area,area_measurement):
        converted_area=""
        if area_measurement == "centimeters":
            converted_area=area/100

        elif area_measurement == "inches":
            converted_area=area*0.0254

        elif area_measurement == "meters":
            converted_area=area

        return round(converted_area,2)


    def compute_circle_area(self,data):
        radius=round(float(data["radius"]),2) 
        area=math.pi* radius * radius
        area=round(area,2) 
        converted_area=""
        if data["output_measurement"] == "centimeters":
            converted_area = self.convert_to_centimeters(area,data["radius_measurement"])
        elif data["output_measurement"] == "inches":
            converted_area = self.convert_to_inches(area,data["radius_measurement"])
        elif data["output_measurement"] == "meters":
            converted_area = self.convert_to_meters(area,data["radius_measurement"])

        return converted_area

    def compute_triangle_area(self,data):
        base=round(float(data["base"]),2)
        height=round(float(data["height"]),2)
 

        if data["output_measurement"] == "centimeters":
            converted_base=self.convert_to_centimeters(base,data["base_measurement"])
            converted_height=self.convert_to_centimeters(height,data["height_measurement"])

        elif data["output_measurement"] == "inches":
            converted_base=self.convert_to_inches(base,data["base_measurement"])
            converted_height=self.convert_to_inches(height,data["height_measurement"])

        elif data["output_measurement"] == "meters":
            converted_base=self.convert_to_meters(base,data["base_measurement"])
            converted_height=self.convert_to_meters(height,data["height_measurement"])
        
        area=round(0.5*converted_base*converted_height,2)

        return area

    def compute_square_area(self,data):
        side=round(float(data["side"]),2) 
        area=side*side
        
        if data["output_measurement"] == "centimeters":
            converted_area = self.convert_to_centimeters(area,data["side_measurement"])
        elif data["output_measurement"] == "inches":
            converted_area = self.convert_to_inches(area,data["side_measurement"])
        elif data["output_measurement"] == "meters":
            converted_area = self.convert_to_meters(area,data["side_measurement"])

        return converted_area

    def compute_rectangle_area(self,data): 
        length=round(float(data["length"]),2)
        width=round(float(data["width"]),2)

        if data["output_measurement"] == "centimeters":
            converted_length=self.convert_to_centimeters(length,data["length_measurement"])
            converted_width=self.convert_to_centimeters(width,data["width_measurement"])

        elif data["output_measurement"] == "inches":
            converted_length=self.convert_to_inches(length,data["length_measurement"])
            converted_width=self.convert_to_inches(width,data["width_measurement"])

        elif data["output_measurement"] == "meters":
            converted_length=self.convert_to_meters(length,data["length_measurement"])
            converted_width=self.convert_to_meters(width,data["width_measurement"])


        area=converted_length*converted_width
        area=round(area,2)

        return area

    def on_post(self, req, resp):
        data=req.media
        area_dict=dict()
        area_dict["message"]=False
        area_dict["measurement"]=""

        if data["shape"] == "Circle":
            area=self.compute_circle_area(data)

        elif data["shape"] == "Triangle":
            area=self.compute_triangle_area(data)
        elif data["shape"] == "Square":
            area=self.compute_square_area(data)
        elif data["shape"] == "Rectangle":
            area=self.compute_rectangle_area(data)

        if area:
            area_dict["message"]=True
            area_dict["area"]=area
            if data["output_measurement"] == "inches":
                area_dict["measurement"]="in"
            elif data["output_measurement"] == "centimeters":
                area_dict["measurement"]="cm"
            elif data["output_measurement"] == "meters":
                area_dict["measurement"]="m"

        resp.body   = json.dumps(area_dict, ensure_ascii=False)
        resp.status = falcon.HTTP_200
        
app = application = falcon.API()
app.add_route('/falcon/area/compute', ComputeArea())
