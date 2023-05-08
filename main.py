from load_data import load_ephemeris, load_star_data
from utils import np, sf, plt, ps, datetime, load, tzwhere, timezone, utc, wgs84, Star, build_stereographic_projection

ephemeris = load_ephemeris()
star_data = load_star_data()
local_position = [51.0447, 114.0719]
time = datetime.now()

#local_timezone_string = tzwhere.tzwhere().tzNameAt(local_position[0], local_position[1])
#local_timezone = timezone('UTC')
#utc_dt = local_timezone.localize(datetime, is_dst=None).astimezone(utc)

#time = load.timescale().from_datetime(utc_dt)
observer = wgs84.latlon(latitude_degrees=local_position[0], longitude_degrees=local_position[1]).at(time)

sun, earth = ephemeris['sun'], ephemeris['earth']

celestial_position = observer.from_altaz(alt_degrees=90, az_degrees=0)
right_ascension, declination, distance = observer.radec()

center = earth.at(time).observe(Star(ra=right_ascension, dec=declination))
projection = build_stereographic_projection(center)

star_positions = earth.at(time).observe(Star.from_dataframe(star_data))
star_data['x'], star_data['y'] = projection(star_positions)

# Star plot

star_plot = plt.plot(figsize = (20,20), facecolor='#041A40')

plt.show()

