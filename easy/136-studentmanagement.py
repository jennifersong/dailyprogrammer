#####################################################################
# 
#        ORIGINAL PROBLEM:
#        Calculate the average score on a series of assignments for 
#        each student in a given class and for the entire class.
#
#        For more information, see the original prompt at 
#        http://www.reddit.com/r/dailyprogrammer/comments/1kphtf/081313_challenge_136_easy_student_management/
#
#####################################################################
vars = raw_input().split()
n, m = int(vars[0]), int(vars[1])
students = {}

everything = [stuff for stuff in [raw_input().split() for x in range(n)]]
for row in everything:
	students[row[0]] = map(int, row[1:])
print round(float(sum([grade for lst in students.values() for grade in lst]))/(n*m), 2)
for student, scores in students.iteritems():
	print "{name} {average}".format(name=student, average=sum(scores)/float(m))
