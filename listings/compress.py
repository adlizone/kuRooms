from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import mimetypes

def compress_image(image):
    img = Image.open(image)
    img_io = BytesIO()
    
    # Compress image by adjusting the quality and saving
    quality = 85  # Starting quality level
    while True:
        img.save(img_io, format=img.format, quality=quality)
        size = img_io.tell()  # Get size of the file in bytes
        if size <= 1 * 1024 * 1024 or quality == 1:  # Check if size is less than or equal to 1MB or quality is at its minimum
            break
        quality -= 5  # Decrease quality by 5 and try again
        img_io.seek(0)  # Reset BytesIO object
        
    img_io.seek(0)  # Go to the start of the BytesIO object

    # Guess the MIME type based on the file extension
    mime_type, _ = mimetypes.guess_type(image.name)
    if mime_type is None:
        mime_type = 'image/jpeg'  # Default to 'image/jpeg' if MIME type could not be determined

    # Create a new Django InMemoryUploadedFile
    new_image = InMemoryUploadedFile(
        img_io,
        'ImageField',
        image.name,
        mime_type,
        sys.getsizeof(img_io),
        None
    )

    return new_image
