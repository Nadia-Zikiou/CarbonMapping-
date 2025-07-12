import arcpy
from arcpy.sa import *
import os
import csv

# --- Spectral Index Functions ---

def calculate_ndvi(nir, red):
    return (Raster(nir) - Raster(red)) / (Raster(nir) + Raster(red))

def calculate_nirv(nir, red):
    ndvi = calculate_ndvi(nir, red)
    return ndvi * Raster(nir)

def calculate_savi(nir, red, L=0.5):
    return ((Raster(nir) - Raster(red)) / (Raster(nir) + Raster(red) + L)) * (1 + L)

def calculate_cigreen(nir, green):
    return Raster(nir) / Raster(green) - 1

# --- Utility Functions ---

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def calculate_statistics(raster):
    mean = arcpy.management.GetRasterProperties(raster, "MEAN").getOutput(0)
    std = arcpy.management.GetRasterProperties(raster, "STD").getOutput(0)
    return float(mean), float(std)

def export_statistics_to_csv(stats_dict, output_csv_path):
    with open(output_csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Index', 'Mean', 'Standard_Deviation'])
        for name, (mean, std) in stats_dict.items():
            writer.writerow([name, mean, std])
