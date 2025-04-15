"""
Draw kaniza squares

    add_pacman() adds pacman shape to an existing figure

    add_full_circles() adds circles to an existing image
    
    border_kaniza_sqr() draws kaniza squares

    border_kaniza_sqr_with_square() draws kaniza squares with a line square connecting the pacmans

    line_border_sqr(): draw the borders of a square

    non_kaniza_sqr():  have packman facing outward

    circle_sqr(): draw 4 circles so the circles form the corners of a square
    
"""
import numpy as np
from PIL import Image, ImageDraw



light_grey_value=255 * 2 // 3
light_grey=(light_grey_value,light_grey_value,light_grey_value)

dark_grey_value=255//3
dark_grey=(dark_grey_value,dark_grey_value,dark_grey_value)

image_size=(160,128)

def add_pacman(image, center, radius=13, mouth_angle=90, orientation=0, pacman_color=dark_grey):
    """
    Draws a Pac-Man–like figure onto an existing PIL image.
    
    Parameters:
        image (PIL.Image): The image to modify.
        center (tuple): The (x, y) coordinates for the center of Pac-Man.
        radius (float): The radius of Pac-Man.
        mouth_angle (float): The total opening angle (in degrees) for the mouth.
        orientation (int): 0,1,2,3;  
            0:(right_down facing);  1:(right_up facing); 2:(left_up facing); 3:(left_down facing)
        pacman_color (tuple): The fill color for Pac-Man (default is yellow).
        
    Returns:
        PIL.Image: The image with the Pac-Man figure drawn on it.
    """
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    
    # re-asign orentation so the angle is in degrees: 0 is right facing
    orientation= 45+ orientation*90


    # Calculate the arc angles (in degrees) for the body (a circle minus a wedge for the mouth)
    start_angle = orientation + mouth_angle / 2
    end_angle = orientation - mouth_angle / 2 + 360  # ensure proper ordering
    
    # Generate points along the arc using NumPy
    theta = np.linspace(np.deg2rad(start_angle), np.deg2rad(end_angle), num=100)
    arc_points = [(center[0] + radius * np.cos(t), center[1] + radius * np.sin(t)) for t in theta]
    
    # Create the polygon points: start at the center, then follow the arc
    polygon_points = [center] + arc_points
    
    # Draw the filled Pac-Man polygon
    draw.polygon(polygon_points, fill=pacman_color)
    
    return image

def add_full_circle(image, center, radius=13, circle_color=dark_grey):
    """
    Draws a full circle onto an existing PIL image.
    
    Parameters:
        image (PIL.Image): The image to modify.
        center (tuple): The (x, y) coordinates for the center of the circle.
        radius (float): The radius of the circle.
        circle_color (tuple): The fill color for the circle (default is dark grey).
        
    Returns:
        PIL.Image: The image with the full circle drawn on it.
    """
    # Create a drawing context
    draw = ImageDraw.Draw(image)
    
    # Calculate the bounding box for the circle.
    # The bounding box is defined by the top-left and bottom-right points.
    left = center[0] - radius
    top = center[1] - radius
    right = center[0] + radius
    bottom = center[1] + radius
    
    # Draw the circle (ellipse with a square bounding box)
    draw.ellipse([left, top, right, bottom], fill=circle_color)
    
    return image




