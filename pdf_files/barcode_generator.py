from barcode import Code128
from barcode.writer import ImageWriter
import os

def generate_barcode(data, filename):
    """
    Generate a Code128 barcode from text/URL and save it as an image.
    
    Args:
        data (str): Text or URL to encode in the barcode
        filename (str): Name of the output file (without extension)
    """
    # Create the barcode object
    barcode = Code128(data, writer=ImageWriter(format='PNG'))
    
    # Save the barcode as an image
    barcode.save(filename)

if __name__ == "__main__":
    # Example usage
    url = "https://example.com"  # Replace with your URL
    filename = "barcode"
    
    # Create output directory if it doesn't exist
    if not os.path.exists("barcodes"):
        os.makedirs("barcodes")
    
    # Generate and save the barcode
    generate_barcode(url, os.path.join("barcodes", filename))
    print(f"Barcode generated and saved as {filename}.png in the barcodes directory") 