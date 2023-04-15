# Copyright TU Wien (2022) - EVC: Task3
# Computer Vision Lab
# Institute of Computer Graphics and Algorithms

import numpy as np

def evc_white_balance(input_image: np.ndarray, white: np.ndarray) -> np.ndarray:
    """evc_white_balance performs white balancing manually.
    
      INPUT
      input       ... image
      white       ... a color (as RGB vector) that should become the new white
    
      OUTPUT
      result      ... result after white balance"""
    
    ### STUDENT CODE
    # TODO: perform white balancing using the 'white' variable
	  # HINT: Make sure the program does not crash if 'white' is zero!
    # NOTE: pixels brighter than 'white' will have values > 1.
    #       This requires a normalization which will be performed
    #       during the histogram clipping.
    # NOTE: The following line can be removed. It prevents the framework
    #       from crashing.

    # Check if white is zero to avoid division by zero
    if np.all(white == 0):
        return input_image
    
    # Normalize the image with the white point
    normalized = input_image / white
    
    # Clip the pixel values to the range [0, 1]
    clipped = np.clip(normalized, 0, 1)
    
    # Return the result
    result = np.minimum(clipped, 1)
    return clipped 
    ### END STUDENT CODE
    
    
