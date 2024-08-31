from django.shortcuts import render,redirect
from .models import ImageResize
from .forms import ImageResizerForm
import cv2

def resize_image_view(request):
    if request.method == "POST":
        form = ImageResizerForm(request.POST, request.FILES)
        if form.is_valid():
            image_resize_instance = form.save()

            image_path = image_resize_instance.image.path
            resize_percentage = image_resize_instance.resize_percentage 

            image = cv2.imread(image_path)# image lai leko image_path mah math vako wala lai leko hai tah 

            #When you load an image using OpenCV with cv2.imread(), the image is represented as a NumPy array. The dimensions of this array can be accessed using the shape attribute:

            # image.shape[0]: Represents the height (number of rows).
            # image.shape[1]: Represents the width (number of columns).
            

            width = int(image.shape[1] * resize_percentage/100)#width multiply by resize percentage / 100
            height = int(image.shape[0] * resize_percentage/100)


            #cv2.resize(): This function from OpenCV is used to resize images. It takes two main arguments:
            resized_image = cv2.resize(image, (width,height))


            cv2.imwrite(image_path, resized_image)

            return redirect("success")
    else:
        form = ImageResizerForm()#Creates an instance of the ImageResizeForm with no data. This prepares an empty form for the user to fill out.

    return render(request,'resize_image.html',{'form':form})#dictionary passing the form instances to the template context, this allowws teh template to access andf render the form fileds 

def success_view(request):
    return render(request, 'success.html')