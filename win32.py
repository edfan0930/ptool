from PIL import Image, ImageWin
import win32print
import win32ui

# Open the image
image_path = "takeout.jpg"
image = Image.open(image_path)

# Get the default printer name
printer_name = win32print.GetDefaultPrinter()

# Print the image
printer_dc = win32ui.CreateDC()
printer_dc.CreatePrinterDC(printer_name)
printer_dc.StartDoc(image_path)
printer_dc.StartPage()

dib = ImageWin.Dib(image)
dib.draw(printer_dc.GetHandleOutput(), (0, 0, image.width, image.height))

printer_dc.EndPage()
printer_dc.EndDoc()
printer_dc.DeleteDC()
