# Copyright © June 2014 by Michael Brock
# Summer Internship @ St. Petersburg College (SPC)
# Images Storage Capacity on USB Drive

# This program demonstrates the use of simple functions in Python. It prompts
# the user for the size of a USB drive (in Gigabytes or Gigs) and passes
# that value to different functions which calculate the number of images that
# can be stored on it in various image file formats (gif, jpeg, png and tiff).

def main():
    
    # Get the size of a USB drive (in Gigabytes) from user (cast it as an int),
    # then convert it to bytes (i.e., usb_bytes = usb_gigs * 1000000000) and
    # assign it to the usb_bytes variable.
    usb_gigs = (int(input('How many Gigabytes is the USB drive? ')))
    usb_bytes = usb_gigs * 1000000000
    
    # Next, place your calls to the other functions here in main(), rather than 
    # from within the other functions, to help keep things more organized. Also,
    # remember to include the variable (i.e., argument) you want to pass to the
    # function inside the parenthesis (i.e., usb_bytes in this case).
    calculate_gif_storage(usb_bytes)
    calculate_jpeg_storage(usb_bytes)
    calculate_png_storage(usb_bytes)
    calculate_tiff_storage(usb_bytes)

# Define functions to calculate the number of images that can be stored on a USB
# drive in various image file formats. Be sure to name a parameter inside the
# parenthesis here (e.g., usb_bytes or similar). This tells the function what it
# should be looking for from the call statement in main(). You can rename them
# here if you want, but for this program it isn't necessary. In other words, the
# name of a parameter can be whatever you want it to be. Just you make sure that
# the argument you pass matches the parameter's data type.

# The calculate_gif_storage() function accepts the size of a USB drive
# in Gigs and calculates the number of GIF images that can be stored on it.
def calculate_gif_storage(usb_bytes):
    resolution = 480000
    color_depth = 1
    compression_rate = 5
    # Divide usb_bytes by the total size of 1 photo of this type.
    images = usb_bytes/((resolution * color_depth)/compression_rate)
    # You can use the format function here to reduce or eliminate significant
    # digits (i.e., numbers to the right of a decimal point) if you want, but
    # that's your call. However, since you can't store partial files, it seems
    # appropriate to have no decimal point or significant digits in this case,
    # so I used it here to eliminate both and to include a comma separator.
    # Note that a similar effect could be accomplished by casting the images
    # variable as an int instead, but that would only remove the decimal point
    # and significant digits and wouldn't include the comma separator. So using
    # the format function is the preferred method.
    print(format(images,',.0f'), "images in GIF format can be stored on this USB drive.")

# The calculate_jpeg_storage() function accepts the size of a USB drive
# in Gigs and calculates the number of JPEG images that can be stored on it.         
def calculate_jpeg_storage(usb_bytes):
    resolution = 480000
    color_depth = 3
    compression_rate = 25
    # Divide usb_bytes by the total size of 1 photo of this type.
    images = usb_bytes/((resolution * color_depth)/compression_rate) 
    print(format(images,',.0f'), "images in JPEG format can be stored on this USB drive.")

# The calculate_png_storage() function accepts the size of a USB drive
# in Gigs and calculates the number of PNG images that can be stored on it. 
def calculate_png_storage(usb_bytes):
    resolution = 480000
    color_depth = 3
    compression_rate = 8
    # Divide usb_bytes by the total size of 1 photo of this type.
    images = usb_bytes/((resolution * color_depth)/compression_rate) 
    print(format(images,',.0f'), "images in PNG format can be stored on this USB drive.")
    
# The calculate_tiff_storage() function accepts the size of a USB drive
# in Gigs and calculates the number of TIFF images that can be stored on it. 
def calculate_tiff_storage(usb_bytes):
    resolution = 480000
    color_depth = 6
    compression_rate = 8
    # Divide usb_bytes by the total size of 1 photo of this type.
    images = usb_bytes/((resolution * color_depth)/compression_rate) 
    print(format(images,',.0f'), "images in TIFF format can be stored on this USB drive.")

# Call the main() function to run the program.      
main ()