def border_kaniza_sqr (image_size=(160,128), orientation=0, width=52, pacman_color=light_grey, background_color=dark_grey,r=13):
    """
    make an image with kaniza square, with one of the imaginary edges crossing the center
    of the image

    the kaniza square can either be up, down, right, or, left. 
    to avoid diagnol (step like diagonal edges) 

    Pramenters:
        image_size(width,height): the size of the image
        orientation(int): 0 1 2 3
            0(up) 1(right) 2(down) 3(left)
        pacman_color: RGB colors (,,) of kaniza inducers
        background_color: background color of the entire image
        r: radius of the pacman inducers


    """

    # create new image of image_size
    img = Image.new("RGB", image_size, background_color)
    mouth_angle=90
    
    #up orientation
    if orientation==0:
        bot_y=image_size[1]//2
        top_y=image_size[1]//2-width
        left_x=image_size[0]//2 -width//2
        right_x=image_size[0]//2 +width//2


        #top_left pacman
        img = add_pacman(img, (left_x,top_y), r, mouth_angle, 0,pacman_color)
        #top_right pacman
        img = add_pacman(img, (right_x,top_y), r, mouth_angle, 1,pacman_color)
        #bottom_left pacman
        img = add_pacman(img, (left_x,bot_y), r, mouth_angle, 3,pacman_color)
        #bottom_right pacman
        img = add_pacman(img, (right_x,bot_y), r, mouth_angle, 2, pacman_color)
   
    #right orentation
    elif orientation==1:
        bot_y=image_size[1]//2+width//2
        top_y=image_size[1]//2-width//2
        left_x=image_size[0]//2 
        right_x=image_size[0]//2 +width
        #top_left pacman
        img = add_pacman(img, (left_x,top_y), r, mouth_angle, 0,pacman_color)
        #top_right pacman
        img = add_pacman(img, (right_x,top_y), r, mouth_angle, 1,pacman_color)
        #bottom_left pacman
        img = add_pacman(img, (left_x,bot_y), r, mouth_angle, 3,pacman_color)
        #bottom_right pacman
        img = add_pacman(img, (right_x,bot_y), r, mouth_angle, 2, pacman_color)

    #down orientation
    elif orientation==2:
        bot_y=image_size[1]//2+width
        top_y=image_size[1]//2
        left_x=image_size[0]//2 -width//2
        right_x=image_size[0]//2 +width//2


        #top_left pacman
        img = add_pacman(img, (left_x,top_y), r, mouth_angle, 0,pacman_color)
        #top_right pacman
        img = add_pacman(img, (right_x,top_y), r, mouth_angle, 1,pacman_color)
        #bottom_left pacman
        img = add_pacman(img, (left_x,bot_y), r, mouth_angle, 3,pacman_color)
        #bottom_right pacman
        img = add_pacman(img, (right_x,bot_y), r, mouth_angle, 2, pacman_color)
    
    #left orientation
    elif orientation==3:
        bot_y=image_size[1]//2+width//2
        top_y=image_size[1]//2-width//2
        left_x=image_size[0]//2 - width
        right_x=image_size[0]//2
        #top_left pacman
        img = add_pacman(img, (left_x,top_y), r, mouth_angle, 0,pacman_color)
        #top_right pacman
        img = add_pacman(img, (right_x,top_y), r, mouth_angle, 1,pacman_color)
        #bottom_left pacman
        img = add_pacman(img, (left_x,bot_y), r, mouth_angle, 3,pacman_color)
        #bottom_right pacman
        img = add_pacman(img, (right_x,bot_y), r, mouth_angle, 2, pacman_color)
    return img

def border_kaniza_sqr_with_square(image_size=(160,128), orientation=0, width=52, 
                                  pacman_color=light_grey, background_color=dark_grey, r=13,
                                  square_line_color=light_grey, square_line_width=1):
    """
    Creates an image with a Kaniza square by drawing four Pac-Man–like inducers using border_kaniza_sqr,
    then draws a square (i.e. lines connecting the centers of the four inducers) over the image.
    
    Parameters:
        image_size (tuple): The size of the image (width, height).
        orientation (int): Orientation of the Kaniza square:
                           0: up, 1: right, 2: down, 3: left.
        width (int): The width (or height) of the Kaniza square element.
        pacman_color (tuple): The RGB color for the Kaniza inducers.
        background_color (tuple): The RGB background color for the image.
        r (int): The radius of the inducers.
        square_line_color (tuple): The RGB color for the connecting square (default black).
        square_line_width (int): The width of the square line.
    
    Returns:
        PIL.Image: The generated image with the inducers and the connecting square.
    """

    # First, generate the Kaniza square image with Pac-Man–like inducers.
    img = border_kaniza_sqr(image_size=image_size, orientation=orientation, width=width,
                            pacman_color=pacman_color, background_color=background_color, r=r)
    
    # Now determine the center coordinates used to position the inducers.
    # These centers correspond to the coordinates used in border_kaniza_sqr.
    if orientation == 0:
        # "Up" orientation:
        # The imaginary square is above the center (one edge crosses the center).
        bot_y = image_size[1] // 2
        top_y = image_size[1] // 2 - width
        left_x = image_size[0] // 2 - width // 2
        right_x = image_size[0] // 2 + width // 2
    elif orientation == 1:
        # "Right" orientation:
        bot_y = image_size[1] // 2 + width // 2
        top_y = image_size[1] // 2 - width // 2
        left_x = image_size[0] // 2
        right_x = image_size[0] // 2 + width
    elif orientation == 2:
        # "Down" orientation:
        bot_y = image_size[1] // 2 + width
        top_y = image_size[1] // 2
        left_x = image_size[0] // 2 - width // 2
        right_x = image_size[0] // 2 + width // 2
    elif orientation == 3:
        # "Left" orientation:
        bot_y = image_size[1] // 2 + width // 2
        top_y = image_size[1] // 2 - width // 2
        left_x = image_size[0] // 2 - width
        right_x = image_size[0] // 2
    else:
        raise ValueError("Orientation must be 0, 1, 2, or 3.")
    
    # The centers for the four inducers drawn in border_kaniza_sqr (they are passed to add_pacman)
    # are:
    top_left = (left_x, top_y)
    top_right = (right_x, top_y)
    bottom_left = (left_x, bot_y)
    bottom_right = (right_x, bot_y)
    
    # Now draw a square connecting these four centers.
    draw = ImageDraw.Draw(img)
    # Define a closed polygon by listing the points in order and closing the loop.
    square_points = [top_left, top_right, bottom_right, bottom_left, top_left]
    
    # Draw the connecting line. (Alternatively, draw.polygon(square_points, outline=square_line_color)
    # if you prefer.)
    draw.line(square_points, fill=square_line_color, width=square_line_width)
    
    return img


