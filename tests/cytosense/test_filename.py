
path = "ATSO_flr24_photos 2022-03-02 17h09_Images.zip"
print(path)

# splitname = path.split("_")
# string_to_cut = splitname[len(splitname)-1]
# filename = path[:-len(string_to_cut)-1]
# print(filename)

def extract_name(path):
    splitname = path.split("_")
    string_to_cut = splitname[len(splitname)-1]
    filename = path[:-len(string_to_cut)-1]
    return filename

print(extract_name(path))