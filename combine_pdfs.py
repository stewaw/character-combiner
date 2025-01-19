from pypdf import PdfWriter, PdfReader

# Update this to match character sheet version
version = "3"

merger = PdfWriter()

# Open each of the individual sheets as a Reader
eg = PdfReader("in/Eg v" + version + " - Character.pdf")
hector = PdfReader("in/Hector v" + version + " - Character.pdf")
storr = PdfReader("in/Storr v" + version + " - Character.pdf")
thrice = PdfReader("in/Thrice v" + version + " - Character.pdf")
ulysses = PdfReader("in/Ulysses v" + version + " - Character.pdf")
cheatsheet = PdfReader("in/CST Cheat Sheet - Cheat Sheet.pdf")

# Add a form_topname for the contents of each sheet so that content isn't overwritten
# Not doing this caused content in fields from the first sheet to be copied into
# correpsonding empty fields of later sheets.
eg.add_form_topname("eg")
hector.add_form_topname("hector")
storr.add_form_topname("storr")
thrice.add_form_topname("thrice")
ulysses.add_form_topname("ulysses")
cheatsheet.add_form_topname("cheatsheet")

# Create a dictionary of characters (PdfReader objects) paired with the number of pages they require
character_dict = {eg: 3, hector: 2, storr: 2, thrice: 2, ulysses: 3}


# Function which takes the merger object (PdfWriter) and the character_dict
# Loops through each item and adds the pages to the merger, followed by the
# pages from the Cheat Sheet
def add_sheets_to_buffer(merger, characters):
    for i, j in characters.items():
        [merger.add_page(page) for page in i.pages[:j]]
        [merger.add_page(page) for page in cheatsheet.pages[:2]]


# Call function passing merger and character_dict
add_sheets_to_buffer(merger, character_dict)

# Create output file
output = open("out/combined_characters.pdf", "wb")

# Write content
merger.write(output)

# Close files
merger.close()
output.close()
