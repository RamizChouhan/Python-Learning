class Info:
    def CommonFields(self,Scourse,SCourseId):
        self.courseName = Scourse
        self.courseId = SCourseId


class Studnet(Info): #single
    def personDetail(self,name,rollNo):
        self.Sname = name
        self.SrollNo = rollNo

        print("student course :",self.courseName)
        print("student courseId :",self.courseId)
        print("student name :",self.Sname)
        print("student RollNo :",self.SrollNo)



std1 = Studnet()
std1.CommonFields("bca",232)
std1.personDetail("karan",12)
    
    
    
