import wave, struct
fileRead = wave.open("audio/448hz.wav", 'rb')
fileData = fileRead.readframes(fileRead.getnframes());
samplingFrequency = fileRead.getframerate()

fileReadParams = fileRead.getparams()
fileRead.close()
byteArrayData = bytearray(fileData)
squaredByteArrayData = 0
avr = 0
avr = float(avr)
avr = float(sum(byteArrayData) / len(byteArrayData))

var = 0
var = float(var)
for x in range(0,len(byteArrayData)):
  var += (byteArrayData[x] - avr) ** 2
var /= len(byteArrayData)
normalizedData = [x - avr for x in byteArrayData]

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
    print(lagVals[x])
    distance[i] = float(x - beginning)

    print(distance[i])
    hits = hits +1
    beginning = x
    i = i + 1
    x = x +1
avrDistance = float(sum(distance) / hits)
Hertz = (samplingFrequency/avrDistance)
print("Hertz:")
print(Hertz)

BPM = Hertz * 60
print ("BPM: ")
print(BPM)