def line_border_sqr(image_size=(160,128), orientation=0, width=52, 
                                background_color=dark_grey,
                                  square_line_color=light_grey, square_line_width=1):
    """
    Creates an image with borders of a square
    
    Parameters:
        image_size (tuple): The size of the image (width, height).
        orientation (int): Orientation of the Kaniza square:
                           0: up, 1: right, 2: down, 3: left.
        width (int): The width (or height) of the square element.
        
        background_color (tuple): The RGB background color for the image.
        square_line_color (tuple): The RGB color for the connecting square (default black).
        square_line_width (int): The width of the square line.
    
    Returns:
        PIL.Image: The generated image with the inducers and the connecting square.
    """

    # First, generate the Kaniza square image with Pac-Man–like inducers.
    img = Image.new("RGB", image_size, background_color)
    
    # Now determine the center coordinates used to position the inducers.
    # These centers correspond to the coordinates used in border_kaniza_sqr.
    if orientation == 0:
        # "Up" orientation:
        # The imaginary square is above the center (one edge crosses the center).
        bot_y = image_size[1] // 2
        top_y = image_size[1] // 2 - width
        left_x = image_size[0] // 2 - width // 2
        right_x = image_size[0] // 2 + width // 2
    elif orientation == 1:
        # "Right" orientation:
        bot_y = image_size[1] // 2 + width // 2
        top_y = image_size[1] // 2 - width // 2
        left_x = image_size[0] // 2
        right_x = image_size[0] // 2 + width
    elif orientation == 2:
        # "Down" orientation:
        bot_y = image_size[1] // 2 + width
        top_y = image_size[1] // 2
        left_x = image_size[0] // 2 - width // 2
        right_x = image_size[0] // 2 + width // 2
    elif orientation == 3:
        # "Left" orientation:
        bot_y = image_size[1] // 2 + width // 2
        top_y = image_size[1] // 2 - width // 2
        left_x = image_size[0] // 2 - width
        right_x = image_size[0] // 2
    else:
        raise ValueError("Orientation must be 0, 1, 2, or 3.")
    
    # The centers for the four inducers drawn in border_kaniza_sqr (they are passed to add_pacman)
    # are:
    top_left = (left_x, top_y)
    top_right = (right_x, top_y)
    bottom_left = (left_x, bot_y)
    bottom_right = (right_x, bot_y)
    
    # Now draw a square connecting these four centers.
    draw = ImageDraw.Draw(img)
    # Define a closed polygon by listing the points in order and closing the loop.
    square_points = [top_left, top_right, bottom_right, bottom_left, top_left]
    
    # Draw the connecting line. (Alternatively, draw.polygon(square_points, outline=square_line_color)
    # if you prefer.)
    draw.line(square_points, fill=square_line_color, width=square_line_width)
    
    return img

