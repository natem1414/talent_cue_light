from ola.ClientWrapper import ClientWrapper
import array

def DmxSent(state):
    if state.Succeeded():
        print("DMX sent successfully!")
    else:
        print("Error sending DMX:", state.message)

def main():
    universe = 1
    data = array.array('B')

    # Append DMX values for channels 1-3
    data.append(10)
    data.append(50)
    data.append(255)

    wrapper = ClientWrapper()
    client = wrapper.Client()

    # Send DMX frame
    client.SendDmx(universe, data, DmxSent)
    wrapper.Run()

if __name__ == '__main__':
    main()
