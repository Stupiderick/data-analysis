# This python file convert the airport IATA three-letter code and the name of the cities to a readable form.
# Created by Erick Li.

def convert(theFile):
    '''
    Input the file and then convert the raw data to readable sentences.
    The raw data are written as:
        1st col: IATA code
        2nd col: city name
    @param: the path of the file
    '''
    with open(theFile, 'r') as myFile:
        for line in myFile:
            item = line.split('\n')
            code = item[1][:3]
            city = item[1][4:]
            print('The code of the airport of {0} is {1}'.format(city, code)). # Print out the readable sentences.
            
