#import needed packages
class MonteCarlo:
    def __init__(self, radius, iterations, nthrows):
    # Initializing a monteCarlo method with radisu,iterations, and nthrows as parameters
        
   # initlaizlize a 2D NumPy array as the attribute of the MonteCarlo class.
    def random_dart(self): 
    # Generating the random coordinates(x,y) for the nthrows for the monteCarlo stimulation. It returns the coordiantes.
       
    def throw_darts(self):
    # Creates random numbers of dart throws and store them in the coordinates
       
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
        
        #for loop that uses the range of number of iterations to estimate pi, then append this to the results list.
         
        #turn the results list into an array
         
        #calculate the mean
       
        #calculate std deviation
        
        #calculate std error using std deviation.
        
        #return or print these values
        
            
    def visualization(self):
        #use coordinates in order to plot them onto the scatterplot
       
        #adding aesthetic(s)/details to the scatterplot: title, labels, etc. 
