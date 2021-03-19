import unittest
import area


class TestArea(unittest.TestCase):

	def test_compute_circle_area(self):
		compute=area.ComputeArea()
		# inch to cm
		result_1 =compute.compute_circle_area({'radius': '10', 'radius_measurement': 'inches', 'output_measurement': 'centimeters', 'shape': 'Circle'})
		self.assertEqual(result_1,797.97)
		# cm to meter
		result_2 =compute.compute_circle_area({'radius': '10', 'radius_measurement': 'centimeters', 'output_measurement': 'meters', 'shape': 'Circle'})
		self.assertEqual(result_2,3.14)
		#meter to inch
		result_3 =compute.compute_circle_area({'radius': '10', 'radius_measurement': 'meters', 'output_measurement': 'inches', 'shape': 'Circle'})
		self.assertEqual(result_3,12368.48)		 
		#cm to inch
		result_4 =compute.compute_circle_area({'radius': '10', 'radius_measurement': 'centimeters', 'output_measurement': 'inches', 'shape': 'Circle'})
		self.assertEqual(result_4,123.69)
		#meter to cm 
		result_5 =compute.compute_circle_area({'radius': '10', 'radius_measurement': 'meters', 'output_measurement': 'centimeters', 'shape': 'Circle'})
		self.assertEqual(result_5,31416)	
 		#inch to meter
		result_6 =compute.compute_circle_area({'radius': '10', 'radius_measurement': 'inches', 'output_measurement': 'meters', 'shape': 'Circle'})
		self.assertEqual(result_6,7.98)	 	

	def test_compute_square_area(self):
		compute=area.ComputeArea()
		# inch to cm
		result_1 =compute.compute_square_area({'side': '6', 'side_measurement': 'inches', 'output_measurement': 'centimeters', 'shape': 'Square'})
		self.assertEqual(result_1,91.44)
		# cm to meter
		result_2 =compute.compute_square_area({'side': '9', 'side_measurement': 'centimeters', 'output_measurement': 'meters', 'shape': 'Square'})
		self.assertEqual(result_2,0.81)
		#meter to inch
		result_3 =compute.compute_square_area({'side': '12', 'side_measurement': 'meters', 'output_measurement': 'inches', 'shape': 'Square'})
		self.assertEqual(result_3,5669.28)		 
		#cm to inch
		result_4 =compute.compute_square_area({'side': '30', 'side_measurement': 'centimeters', 'output_measurement': 'inches', 'shape': 'Square'})
		self.assertEqual(result_4,354.33)
		#meter to cm 
		result_5 =compute.compute_square_area({'side': '5', 'side_measurement': 'meters', 'output_measurement': 'centimeters', 'shape': 'Square'})
		self.assertEqual(result_5,2500)	
 		#inch to meter
		result_6 =compute.compute_square_area({'side': '4', 'side_measurement': 'inches', 'output_measurement': 'meters', 'shape': 'Square'})
		self.assertEqual(result_6,0.41)	 	

	def test_compute_triangle_area(self):
		compute=area.ComputeArea()
		# inch and cm to meter
		result_1 =compute.compute_triangle_area({'base': '10', 'base_measurement': 'inches', 'height': '50', 'height_measurement': 'centimeters','output_measurement': 'meters', 'shape': 'Triangle'})
		self.assertEqual(result_1,0.06)
		# inch and meter to cm
		result_2 =compute.compute_triangle_area({'base': '12', 'base_measurement': 'inches', 'height': '3', 'height_measurement': 'meters','output_measurement': 'centimeters', 'shape': 'Triangle'})
		self.assertEqual(result_2,4572)
		#cm and meter to inch
		result_3 =compute.compute_triangle_area({'base': '4', 'base_measurement': 'centimeters', 'height': '9', 'height_measurement': 'meters','output_measurement': 'inches', 'shape': 'Triangle'})
		self.assertEqual(result_3,278.15)	
		#meter 
		result_4 =compute.compute_triangle_area({'base': '2', 'base_measurement': 'meters', 'height': '13', 'height_measurement': 'meters','output_measurement': 'meters', 'shape': 'Triangle'})
		self.assertEqual(result_4,13)
		#cm 
		result_5 =compute.compute_triangle_area({'base': '3', 'base_measurement': 'centimeters', 'height': '15', 'height_measurement': 'centimeters','output_measurement': 'centimeters', 'shape': 'Triangle'})
		self.assertEqual(result_5,22.5)	
 		#inch
		result_6 =compute.compute_triangle_area({'base': '9', 'base_measurement': 'inches', 'height': '16', 'height_measurement': 'inches','output_measurement': 'inches', 'shape': 'Triangle'})
		self.assertEqual(result_6,72)	 	
 		# inch and cm to inch
		result_7 =compute.compute_triangle_area({'base': '20', 'base_measurement': 'inches', 'height': '21', 'height_measurement': 'centimeters','output_measurement': 'inches', 'shape': 'Triangle'})
		self.assertEqual(result_7,82.70)	 
 		#inch and meter to inch
		result_8 =compute.compute_triangle_area({'base': '30', 'base_measurement': 'inches', 'height': '10', 'height_measurement': 'meters','output_measurement': 'inches', 'shape': 'Triangle'})
		self.assertEqual(result_8,5905.5)	 	
 		#cm and inch to cm
		result_9 =compute.compute_triangle_area({'base': '11', 'base_measurement': 'centimeters', 'height': '15', 'height_measurement': 'inches','output_measurement': 'centimeters', 'shape': 'Triangle'})
		self.assertEqual(result_9,209.55)	 
 		#cm and meter to cm
		result_10 =compute.compute_triangle_area({'base': '16', 'base_measurement': 'centimeters', 'height': '9', 'height_measurement': 'meters','output_measurement': 'centimeters', 'shape': 'Triangle'})
		self.assertEqual(result_10,7200)
 		#meter and cm to meter
		result_11 =compute.compute_triangle_area({'base': '8', 'base_measurement': 'meters', 'height': '30', 'height_measurement': 'centimeters','output_measurement': 'meters', 'shape': 'Triangle'})
		self.assertEqual(result_11,1.2)
 		#meter and inch to meter
		result_12 =compute.compute_triangle_area({'base': '9', 'base_measurement': 'meters', 'height': '10', 'height_measurement': 'inches','output_measurement': 'meters', 'shape': 'Triangle'})
		self.assertEqual(result_12,1.12)	 	

	def test_compute_rectangle_area(self):
		compute=area.ComputeArea()
		# inch and cm to meter
		result_1 =compute.compute_rectangle_area({'length': '15', 'length_measurement': 'inches', 'width': '50', 'width_measurement': 'centimeters','output_measurement': 'meters', 'shape': 'Rectangle'})
		self.assertEqual(result_1,0.19)
		# inch and meter to cm
		result_2 =compute.compute_rectangle_area({'length': '10', 'length_measurement': 'inches', 'width': '30', 'width_measurement': 'meters','output_measurement': 'centimeters', 'shape': 'Rectangle'})
		self.assertEqual(result_2,76200)
		#cm and meter to inch
		result_3 =compute.compute_rectangle_area({'length': '60', 'length_measurement': 'centimeters', 'width': '30', 'width_measurement': 'meters','output_measurement': 'inches', 'shape': 'Rectangle'})
		self.assertEqual(result_3,27897.58)	
		#meter 
		result_4 =compute.compute_rectangle_area({'length': '25', 'length_measurement': 'meters', 'width': '25', 'width_measurement': 'meters','output_measurement': 'meters', 'shape': 'Rectangle'})
		self.assertEqual(result_4,625)
		#cm 
		result_5 =compute.compute_rectangle_area({'length': '100', 'length_measurement': 'centimeters', 'width': '100', 'width_measurement': 'centimeters','output_measurement': 'centimeters', 'shape': 'Rectangle'})
		self.assertEqual(result_5,10000)	
 		#inch
		result_6 =compute.compute_rectangle_area({'length': '10', 'length_measurement': 'inches', 'width': '15', 'width_measurement': 'inches','output_measurement': 'inches', 'shape': 'Rectangle'})
		self.assertEqual(result_6,150)	 	
 		# inch and cm to inch
		result_7 =compute.compute_rectangle_area({'length': '30', 'length_measurement': 'inches', 'width': '70', 'width_measurement': 'centimeters','output_measurement': 'inches', 'shape': 'Rectangle'})
		self.assertEqual(result_7,826.8)	 
 		#inch and meter to inch
		result_8 =compute.compute_rectangle_area({'length': '40', 'length_measurement': 'inches', 'width': '20', 'width_measurement': 'meters','output_measurement': 'inches', 'shape': 'Rectangle'})
		self.assertEqual(result_8,31496)	 	
 		#cm and inch to cm
		result_9 =compute.compute_rectangle_area({'length': '60', 'length_measurement': 'centimeters', 'width': '90', 'width_measurement': 'inches','output_measurement': 'centimeters', 'shape': 'Rectangle'})
		self.assertEqual(result_9,13716)	 
 		#cm and meter to cm
		result_10 =compute.compute_rectangle_area({'length': '100', 'length_measurement': 'centimeters', 'width': '20', 'width_measurement': 'meters','output_measurement': 'centimeters', 'shape': 'Rectangle'})
		self.assertEqual(result_10,200000)
 		#meter and cm to meter
		result_11 =compute.compute_rectangle_area({'length': '10', 'length_measurement': 'meters', 'width': '90', 'width_measurement': 'centimeters','output_measurement': 'meters', 'shape': 'Rectangle'})
		self.assertEqual(result_11,9)
 		#meter and inch to meter
		result_12 =compute.compute_rectangle_area({'length': '15', 'length_measurement': 'meters', 'width': '25', 'width_measurement': 'inches','output_measurement': 'meters', 'shape': 'Rectangle'})
		self.assertEqual(result_12,9.6)	 	

if __name__ =='__main':
	unittest.main()