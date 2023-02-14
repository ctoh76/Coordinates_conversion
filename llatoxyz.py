import math

#WGS84 ellipsoid model to cartesian
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
"""
The first function, cartesian_to_ecef, takes Cartesian coordinates (x, y, z) and returns ECEF coordinates (x_ecef, y_ecef, z_ecef) using the WGS84 ellipsoid model. 
The second function, ecef_to_lla, takes ECEF coordinates and returns LLA coordinates (latitude, longitude, altitude) using the same ellipsoid model.

To use the functions, first call cartesian_to_ecef with your Cartesian coordinates to get ECEF coordinates. Then, call ecef_to_lla with the ECEF coordinates to get LLA coordinates, as shown in the example usage. The output will be printed to the console.
"""
def cartesian_to_ecef(x, y, z):
    # Constants for WGS84 ellipsoid model
    a = 6378137.0
    b = 6356752.314245
    f = (a - b) / a
    e_sq = f * (2 - f)

    # Calculate ECEF coordinates
    N = a / math.sqrt(1 - e_sq * math.sin(math.radians(y))**2)
    x_ecef = (N + z) * math.cos(math.radians(y)) * math.cos(math.radians(x))
    y_ecef = (N + z) * math.cos(math.radians(y)) * math.sin(math.radians(x))
    z_ecef = ((1 - e_sq) * N + z) * math.sin(math.radians(y))

    return x_ecef, y_ecef, z_ecef


def ecef_to_lla(x, y, z):
    # Constants for WGS84 ellipsoid model
    a = 6378137.0
    b = 6356752.314245
    f = (a - b) / a
    e_sq = f * (2 - f)

    # Calculate longitude and latitude
    lon = math.atan2(y, x)
    p = math.sqrt(x**2 + y**2)
    lat = math.atan2(z, p*(1-e_sq))
    N = a / math.sqrt(1 - e_sq*math.sin(lat)**2)

    # Calculate altitude
    alt = p / math.cos(lat) - N

    # Convert to degrees
    lon = math.degrees(lon)
    lat = math.degrees(lat)

    return lat, lon, alt
