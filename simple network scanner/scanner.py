import os


network = "192.168.1"

print("Scanning network...\n")
for i in range(1, 20):   
    ip = network + str(i)
    response = os.system("ping -n 1 " + ip + ">nul")

    print("checking:",ip)
    print("Device found:", ip)

print("\nScan finished")    