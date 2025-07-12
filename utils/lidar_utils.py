# utils/lidar_utils.py

import arcpy
import os

def convert_laz_to_las(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    arcpy.env.workspace = input_folder
    laz_files = arcpy.ListFiles("*.laz")

    for laz_file in laz_files:
        las_file = os.path.join(output_folder, os.path.splitext(laz_file)[0] + ".las")
        arcpy.conversion.ConvertLas(input=laz_file, out_las=las_file)
        print(f"Converted {laz_file} to {las_file}")

def create_dtm(input_las, output_dtm):
    arcpy.management.LasDatasetToRaster(input_las, output_dtm, "ELEVATION", "BINNING", "MINIMUM", 1)
    print(f"DTM saved to {output_dtm}")

def create_dsm(input_las, output_dsm):
    arcpy.management.LasDatasetToRaster(input_las, output_dsm, "ELEVATION", "BINNING", "MAXIMUM", 1)
    print(f"DSM saved to {output_dsm}")

def create_intensity_raster(input_las, output_intensity):
    arcpy.management.LasDatasetToRaster(input_las, output_intensity, "INTENSITY", "BINNING", "MEAN", 1)
    print(f"Intensity raster saved to {output_intensity}")

def create_density_raster(input_las, output_density):
    arcpy.management.LasDatasetToRaster(input_las, output_density, "POINT_COUNT", "BINNING", "SUM", 1)
    print(f"Density raster saved to {output_density}")
