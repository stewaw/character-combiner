from pypdf import PdfWriter, PdfReader

# Update this to whatever their level is
level = "1"

merger = PdfWriter()

# Open each of the individual sheets as a Reader
eg = PdfReader("in/Eg " + level + ".pdf")
hector = PdfReader("in/Hector " + level + ".pdf")
storr = PdfReader("in/Storr " + level + ".pdf")
thrice = PdfReader("in/Thrice " + level + ".pdf")
ulysses = PdfReader("in/Ulysses " + level + ".pdf")

# Add a form_topname for the contents of each sheet so that content isn't overwritten
# Not doing this caused content in fields from the first sheet to be copied into correpsonding
# empty fields of later sheets.
eg.add_form_topname("eg")
hector.add_form_topname("hector")
storr.add_form_topname("storr")
thrice.add_form_topname("thrice")
ulysses.add_form_topname("ulysses")

# Adds the relevant pages for each char to the buffer
[merger.add_page(page) for page in eg.pages[:3]]
[merger.add_page(page) for page in hector.pages[:2]]
[merger.add_page(page) for page in storr.pages[:2]]
[merger.add_page(page) for page in thrice.pages[:2]]
[merger.add_page(page) for page in ulysses.pages[:3]]


# Create output file
output = open("out/combined_characters.pdf", "wb")

# Write content
merger.write(output)

# Close files
merger.close()
output.close()
