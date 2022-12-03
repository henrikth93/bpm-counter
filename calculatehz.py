def calculateHz(byteArrayData, samplingFrequency):
  avr = 0.0
  avr = float(sum(byteArrayData) / len(byteArrayData))
  var = 0.0

  for x in range(0,len(byteArrayData)):
    var += (byteArrayData[x] - avr) ** 2
  var /= len(byteArrayData)

  corrVal = 0
  divVal = 0
  lagVals = []


  for i in range(len(byteArrayData)):
    lagVals.append(0)
  for x in byteArrayData:
    divVal += float((x - avr) ** 2)
  for lag in range(0, len(byteArrayData)):
    corrVal = 0;

    for x in range(0,len(byteArrayData)-lag):
      corrVal += float((byteArrayData[x] - avr) * (byteArrayData[x + lag] - avr))
    lagVals[lag] = corrVal/divVal

  hits = 0
  beginning = 0
  distance = []
  for i in range(len(lagVals)):
    distance.append(0)
  i = 1
  for x in range(1,len(lagVals)-2):
    if (lagVals[x] > lagVals[x-1] and  lagVals[x] > lagVals[x+1] and lagVals[x] > 0.8):
      distance[i] = float(x - beginning)
      hits = hits +1
      beginning = x
      i = i + 1
      x = x +1
  avrDistance = float(sum(distance) / hits)
  Hertz = (samplingFrequency/avrDistance)
  BPM = Hertz * 60
  return Hertz, BPM;