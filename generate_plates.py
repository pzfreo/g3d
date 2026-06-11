from build123d import *

def generate_test_plates():
    # Plate dimensions
    width = 20
    length = 20
    # Heights from 2.5mm to 4mm with 0.5mm steps
    heights = [2.5, 3.0, 3.5, 4.0]

    for h in heights:
        # Create the plate
        # align=(Align.CENTER, Align.CENTER, Align.MIN) ensures the bottom is at Z=0
        with BuildPart() as plate:
            Box(width, length, h, align=(Align.CENTER, Align.CENTER, Align.MIN))
        
        # Export as STEP file
        filename = f"test_plate_{h}mm.step"
        export_step(plate.part, filename)
        print(f"Exported: {filename}")

        # Export as STL for slicing — the estampo cura image cannot
        # load STEP (no build123d inside the container)
        stl_filename = f"test_plate_{h}mm.stl"
        export_stl(plate.part, stl_filename)
        print(f"Exported: {stl_filename}")

if __name__ == "__main__":
    generate_test_plates()
