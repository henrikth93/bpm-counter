import struct, filehandler, calculatehz




byteArrayData, samplingFrequency = filehandler.fileHandler("audio/400hz.wav");
Hz, BPM = calculatehz.calculateHz(byteArrayData, samplingFrequency);

print("Herz: ", Hz, "BPM: ", BPM)



