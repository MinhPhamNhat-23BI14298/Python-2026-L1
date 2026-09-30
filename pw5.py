import zipfile
import sys
import codecs

# Write info students mark management after finishing input
class Input:
  def __init__(self, stName="", stId="", stDob="", courses=""):
    self.stName = stName
    self.stId = stId
    self.stDob = stDob
    self.courses = courses
    self.student_list = []

  def inputSt(self, name, stId, stDob, courses):
    st = Input(name, stId, stDob, courses)
    self.student_list.append(st)

  def compress(self, nameFile):
    list_files = ['students.txt', 'courses.txt', 'marks.txt']

    compression = zipfile.ZIP_DEFLATED
    z = zipfile.ZipFile(nameFile, mode="w")

    for file in list_files:
      z.write(file, file, compress_type=compression)
    z.close()

  def decompress(self):
    try:
      with zipfile.ZipFile("students.dat", "r") as zip_ref:
        zip_ref.extractall("decompress")
    except Exception as e:
      print("students.dat not found")
      print("error :",e)

  def writeFile(self, st):
    for i in st:
      with open("students.txt", "a+", encoding='utf-8') as f1:
        f1.write("Name: "+i.stName+'\\n')
        f1.write("ID: "+i.stId+'\\n')
        f1.write("Date of birth: "+i.stDob+'\\n')
        f1.write("----------------------------\\n")

      with open('courses.txt', 'a+', encoding='utf-8') as f2:
        f2.write('Name: '+i.stName+'\\n')
        for j in i.courses:
          f2.write('Courses: '+j[0]+'\\n')
          f2.write('-------------------\\n')

      with open('marks.txt', 'a+', encoding='utf-8') as f3:
        f3.write('Name: '+i.stName+'\\n')
        for j in i.courses:
          f3.write(f'{j[0]}:'+j[1]+'\\n')
          f3.write('------------------\\n')
    f1.close()
    f2.close()
    f3.close()

  def deleteSt(self, name):
    for i in range(len(self.student_list)):
      if name == self.student_list[i].stName:
        print(f'student {name} is deleted')
        del self.student_list[i]


class Output:
  def __init__(self, student_list=''):
    self.student_list = student_list

  def listSt(self, student_list):
    for i in student_list:
      print(f"Name: {i.stName}")
      print(f"Id: {i.stId}")
      print(f"Date Of Birth: {i.stDob}")
      for j in range(len(i.courses)):
        print(f"Marks of {i.courses[j][0]}: ", i.courses[j][1])
      print("*************************")

# Input student info, course info and marks info
st = Input('' ,'', '' ,  '')
st.inputSt('Pham Nhat Minh', '23BI14298', '12/10/2005', (('Operating System', '13.5'), ('French Language', '12.7'), ('Numerical Methods', '17')))
st.inputSt('Vladimir Putin', '23BA14404', '25/09/2004', (('Operating System', '16.7'), ('French Language', '16.5'), ('Numerical Methods', '12')))
st.inputSt('Xi Jinping', '23BI14266', '21/04/2005', (('Operating System', '19.0'), ('French Language', '18.0'), ('Numerical Methods', '18.3')))

st.writeFile(st.student_list)

st.compress('students.dat')
st.decompress()

display = Output()
display.listSt(st.student_list)