

def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    assert 1==1
    
    
def program_school(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
    programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list
    
    ##programs = GetPrograms.get_programs()
##print(programs)

programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)