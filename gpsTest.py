def getLatLongFromNMEA(nmeaSen):
        lat = nmeaSen[2]
        latDir = 1.0 if nmeaSen[3] == 'N' else -1.0

        #Parse latitude to google maps coordinate
        hours = float(lat[0:2])
        mins = float(lat[2:])
        lat = latDir * (hours + mins / 60.0)

        lon = nmeaSen[4]
        lonDir = 1.0 if nmeaSen[5] == 'E' else -1.0

        #Parse longitude to google maps coordinates
        hours = float(lon[0:3])
        mins = float(lon[3:])
        lon = lonDir * (hours + mins / 60.0)

        return [lat, lon]

sigStr = "$GPGGA,225446,4916.45,N,12311.12,W,000.5,054.7,191194,020.3,E*68"
strArr = sigStr.split(',')
lat, lon = getLatLongFromNMEA(strArr)
print lat
print lon
