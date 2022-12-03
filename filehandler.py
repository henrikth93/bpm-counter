import wave
def fileHandler(filename):
  fileRead = wave.open(filename, 'rb')
  fileData = fileRead.readframes(fileRead.getnframes());
  samplingFrequency = fileRead.getframerate()

  fileRead.close()
  byteArrayData = bytearray(fileData)
  return byteArrayData, samplingFrequency