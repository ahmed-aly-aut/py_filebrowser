import os, stat

__author__ = 'aaly'

class Filebrowser:
    """A simple example class"""

    def __init__(self):
        self.current_dir = "upload/"

    def out(self):
        paths = self.current_dir.split("/", 1)
        for i in range(0, len(paths)):
            self.current_dir += paths[i] + "/"

    def listElements(self):
        value=""
        for root, directories, files in os.walk(self.current_dir):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                if (os.path.isdir(filepath)):
                    value+= "<a href=\"javascript:opendir('" + filename + "/')\"><li><i class=\"icon-large icon-folder-open\"></i>" + filename + "</li></a>"
                else:
                    value+= "<a href=\"javascript:openfile('" + filepath + "')\"><li><i class=\"icon-large icon-picture\"></i>" + filename + "</li></a>"
        return value

    def create_dir(self, name):
        original_umask = os.umask(0)
        os.mkdir(name)
        os.chmod(name, stat.S_IRWXO)
        os.umask(original_umask)

    def open_file(self, file):
        return '<img class="anpassen" src="' + file + '" alt="' + file + '">'

    def getCurrentDir(self):
        return self.current_dir

    def setCurrentDir(self, current_dir):
        self.current_dir = current_dir