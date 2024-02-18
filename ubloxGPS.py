from ublox_gps import UbloxGps
import serial
import json

# Can also use SPI here - import spidev
# I2C is not supported

port = serial.Serial('/dev/ttyACM0', baudrate=38400, timeout=1)
gps = UbloxGps(port)

def run():
  
  try: 
    # print("Listenting for UBX Messages.")
    # while True:
    try: 
        coords = gps.geo_coords()
        # references:
        # https://github.com/sparkfun/Qwiic_Ublox_Gps_Py/
        # https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
        # https://www.w3schools.com/python/ref_string_format.asp
        # https://stackoverflow.com/questions/5466451/how-do-i-escape-curly-brace-characters-in-a-string-while-using-format-or

            # Create Dictionary
        value = {
            "name": "Map",
            "lat": coords.lat,
            "lon": coords.lon
        }
        print("{{\"name\":\"Map\",\"lat\":{lat},\"lon\":{lon}}}".format(lat = round(coords.lat,4), lon = round(coords.lon,4)))
        # print(coords.lon, coords.lat)
    except (ValueError, IOError) as err:
        print(err)
  
  finally:
    port.close()

if __name__ == '__main__':
  run()

# preferred  format JSON
# {"name":"Map","lat":43.27225,"lon":-79.92025}


# {name:"Map",lat:43.2498,lon:-79.9247}
