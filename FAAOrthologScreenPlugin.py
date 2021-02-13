import sys
import PyPluMA
class FAAOrthologScreenPlugin:
   def input(self, inputfile):
                infile = open(inputfile, 'r')
                self.parameters = dict()
                for line in infile:
                   contents = line.strip().split('\t')
                   self.parameters[contents[0]] = contents[1]
                self.firstfile = PyPluMA.prefix() + "/" + self.parameters["faa1"]
                self.secondfile = PyPluMA.prefix() + "/" + self.parameters["faa2"]
                self.thirdfile = PyPluMA.prefix() + "/" + self.parameters["ortholog"]

   def run(self):
      seq1 = set()
      seq2 = set()
      
      file3 = open(self.thirdfile, 'r')
      
      for line in file3:
         myline = line.strip()
         seqnames = myline.split('\t')
         seq1.add(seqnames[0])
         seq2.add(seqnames[1])
      
      
      self.lines1 = []
      file1 = open(self.firstfile, 'r')
      for line in file1:
         myline = line.strip()
         if (len(myline) > 0 and myline[0] == '>'):
           #contents = myline.split('\w')
           #myseq = contents[0][1:]
           myseq = myline[1:myline.find(' ')]
           if (myseq in seq1):
             self.lines1.append(myline)
             self.lines1.append(file1.readline().strip())
      
      self.lines2 = []
      file2 = open(self.secondfile, 'r')
      for line in file2:
         myline = line.strip()
         if (len(myline) > 0 and myline[0] == '>'):
           myseq = myline[1:myline.find(' ')]
           if (myseq in seq2):
              self.lines2.append(myline)
              self.lines2.append(file2.readline().strip())

   def output(self, outputfile):
      file4 = open(outputfile+"."+self.parameters["faa1"], 'w')
      for line in self.lines1:
         file4.write(line+"\n")
      
      file5 = open(outputfile+"."+self.parameters["faa2"], 'w')
      for line in self.lines2:
         file5.write(line+"\n")




