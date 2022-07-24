import wave, numpy, struct, matplotlib.pyplot as plt


fileRead = wave.open("audio/test.wav", 'rb')
fileData = fileRead.readframes(fileRead.getnframes()); 


fileReadParams = fileRead.getparams();
fileRead.close();
byteArrayData = bytearray(fileData);
##print(byteArrayData)
##print(fileData)
dt = numpy.dtype(int)
##fileData = numpy.frombuffer(fileData,dtype=dt) / 10;
print(byteArrayData)
##for x in range(len(byteArrayData)):
##   byteArrayData[x] = byteArrayData[x]>>1;

##print(fileData[0])

##fileData = bytearray(fileData)
plt.figure(1);
plt.title("Wav file")#
plt.plot(byteArrayData)
plt.show()
fileData = bytearray(fileData);
##print(fileData)
fileWrite = wave.open( "audio/writeout.wav", 'wb');
fileWrite.setparams(fileReadParams);
fileWrite.writeframes(byteArrayData);
fileWrite.close();