def non_kaniza_sqr (image_size=(160,128), orientation=0, width=52, pacman_color=light_grey, background_color=dark_grey,r=13):
    """
    make an image with kaniza square, with one of the imaginary edges crossing the center
    of the image

    the kaniza square can either be up, down, right, or, left. 
    to avoid diagnol (step like diagonal edges) 

    Pramenters:
        image_size(width,height): the size of the image
        orientation(int): 0 1 2 3
            0(up) 1(right) 2(down) 3(left)
        pacman_color: RGB colors (,,) of kaniza inducers
        background_color: background color of the entire image
        r: radius of the pacman inducers


    """

    # create new image of image_size
    img = Image.new("RGB", image_size, background_color)
    mouth_angle=90
    
    #up orientation
    if orientation==0:
        bot_y=image_size[1]//2
        top_y=image_size[1]//2-width
        left_x=image_size[0]//2 -width//2
        right_x=image_size[0]//2 +width//2


        #top_left pacman
        img = add_pacman(img, (left_x,top_y), r, mouth_angle, 2,pacman_color)
        #top_right pacman
        img = add_pacman(img, (right_x,top_y), r, mouth_angle, 3,pacman_color)
        #bottom_left pacman
        img = add_pacman(img, (left_x,bot_y), r, mouth_angle, 1,pacman_color)
        #bottom_right pacman
        img = add_pacman(img, (right_x,bot_y), r, mouth_angle, 0, pacman_color)
   
    #right orentation
    elif orientation==1:
        bot_y=image_size[1]//2+width//2
        top_y=image_size[1]//2-width//2
        left_x=image_size[0]//2 
        right_x=image_size[0]//2 +width
        #top_left pacman
        img = add_pacman(img, (left_x,top_y), r, mouth_angle, 2,pacman_color)
        #top_right pacman
        img = add_pacman(img, (right_x,top_y), r, mouth_angle, 3,pacman_color)
        #bottom_left pacman
        img = add_pacman(img, (left_x,bot_y), r, mouth_angle, 1,pacman_color)
        #bottom_right pacman
        img = add_pacman(img, (right_x,bot_y), r, mouth_angle, 0, pacman_color)

    #down orientation
    elif orientation==2:
        bot_y=image_size[1]//2+width
        top_y=image_size[1]//2
        left_x=image_size[0]//2 -width//2
        right_x=image_size[0]//2 +width//2


        #top_left pacman
        img = add_pacman(img, (left_x,top_y), r, mouth_angle, 2,pacman_color)
        #top_right pacman
        img = add_pacman(img, (right_x,top_y), r, mouth_angle, 3,pacman_color)
        #bottom_left pacman
        img = add_pacman(img, (left_x,bot_y), r, mouth_angle, 1,pacman_color)
        #bottom_right pacman
        img = add_pacman(img, (right_x,bot_y), r, mouth_angle, 0, pacman_color)
    
    #left orientation
    elif orientation==3:
        bot_y=image_size[1]//2+width//2
        top_y=image_size[1]//2-width//2
        left_x=image_size[0]//2 - width
        right_x=image_size[0]//2
        #top_left pacman
        img = add_pacman(img, (left_x,top_y), r, mouth_angle, 2,pacman_color)
        #top_right pacman
        img = add_pacman(img, (right_x,top_y), r, mouth_angle, 3,pacman_color)
        #bottom_left pacman
        img = add_pacman(img, (left_x,bot_y), r, mouth_angle, 1,pacman_color)
        #bottom_right pacman
        img = add_pacman(img, (right_x,bot_y), r, mouth_angle, 0, pacman_color)
    return img
    
def circle_sqr(image_size=(160, 128), orientation=0, width=52, circle_color=light_grey, 
                    background_color=dark_grey, r=13):
    """
    Create an image with a Kaniza square, where one of the imaginary edges crosses 
    the center of the image, using full circles instead of Pac-Man shapes.

    Parameters:
        image_size (tuple): The size of the image (width, height).
        orientation (int): Orientation of the Kaniza square:
                           0: up, 1: right, 2: down, 3: left.
        width (int): The width (or height) of the Kaniza square element.
        circle_color (tuple): The fill color (RGB) for the circle inducers.
        background_color (tuple): The background color (RGB) for the entire image.
        r (int): The radius of the circle inducers.
        
    Returns:
        PIL.Image: The generated image.
    """

    # Create a new image with the specified background color
    img = Image.new("RGB", image_size, background_color)

    # For simplicity, we calculate the positions for four circles at the corners 
    # of the "square" element. The square is centered on the image.
    
    if orientation == 0:  # Up orientation
        bot_y = image_size[1] // 2
        top_y = image_size[1] // 2 - width
        left_x = image_size[0] // 2 - width // 2
        right_x = image_size[0] // 2 + width // 2
        
    elif orientation == 1:  # Right orientation
        bot_y = image_size[1] // 2 + width // 2
        top_y = image_size[1] // 2 - width // 2
        left_x = image_size[0] // 2
        right_x = image_size[0] // 2 + width
        
    elif orientation == 2:  # Down orientation
        bot_y = image_size[1] // 2 + width
        top_y = image_size[1] // 2
        left_x = image_size[0] // 2 - width // 2
        right_x = image_size[0] // 2 + width // 2
        
    elif orientation == 3:  # Left orientation
        bot_y = image_size[1] // 2 + width // 2
        top_y = image_size[1] // 2 - width // 2
        left_x = image_size[0] // 2 - width
        right_x = image_size[0] // 2

    # Draw the four circles at the corresponding positions.
    # Top-left circle
    img = add_full_circle(img, (left_x, top_y), r, circle_color)
    # Top-right circle
    img = add_full_circle(img, (right_x, top_y), r, circle_color)
    # Bottom-left circle
    img = add_full_circle(img, (left_x, bot_y), r, circle_color)
    # Bottom-right circle
    img = add_full_circle(img, (right_x, bot_y), r, circle_color)
    
    return img



