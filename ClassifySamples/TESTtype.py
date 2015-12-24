
import magic

f = magic.Magic(magic_file="C:\Program Files\GnuWin32\share\misc\magic")
file = "C:\\ClassifySamples\\20151109\\Vi\\3E28BA742A6423260F70B19A1CE6B607"
print f.from_buffer(file)
#f.from_buffer(open(file).read(1024))
