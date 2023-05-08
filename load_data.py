from utils import load, hipparcos

def load_ephemeris():
    ephemeris = load('de421.bsp')
    return ephemeris

def load_star_data():
    with load.open(hipparcos.URL) as f:
        star_data = hipparcos.load_dataframe(f)
    return star_data