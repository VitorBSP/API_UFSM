#%%
list_alunos = []
def get_last_id():
    if list_alunos:
        last_aluno = list_alunos[-1]
    else:
        return 1
    return last_aluno.id + 1

#%%
class Aluno:
    def __init__(self, curso, anoIngresso, anoEvasao, tipoEvasao):
        self.id = get_last_id()
        self._curso = curso
        self._anoIngresso = int(anoIngresso)
        self._anoEvasao = int(anoEvasao)
        self._tipoEvasao = int(tipoEvasao)
        self._is_publish = False #default is draft (rascunho)
    @property
    def data(self):
        return  {
                    'id' : self.id,
                    'curso' : self._curso,
                    'anoIngresso' : self._anoIngresso,
                    'anoEvasao' : self._anoEvasao,
                    'tipoEvasao' : self._tipoEvasao
                }
    @property
    def curso(self):
        return self._curso

    @curso.setter
    def curso(self, curso):
        self._curso = curso

    @property
    def anoIngresso(self):
        return self._anoIngresso

    @anoIngresso.setter
    def anoIngresso(self, anoIngresso):
        self._anoIngresso = anoIngresso
    
    @property
    def anoEvasao(self):
        return self._anoEvasao

    @anoEvasao.setter
    def anoEvasao(self, anoEvasao):
        self._anoEvasao = anoEvasao

    @property
    def tipoEvasao(self):
        return self._tipoEvasao

    @tipoEvasao.setter
    def tipoEvasao(self, tipoEvasao):
        self._tipoEvasao = tipoEvasao




    
# %%
