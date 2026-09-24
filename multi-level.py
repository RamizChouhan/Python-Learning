class Info:
    def CommonFields(self,Scourse,SCourseId):
        self.courseName = Scourse
        self.courseId = SCourseId


class Student(Info):
    def personDetail(self,name,rollNo):
        self.Sname = name
        self.SrollNo = rollNo

class ShowDetail(Student):#multi - level
    def Show(self):
        print("student course :",self.courseName)
        print("student courseId :",self.courseId)
        print("student name :",self.Sname)
        print("student RollNo :",self.SrollNo)
    


std1 = ShowDetail()
std1.CommonFields("bca",232)
std1.personDetail("karan",12)
std1.Show()
    
    
    
