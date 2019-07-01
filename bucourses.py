import sys
import pandas
argument1 = str(sys.argv[1])
argument2 = str(sys.argv[2])
argument1year = int(argument1[:4])
argument2year = int(argument2[:4])
argument1semester = int(0);
argument2semester = int(0);
#This if block makes a integer conversion for given semester
if argument1[5:] == 'Fall':
    argument1semester = 1
elif argument1[5:] == 'Spring':
    argument1semester = 2
else:
    argument1semester = 3

if argument2[5:] == 'Fall':
    argument2semester = 1
elif argument2[5:] == 'Spring':
    argument2semester = 2
else:
    argument2semester = 3

#Creating a dataframe
MainData = pandas.DataFrame(columns=['Department', 'Course Code', 'Course Name'])
#This array stores every semester in it like "2018-Fall"
Semsester_Array = []
#To create csv table column name accurately we iterate over semesters and create a a column and save them to Semester_Array
iterateinsemestersforcolums = argument1semester
for year in range(argument1year, argument2year + 1):
    twocheck = True

    while twocheck:
        #Reconversion from integer to semester
        if iterateinsemestersforcolums == 1:
            semester = str(str(year) + "-Fall")
        elif iterateinsemestersforcolums == 2:
            semester = str(str(year) + "-Spring")
        else:
            semester = str(str(year) + "-Summer")
        #create column for that semester
        MainData[semester] = ''
        #save this semester to semester array
        Semsester_Array.append(semester)
        #Checks whether reached to last semester or not
        if year == argument2year and iterateinsemestersforcolums == argument2semester:
            break
        if iterateinsemestersforcolums == 3:
            iterateinsemestersforcolums = 1
        elif iterateinsemestersforcolums == 2:
            iterateinsemestersforcolums = 3
        else:
            iterateinsemestersforcolums = 2
            twocheck = False
#Lastly create total offerings column
MainData['Total Offerings'] = ''
#Colomns has been emerged

#Departmantal list arrays
Department_Long_List = ['MANAGEMENT', 'ASIAN+STUDIES', 'ASIAN+STUDIES+WITH+THESIS', 'ATATURK+INSTITUTE+FOR+MODERN+TURKISH+HISTORY', 'AUTOMOTIVE+ENGINEERING', 'MOLECULAR+BIOLOGY+%26+GENETICS', 'BUSINESS+INFORMATION+SYSTEMS', 'BIOMEDICAL+ENGINEERING', 'CRITICAL+AND+CULTURAL+STUDIES', 'CIVIL+ENGINEERING', 'CONSTRUCTION+ENGINEERING+AND+MANAGEMENT', 'COMPUTER+EDUCATION+%26+EDUCATIONAL+TECHNOLOGY', 'EDUCATIONAL+TECHNOLOGY', 'CHEMICAL+ENGINEERING', 'CHEMISTRY', 'COMPUTER+ENGINEERING', 'COGNITIVE+SCIENCE', 'COMPUTATIONAL+SCIENCE+%26+ENGINEERING', 'ECONOMICS', 'EDUCATIONAL+SCIENCES', 'ELECTRICAL+%26+ELECTRONICS+ENGINEERING', 'ECONOMICS+AND+FINANCE', 'ENVIRONMENTAL+SCIENCES', 'ENVIRONMENTAL+TECHNOLOGY', 'EARTHQUAKE+ENGINEERING', 'ENGINEERING+AND+TECHNOLOGY+MANAGEMENT', 'FINANCIAL+ENGINEERING', 'FOREIGN+LANGUAGE+EDUCATION', 'GEODESY', 'GEOPHYSICS', 'GUIDANCE+%26+PSYCHOLOGICAL+COUNSELING', 'HISTORY', 'HUMANITIES+COURSES+COORDINATOR', 'INDUSTRIAL+ENGINEERING', 'INTERNATIONAL+COMPETITION+AND+TRADE', 'CONFERENCE+INTERPRETING', 'INTERNATIONAL+TRADE', 'INTERNATIONAL+TRADE+MANAGEMENT', 'LINGUISTICS', 'WESTERN+LANGUAGES+%26+LITERATURES', 'LEARNING+SCIENCES', 'MATHEMATICS', 'MECHANICAL+ENGINEERING', 'MECHATRONICS+ENGINEERING', 'INTERNATIONAL+RELATIONS%3aTURKEY%2cEUROPE+AND+THE+MIDDLE+EAST', 'INTERNATIONAL+RELATIONS%3aTURKEY%2cEUROPE+AND+THE+MIDDLE+EAST+WITH+THESIS', 'MANAGEMENT+INFORMATION+SYSTEMS', 'FINE+ARTS', 'PHYSICAL+EDUCATION', 'PHILOSOPHY', 'PHYSICS', 'POLITICAL+SCIENCE%26INTERNATIONAL+RELATIONS', 'PRIMARY+EDUCATION', 'PSYCHOLOGY', 'MATHEMATICS+AND+SCIENCE+EDUCATION', 'SECONDARY+SCHOOL+SCIENCE+AND+MATHEMATICS+EDUCATION', 'SYSTEMS+%26+CONTROL+ENGINEERING', 'SOCIOLOGY', 'SOCIAL+POLICY+WITH+THESIS', 'SOFTWARE+ENGINEERING', 'SOFTWARE+ENGINEERING+WITH+THESIS', 'TURKISH+COURSES+COORDINATOR', 'TURKISH+LANGUAGE+%26+LITERATURE', 'TRANSLATION+AND+INTERPRETING+STUDIES', 'SUSTAINABLE+TOURISM+MANAGEMENT', 'TOURISM+ADMINISTRATION', 'TRANSLATION', 'EXECUTIVE+MBA', 'SCHOOL+OF+FOREIGN+LANGUAGES']
Department_Short_List = ['AD', 'ASIA', 'ASIA', 'ATA', 'AUTO', 'BIO', 'BIS', 'BM', 'CCS', 'CE', 'CEM', 'CET', 'CET', 'CHE', 'CHEM', 'CMPE', 'COGS', 'CSE', 'EC', 'ED', 'EE', 'EF', 'ENV', 'ENVT', 'EQE', 'ETM', 'FE', 'FLED', 'GED', 'GPH', 'GUID', 'HIST', 'HUM', 'IE', 'INCT', 'INT', 'INTT', 'INTT', 'LING', 'LL', 'LS', 'MATH', 'ME', 'MECA', 'MIR', 'MIR', 'MIS', 'PA', 'PE', 'PHIL', 'PHYS', 'POLS', 'PRED', 'PSY', 'SCED', 'SCED', 'SCO', 'SOC', 'SPL', 'SWE', 'SWE', 'TK', 'TKL', 'TR', 'TRM', 'TRM', 'WTR', 'XMBA', 'YADYOK']

