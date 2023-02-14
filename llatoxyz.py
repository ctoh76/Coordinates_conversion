import math

def convert_to_cartesian(ref_lat, ref_lon, ref_alt, target_lat, target_lon, target_alt):
    # Convert degrees to radians
    ref_lat = math.radians(ref_lat)
    ref_lon = math.radians(ref_lon)
    target_lat = math.radians(target_lat)
    target_lon = math.radians(target_lon)

    # Define constants
    R = 6371000  # Earth's radius in meters
    f = 1 / 298.257223563  # Earth's flattening

    # Calculate the geocentric latitude and altitude of the reference point
    e2 = 2*f - f**2  # Square of the eccentricity
    N = R / math.sqrt(1 - e2*math.sin(ref_lat)**2)  # Radius of curvature in the prime vertical
    x_ref = (N + ref_alt) * math.cos(ref_lat) * math.cos(ref_lon)
    y_ref = (N + ref_alt) * math.cos(ref_lat) * math.sin(ref_lon)
    z_ref = (N*(1-e2) + ref_alt) * math.sin(ref_lat)

    # Calculate the geocentric latitude and altitude of the target point
    N = R / math.sqrt(1 - e2*math.sin(target_lat)**2)  # Radius of curvature in the prime vertical
    x_target = (N + target_alt) * math.cos(target_lat) * math.cos(target_lon)
    y_target = (N + target_alt) * math.cos(target_lat) * math.sin(target_lon)
    z_target = (N*(1-e2) + target_alt) * math.sin(target_lat)

    # Calculate the Cartesian coordinates relative to the reference point
    x = x_target - x_ref
    y = y_target - y_ref
    z = z_target - z_ref

    return (x, y, z)

    # Example usage
    ref_lat = 37.7749
    ref_lon = -122.4194
    ref_alt = 0
    target_lat = 51.5074
    target_lon = -0.1278
    target_alt = 0
    x, y, z = convert_to_cartesian(ref_lat, ref_lon, ref_alt, target_lat, target_lon, target_alt)
    return x,y,z
 