# Example usage:
if __name__ == "__main__":
    
    # test pacman function code
    """
    # Load an existing image or create a new one (here we create a white image)
    img = Image.new("RGB", image_size, light_grey)
    
    # Pac-Man parameters
    center = (100, 60)      # center of the image
    radius = 7              # size of Pac-Man
    mouth_angle = 90        # mouth opening angle in degrees
    orientation = -45         # mouth faces right (0°)
    
    # Add the Pac-Man figure to the image
    img_with_pacman = add_pacman(img, (50,20), radius, mouth_angle, 0)
    img_with_pacman = add_pacman(img, (100,20), radius, mouth_angle, 1)
    img_with_pacman = add_pacman(img, (100,70), radius, mouth_angle, 2)
    img_with_pacman = add_pacman(img, (50,70), radius, mouth_angle, 3)
    img_with_pacman.show()
    """

    # Test  border_kaniza_sqr()
    radius = 13
    orent=[0,1,2,3]
    image_size=(160,128)
    inducer_color_=light_grey
    background_color_=dark_grey
    width,height=image_size
    middle_y= height//2
    middle_x=width//2
    """
    # test border_kaniza_sqr ():
    for i in range(len(orent)):
        image= border_kaniza_sqr (image_size, orent[i], 52, inducer_color_, background_color_,radius)
        draw =ImageDraw.Draw(image)
        # Draw a red horizontal line across the middle of the image
        draw.line((0, middle_y, width, middle_y), fill='red', width=2)
        # Draw a red vertical line across the middle of the image
        draw.line((middle_x, 0, middle_x, height), fill='red', width=2)

        image.show()

    #test non_kaniza_sqr():
    for i in range(len(orent)):
        image= non_kaniza_sqr (image_size, orent[i], 52, inducer_color_, background_color_,radius)
        draw =ImageDraw.Draw(image)
        # Draw a red horizontal line across the middle of the image
        draw.line((0, middle_y, width, middle_y), fill='red', width=2)
        # Draw a red vertical line across the middle of the image
        draw.line((middle_x, 0, middle_x, height), fill='red', width=2)

        image.show()
 
    #test circle_sqr():
    for i in range(len(orent)):
        image= circle_sqr (image_size, orent[i], 52, inducer_color_, background_color_,radius)
        draw =ImageDraw.Draw(image)
        # Draw a red horizontal line across the middle of the image
        draw.line((0, middle_y, width, middle_y), fill='red', width=2)
        # Draw a red vertical line across the middle of the image
        draw.line((middle_x, 0, middle_x, height), fill='red', width=2)

        image.show()

    # test border_kaniza_sqr_with_square()
    for i in range(len(orent)):
        image= border_kaniza_sqr_with_square (image_size, orent[i], 52, inducer_color_, background_color_,radius,square_line_color=inducer_color_,square_line_width=1)
        draw =ImageDraw.Draw(image)
        # Draw a red horizontal line across the middle of the image
            #draw.line((0, middle_y, width, middle_y), fill='red', width=2)
        # Draw a red vertical line across the middle of the image
            #draw.line((middle_x, 0, middle_x, height), fill='red', width=2)

        image.show()"""

    # test line_border_sqr()
    for i in range(len(orent)):
        image= line_border_sqr(image_size, orent[i], 52, background_color_,square_line_color=inducer_color_,square_line_width=1)
        draw =ImageDraw.Draw(image)
        # Draw a red horizontal line across the middle of the image
            #draw.line((0, middle_y, width, middle_y), fill='red', width=2)
        # Draw a red vertical line across the middle of the image
            #draw.line((middle_x, 0, middle_x, height), fill='red', width=2)

        image.show()