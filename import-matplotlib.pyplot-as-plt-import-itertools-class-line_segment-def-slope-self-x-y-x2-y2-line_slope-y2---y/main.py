import matplotlib.pyplot as plt
import itertools

class line_segment():
    def slope(self, x, y, x2, y2):
        line_slope = (y2 - y)/(x2 - x)
        return line_slope
    def intercept(self, slope, x, y):
        y_intercept = y - slope * x
        return y_intercept
        
def main():
    x1 = float(raw_input("Please enter the x coord for the starting point of a line: "))
    y1 = float(raw_input("Now the y coord, please: "))
    x2 = float(raw_input("Please enter the x ending point of the line: "))
    y2 = float(raw_input("Now the y ending point: "))
    
    your_line = line_segment()
    
    your_slope = your_line.slope(x1, y1, x2, y2)
    your_intercept = your_line.intercept(your_slope, x1, y1)
    
    print "The equation of your line is: y = %r * x + %r" % (your_slope, your_intercept)
    
    new_line = line_segment()
    
    xnew = x2 - 1
    ynew = your_slope * xnew + your_intercept
    nega_slope = -your_slope
    nega_intercept = new_line.intercept(nega_slope, xnew, ynew)
    
    print "Your new line is: y = %r * x + %r" % (nega_slope, nega_intercept)
    
    xnew1 = xnew - 0.5
    ynew1 = nega_slope * xnew1 + nega_intercept
    xnew2 = xnew + 0.5
    ynew2 = nega_slope * xnew2 + nega_intercept
    
fig = plt.figure()
ax = fig.add_subplot(111)
coords = [[x1, y1],[x2, y2],[xnew1, ynew1],[xnew2, ynew2]]
plt.plot(*zip(*itertools.chain.from_iterable(itertools.combinations(coords, 2))), color = 'brown', marker = 'o')

plt.show()

if __name__ == "__main__":
    main()
