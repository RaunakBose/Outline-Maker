import filtering
import cv2

if __name__ == "__main__":
    print('Enter image name:')
    image_name = input()
    input_image = cv2.imread(image_name, 0)
    outline = filtering.Filtering(input_image)
    an_outline = outline.getOutline()
    output_image_name = "outline.jpg"
    cv2.imwrite(output_image_name, an_outline)
