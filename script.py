import gpxpy
import gpxpy.gpx
import math

def haversine(lat1, lon1, lat2, lon2):
    """Calcule la distance en mètres entre deux points GPS."""
    R = 6371000  # Rayon de la Terre en mètres
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def process_gpx(file_path, k=0.03):
    with open(file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    total_distance = 0
    total_time = 0
    corrected_paces = []

    # Parcours de chaque segment de track dans le fichier GPX
    for track in gpx.tracks:
        for segment in track.segments:
            points = segment.pointsPI
            for i in range(1, len(points)):
                pt1, pt2 = points[i-1], points[i]
                distance = haversine(pt1.latitude, pt1.longitude, pt2.latitude, pt2.longitude)
                elevation_diff = pt2.elevation - pt1.elevation
                grade = (elevation_diff / distance * 100) if distance != 0 else 0
                time_diff = (pt2.time - pt1.time).total_seconds() if (pt1.time and pt2.time) else 0
                if time_diff > 0 and distance > 0:
                    pace = (time_diff / 60) / (distance / 1000)  # minutes par km
                    corrected_pace = pace * (1 + k * grade)
                    corrected_paces.append(corrected_pace)
                    total_distance += distance
                    total_time += time_diff

    if corrected_paces:
        avg_corrected_pace = sum(corrected_paces) / len(corrected_paces)
    else:
        avg_corrected_pace = None

    print("Distance totale : {:.2f} km".format(total_distance / 1000))
    print("Temps total : {:.2f} minutes".format(total_time / 60))
    if avg_corrected_pace is not None:
        print("Pace moyen corrigé : {:.2f} min/km".format(avg_corrected_pace))
    else:
        print("Aucun calcul de pace n'a pu être effectué.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <fichier_gpx>")
        sys.exit(1)
    gpx_file_path = sys.argv[1]
    process_gpx(gpx_file_path)
