alunos = []
def get_last_id():
    if alunos:
        last_aluno = alunos[-1]
    else:
        return 1
    return last_aluno['id'] + 1


class Aluno:
    def __init__(self, curso, anoIngresso, anoEvasao, tipoEvasao):
        self.id = get_last_id()
        self.curso = curso
        self.anoIngresso = anoIngresso
        self.anoEvasao = anoEvasao
        self.tipoEvasao = tipoEvasao
        self.is_publish = False #default is draft (rascunho)
    @property
    def data(self):
        return  {
                    'id' : self.id,
                    'curso' : self.curso,
                    'anoIngresso' : self.anoIngresso,
                    'anoEvasao' : self.anoEvasao,
                    'tipoEvasao' : self.tipoEvasao
                }

    