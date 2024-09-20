from pypdf import PdfWriter, PdfReader

# Update this to whatever their level is
level = "5"

merger = PdfWriter()

# Open each of the individual sheets as a Reader
eg = PdfReader("in/Eglatine Grubb - Rogue " + level + ".pdf")
hector = PdfReader("in/Hector Lohikäärme - Paladin " + level + ".pdf")
storr = PdfReader("in/Storr Amberfine - Rogue " + level + ".pdf")
thrice = PdfReader("in/Thrice Parented - Fighter " + level + ".pdf")
ulysses = PdfReader("in/Ulysses Ilias - Bard " + level + ".pdf")

# Add a form_topname for the contents of each sheet so that content isn't overwritten
# Not doing this caused content in fields from the first sheet to be copied into correpsonding
# empty fields of later sheets.
eg.add_form_topname("eg")
hector.add_form_topname("hector")
storr.add_form_topname("storr")
thrice.add_form_topname("thrice")
ulysses.add_form_topname("ulysses")

# Adds the relevant pages for each char to the buffer
merger.append(fileobj=eg, pages=(0, 2))
merger.append(fileobj=hector, pages=(0, 3))
merger.append(fileobj=storr, pages=(0, 2))
merger.append(fileobj=thrice, pages=(0, 1))
merger.append(fileobj=ulysses, pages=(0, 3))

# Create output file
output = open("out/combined_characters2.pdf", "wb")

# Write content
merger.write(output)

# Close files
merger.close()
output.close()
