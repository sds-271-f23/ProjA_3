#import needed packages
import numpy as np

class MonteCarlo:
    def __init__(self, radius, iterations, nthrows):
    # Initializing a monteCarlo method with radisu,iterations, and nthrows as parameters
        self.radius = radius
        self.iterations = iterations
        self.nthrows = nthrows 
        # initlaizlize a 2D NumPy array as the attribute of the MonteCarlo class.
        self.coordinates = np.zeros(nthrows)

    def random_dart(self): 
    # Generating the random coordinates(x,y) for the nthrows for the monteCarlo stimulation. It returns the coordiantes.
        half_x = np.random()
        half_y = np.random()
        return (2*half_x, 2*half_y)
       
    def throw_darts(self):
    # Creates random numbers of dart throws and store them in the coordinates 
        for i in range(self.nthrows):
            self.coordinates[i] = self.random_dart()
    
    def check_circle(self):
    #want to check if the coordinate is smaller than the radius of the circle to confirm it is inside circle

    # Checks for thif the coordinate is smaller than the radius of the circle to confirm it is
        #inside the circle. Then it returns an integer the number of darts inside circle.
        
    # The for loop iterates through each nnumber of throws and updates the coordinates
        
    # Radius is used to find the distance of coordinates from origin.
            
        # if distance < radius of the circle the point falls inside the circle.
              
    def estimate_pi(self):
        # estimating pi with one experiment of nthrows, using Montecarlo stimulation.It returns a float(pi_value)
        
    # knowing the ratio of area for a circle is pi/4, we find the pi value as following
        
    
    def monte_carlo_sim(self):
        #create a list where the results can be stored inside
        results = []
        
        #for loop that uses the range of number of iterations to estimate pi, then append this to the results list.
        for i in range(self.iterations):
            self.coordinates = self.throw_darts()
            ratio = self.check_circle()/self.nthrows
            results.append(ratio)
            
        #turn the results list into an array
        results = numpy.asarray(results) 
         
        #calculate the mean
        mean = results.mean()
       
        #calculate std deviation
        std = results.std()
        
        #calculate std error using std deviation.
        se = std/np.sqrt(self.nthrows)
        
        #return or print these values
        return(mean, std, se)
            
    def visualization(self):
        #use coordinates in order to plot them onto the scatterplot
       
        #adding aesthetic(s)/details to the scatterplot: title, labels, etc. 