#baseurl for schedules
baseurl = 'https://registration.boun.edu.tr/scripts/sch.asp?donem='
#This nested for loop iterates over departments semester by semester, creates a small tables for every departmend and add it to big table called main data
for depindex in range(0,len(Department_Short_List)):
    iteratesemester = argument1semester
    #Stores a departments data semester by semester
    DepartmentArray = []
    #Total instructor set for a department
    TotalInstructors = set()
    #Total course set for a department
    TotalCourses = set()
    #Total graduate course set for a department
    Graduate_All_Semesters = set()
    #Total undergraduate course set for a department
    UnderGraduate_All_Semesters = set()
    #The total number of undergraduate course gave in all semesters
    UnderGraduateTotalNumber = 0
    # The total number of graduate course gave in all semesters
    GraduateTotalNumber = 0
    # This dictionary stores course code as a key and set of instructors that give this course as a value
    Code_Instructor_Dictionary = dict()
    CodeNameDictionary = dict()
    # This dictionary stores course code as a key and set of semesters in that this course has been given  as a value
    Code_Semester_Dictionary = dict();

    #iterating semester by semester in a department
    for year in range(argument1year, argument2year + 1):
        #increment by one year after Fall
        twocheck = True

        while twocheck:
            #Preparing the year section in url
            if iteratesemester == 1:
                replace_year = str(str(year) + '/' + str(year + 1) + '-1')
                semester = str(str(year) + "-Fall")
            elif iteratesemester == 2:
                replace_year = str(str(year - 1) + '/' + str(year) + '-2')
                semester = str(str(year) + "-Spring")
            else:
                replace_year = str(str(year - 1) + '/' + str(year) + '-3')
                semester = str(str(year) + "-Summer")

            url = baseurl + replace_year
            #Adding the departmental things to url
            url = url + '&kisaadi=' + Department_Short_List[depindex] + '&bolum=' + Department_Long_List[depindex]
            #URL has been created

            #If url has nothing in it then this try section given an exception
            try:
                #reading table via pandas
                files = pandas.read_html(url)
                #TODO Instructorda STUFF STUFF var mı kontrol et
                #the set of instructors give course in this semester
                Instructors_Give_Course_Current_Semester = set()
                #set of courses opened this semester
                Courses_Opened_This_Semester = set()
                #the set of undergrade courses opened this semester
                UnderGraduateList = set()
                #the set of graduate courses opened this semester
                GraduateList = set()

                #iterating over courses
                for index in range(1, len(files[3][0])):
                    #if the course is LAB or PS then it cathces exception
                    try:
                        #Course code e.g. MATh102.01
                        course = files[3][0][index]
                        #adding the course the set without its section
                        Courses_Opened_This_Semester.add(course[:-3])
                        #if instructor of this course is not staff then add to instructor set
                        if files[3][5][index] != "STAFF STAFF":
                            Instructors_Give_Course_Current_Semester.add(files[3][5][index])
                        #Add this course to course name dictionary with its names
                        CodeNameDictionary[course[:-3]] = files[3][2][index]
                        #Adds instructor to set of instructors that gives this course to find distinct instructors lately
                        if course[:-3] not in Code_Instructor_Dictionary:
                            Code_Instructor_Dictionary[course[:-3]] = set()
                            if files[3][5][index] != "STAFF STAFF":
                                Code_Instructor_Dictionary[course[:-3]].add(files[3][5][index])
                        else:
                            if files[3][5][index] != "STAFF STAFF":
                                Code_Instructor_Dictionary[course[:-3]].add(files[3][5][index])
                        #Add this semester to the set of semester that this course has been given
                        if course[:-3] not in Code_Semester_Dictionary:
                            Code_Semester_Dictionary[course[:-3]] = set()
                            Code_Semester_Dictionary[course[:-3]].add(semester)
                        else:
                            Code_Semester_Dictionary[course[:-3]].add(semester)
                        #if the first digit of code is not integer than this try except adds this course to undergraduatelist
                        try:
                            #if the first digit is greater than 4 it adds to graduate else undergraduate
                            if (int(course[-6:-3][0]) > 4):
                                GraduateList.add(course[:-3])
                            else:
                                UnderGraduateList.add(course[:-3])
                        except:
                            UnderGraduateList.add(course[:-3])
                    except:
                        pass
                #The number of instructor gives course this semester
                instructornumber = len(Instructors_Give_Course_Current_Semester)
                #the number of gradute courses opened this semester
                Gnumber = len(GraduateList)
                #the number of undergradute courses opened this semester
                Unumber = len(UnderGraduateList)

                UnderGraduateTotalNumber += Unumber
                GraduateTotalNumber += Gnumber
                #Adding whole courses intructors to appropriate sets
                Graduate_All_Semesters = Graduate_All_Semesters.union(GraduateList)
                UnderGraduate_All_Semesters = UnderGraduate_All_Semesters.union(UnderGraduateList)
                TotalCourses = TotalCourses.union(Courses_Opened_This_Semester)
                TotalInstructors = TotalInstructors.union(Instructors_Give_Course_Current_Semester)
                #Add required values for creating a table to deparment array as this semester
                DepartmentArray.extend([[semester, list(Courses_Opened_This_Semester), Unumber, Gnumber, instructornumber]])
            except:
                #even if there is no course in that semester we add this semester to department array
                DepartmentArray.extend([[semester, list(), 0, 0, 0]])


            #Same rutine as above for iterating over semesters
            if year == argument2year and iteratesemester == argument2semester:
                break
            if iteratesemester == 3:
                iteratesemester = 1
            elif iteratesemester == 2:
                iteratesemester = 3
            else:
                iteratesemester = 2
                twocheck = False


    #Creating department table
    data = pandas.DataFrame(columns=['Course Code', 'Course Name'])
    data.at[0, 'Course Code'] = str("U" + str(len(UnderGraduate_All_Semesters)) + " " + "G" + str(len(Graduate_All_Semesters)))
    data.at[0, 'Total Offerings'] = str("U" + str(UnderGraduateTotalNumber) + " " + "G" + str(GraduateTotalNumber) + " " + "I" + str(len(TotalInstructors)))
    bolum = Department_Long_List[depindex]
    bolum = bolum.replace("+", " ")
    bolum = bolum.replace("%26", "&")
    bolum = bolum.replace("%3a", ":")
    bolum = bolum.replace("%2c", ",")
    data.at[0, 'Department'] = str(Department_Short_List[depindex] + '(' + bolum + ')')
    for index in range(len(DepartmentArray)):
        data.at[0, DepartmentArray[index][0]] = str(
            "U" + str(DepartmentArray[index][2]) + " " + "G" + str(DepartmentArray[index][3]) + " " + "I" + str(
                DepartmentArray[index][4]))
        i = 1
        for key, value in CodeNameDictionary.items():
            data.at[i, 'Course Code'] = key
            data.at[i, 'Course Name'] = value
            if key in DepartmentArray[index][1]:
                data.at[i, DepartmentArray[index][0]] = 'x'
            data.at[i, 'Total Offerings'] = str(
                str(len(Code_Semester_Dictionary[key])) + '/' + str(len(Code_Instructor_Dictionary[key])))

            i += 1
    header = data.head(1)
    remain = data[1:].copy()
    remain.sort_values(by='Course Code', inplace=True, ascending=True)
    header = header.append(remain, ignore_index=True)
    #Adding department table to Main table
    MainData = MainData.append(header, ignore_index=True, sort=True)
#Reoder the columns for wanted form
order_array = ['Department', 'Course Code', 'Course Name']
order_array.extend(Semsester_Array)
order_array.append('Total Offerings')
MainData = MainData.reindex(columns=order_array)
#Prints csv to console
print(MainData.to_csv(index=False))
