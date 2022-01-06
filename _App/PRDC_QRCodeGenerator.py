# QR Code Generator
# Author: Milos Petrasinovic <mpetrasinovic@prdc.rs>
# PR-DC, Republic of Serbia
# info@pr-dc.com
# --------------------
#
# Copyright (C) 2021 PR-DC <info@pr-dc.com>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as 
# published by the Free Software Foundation, either version 3 of the 
# License, or (at your option) any later version.
#  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#  
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ---------------

# Input variables
# --------------------
# Absolute path to Inkscape (https://inkscape.org/)
inkscapePath = 'C:/Program Files/Inkscape/bin/inkscape.exe' 
folder = 'qrcodes' # output folder
outFileName = 'QRCode_' # qr code file prefix
ids = range(1, 101) # ids range
url = 'https://pr-dc.com/some-page/?id=' # url to with id is appended

# Import packages
# --------------------
import os
import glob
from subprocess import Popen, PIPE, STDOUT
import qrcode
import qrcode.image.svg

# Global variables
# --------------------
directory = os.path.dirname(os.path.abspath(__file__))
outputfolder = os.path.join(directory, folder)

# Main function
# --------------------
def main():
    print("PR-DC QRCodeGenerator\n--------------------")
    if not os.path.exists(outputfolder):
        os.makedirs(outputfolder)
    
    print("Generating " + str(len(ids)) + " svg files")
    factory = qrcode.image.svg.SvgPathImage
    for i in ids:
        img = qrcode.make(url+str(i), image_factory=factory)
        img.save(folder+"/"+outFileName+"_"+str(i)+".svg")
    
    svgList = [f for f in glob.glob(folder+"/*.svg")]
    N = len(list(enumerate(svgList)))
    for idx, fileName in enumerate(svgList):
        fileNameNoExt = fileName[:-4]
        print("Generating file " + fileNameNoExt + ".pdf [" + \
          str(idx+1) + "/" + str(N) + "]")
        cmd = [inkscapePath,directory + '/' + fileNameNoExt + '.svg',
               '--actions=EditSelectAll;SelectionUnGroup;EditSelectAll;' \
               'SelectionUnion;FileSave;FileClose;',
               '--batch-process']
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        output = p.stdout.read()
        cmd = [inkscapePath, directory + '/' + fileNameNoExt + '.svg',
               '--export-area-drawing', '--export-type=pdf',
               '--export-filename=' + directory + '/' + fileNameNoExt + '.pdf']
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
        output = p.stdout.read()
    k = input("Press [Enter] to continue...")

# Run main function
if __name__ == '__main__':
    main()