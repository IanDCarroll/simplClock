from time import sleep

def chrono(seconds):
    count = 0
    while True:
        print "chronometer: %d" % count
        count += 1
        sleep(seconds)

if __name__ == '__main__':

    message = "Please enter the frequency in seconds (<CTRL C> to quit): "
    frequency = float(raw_input(message))
    try:
        chrono(frequency)
    except:
        print "\n\n\tChronometer Stopped.\n"
