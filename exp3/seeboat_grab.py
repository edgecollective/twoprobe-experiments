import serial

PORT='/dev/ttyACM0'
OUTFILE='out.csv'
NUM_SAMPLES = 1000

f=open(OUTFILE,"w+")

s=serial.Serial(PORT,115200,timeout=1)

while True:
    line=s.readline()
    print(line)
    p=line.split(',')
    print(p)
    if len(p)>1:
        data=p[0]
        #vals=data.split(',')
        f.write(data)
        f.write('\n')
        f.flush()

f.close()

#s.write('ADC.STOP\n\r')
