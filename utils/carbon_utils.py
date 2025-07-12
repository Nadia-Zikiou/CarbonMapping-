# utils/carbon_utils.py

import arcpy
from arcpy.sa import *
import csv
import os

arcpy.CheckOutExtension("Spatial")

def estimate_agb_and_carbon_change(workspace, agb_2016_path, agb_2023_path, output_dir):
    arcpy.env.workspace = workspace
    arcpy.env.overwriteOutput = True

    # Load input rasters
    agb_2016 = Raster(agb_2016_path)
    agb_2023 = Raster(agb_2023_path)

    # --- Compute AGB and Carbon Change ---
    agb_change = agb_2023 - agb_2016
    agb_change.save(os.path.join(output_dir, "AGB_Change_2016_2023.tif"))

    carbon_2016 = agb_2016 * 0.47
    carbon_2023 = agb_2023 * 0.47
    carbon_change = carbon_2023 - carbon_2016
    carbon_change.save(os.path.join(output_dir, "Carbon_Change_2016_2023.tif"))

    # --- Classify Change ---
    reclassed = Reclassify(agb_change, "Value", RemapRange([
        [-99999, -10, 1],
        [-10, 10, 2],
        [10, 99999, 3]
    ]))
    reclassed.save(os.path.join(output_dir, "AGB_Change_Classified.tif"))

    # --- Calculate Stats ---
    mean_agb_2016 = float(arcpy.GetRasterProperties_management(agb_2016, "MEAN").getOutput(0))
    mean_agb_2023 = float(arcpy.GetRasterProperties_management(agb_2023, "MEAN").getOutput(0))
    mean_carbon_2016 = mean_agb_2016 * 0.47
    mean_carbon_2023 = mean_agb_2023 * 0.47

    rows = int(arcpy.GetRasterProperties_management(agb_2023, "ROWCOUNT").getOutput(0))
    cols = int(arcpy.GetRasterProperties_management(agb_2023, "COLUMNCOUNT").getOutput(0))
    cell_size = float(arcpy.GetRasterProperties_management(agb_2023, "CELLSIZEX").getOutput(0))
    cell_area_ha = (cell_size ** 2) / 10000
    total_area_ha = rows * cols * cell_area_ha

    total_agb_2016 = mean_agb_2016 * total_area_ha
    total_agb_2023 = mean_agb_2023 * total_area_ha
    agb_diff = total_agb_2023 - total_agb_2016

    total_carbon_2016 = mean_carbon_2016 * total_area_ha
    total_carbon_2023 = mean_carbon_2023 * total_area_ha
    carbon_diff = total_carbon_2023 - total_carbon_2016
    annual_carbon_sequestration = carbon_diff / 7.0
    annual_co2eq = annual_carbon_sequestration * (44.0 / 12.0)
    co2_total_change = carbon_diff * (44.0 / 12.0)

    # --- Export CSV ---
    output_csv = os.path.join(output_dir, "Carbon_Change_Summary_2016_2023.csv")
    with open(output_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Metric", "Value"])
        writer.writerow(["Total Area (ha)", total_area_ha])
        writer.writerow(["Mean AGB 2016 (tons/ha)", mean_agb_2016])
        writer.writerow(["Mean AGB 2023 (tons/ha)", mean_agb_2023])
        writer.writerow(["Mean Carbon 2016 (tons/ha)", mean_carbon_2016])
        writer.writerow(["Mean Carbon 2023 (tons/ha)", mean_carbon_2023])
        writer.writerow(["AGB Gain (tons)", agb_diff])
        writer.writerow(["Carbon Gain (tons)", carbon_diff])
        writer.writerow(["Annual Carbon Sequestration (tons/year)", annual_carbon_sequestration])
        writer.writerow(["Annual CO2e Sequestration (tons/year)", annual_co2eq])
        writer.writerow(["Total CO2e Change (tons)", co2_total_change])

    print("Change analysis complete. Rasters and summary CSV saved.")

    arcpy.CheckInExtension("Spatial")
