from os import getcwd
import pgi
from random import choice
from pdb import set_trace
pgi.require_version('Gtk', '3.0')
from pgi.repository import Gtk  # noqa

d = {' ': 'espaço', '/': 'barra_direita', '\\': 'barra_esquerda',
     'sh': 'shift_esquerdo', 'sh2': 'shift_direito', '|': ['sh2', '\\'],
     '?': ['sh2', '/'], '[': 'colchete_esquerdo', ']': 'colchete_direito',
     '\n': 'enter', '{': ['sh', '['], '}': ['sh', ']'], '.': 'ponto',
     ';': 'ponto_virgula', ',': 'virgula', "'": 'aspas', '^': ['sh', '~'],
     '>': ['sh', '.'], ':': ['sh', ';'], '<': ['sh', ','], '"': ['sh', "'"],
     'ã': ['~', 'a'], 'õ': ['~', 'o'], 'â': ['~', 'sh', 'a'],
     'ê': ['~', 'sh', 'e'], 'ô': ['~', 'sh', 'o'], '=': 'igual',
     'á': ['´', 'a'], 'é': ['´', 'e'], 'í': ['´', 'i'], 'ó': ['´', 'o'],
     'ú': ['´', 'u'], '+': ['sh', '='], 'à': ['´', 'sh', 'a'],
     '_': ['sh', '-'], '-': 'menos', '!': ['sh', '1'], '@': ['sh2', '2'],
     '#': ['sh2', '3'], '$': ['sh2', '4'], '%': ['sh2', '5'], '¨': ['sh', '6'],
     '&': ['sh', '7'], '*': ['sh', '8'], '(': ['sh', '9'], ')': ['sh', '0'],
     '´': 'agudo', '~': 'til', '`': ['sh', '´']}

right_shift = 'qwertasdfgzxcvbãáâàêé'
left_shift = 'yuiophjklçnmíõôóú'
lr = right_shift + left_shift
dedos = ['\'"1qaz\\|', '2wsx', '3edc', '45rtfgvb', '0pç;:/?~^´`-_=+[]{}\n',
         '9ol>.', '8ik<,', '67yuhjnm']
jogo1 = 'abcdefghijklmnopqrstuvxwyzç,.;/~]´[\\'
jogo4 = 'ãêáõôéâíóúà`´~^' + 'ãêáõôéâíóúà'.upper()


def dr(item):
    """
    Função de recursividade que retorna um gerador do dicionário d.
    Este gerador tem a função de retornar parte do nome da imagem à ser
    carregada.
    """
    if isinstance(item, str) and item.lower() in d:
        return dr(d.get(item.lower(), item.lower()))
    elif isinstance(item, str):
        return item
    return (dr(a.lower()) for a in item)


def colorir(texto, posicao, cor='green1'):
    """
    Função que colore um texto em uma determinada posição.
    """
    texto = texto.split(' ')
    texto[posicao] = f'<span color="{cor}">{texto[posicao]}</span>'
    return ' '.join(texto)


class Janela:
    def __init__(self):
        # criando objetos.
        self._apagar = False
        self.cache = ''
        self.red_cache = ''
        self.prof_cache = ''
        self.builder = Gtk.Builder()
        self.local = getcwd()
        self.texto = []
        self.n_word_cache = -1
        self.jogo_escolhido = '0'

        # obtendo a interface glade
        self.builder.add_from_file('gwc.glade')

        # obtendo objetos.
        self._janela = self.builder.get_object('janela')
        self._0 = self.builder.get_object('zero')
        self._1 = self.builder.get_object('um')
        self._2 = self.builder.get_object('dois')
        self._3 = self.builder.get_object('tres')
        self._4 = self.builder.get_object('quatro')
        self._5 = self.builder.get_object('cinco')
        self._6 = self.builder.get_object('seis')
        self._7 = self.builder.get_object('sete')
        self._8 = self.builder.get_object('oito')
        self._9 = self.builder.get_object('nove')
        self._agudo = self.builder.get_object('agudo')
        self._alt_direito = self.builder.get_object('alt-direito')
        self._alt_esquerdo = self.builder.get_object('alt-esquerdo')
        self._a = self.builder.get_object('a')
        self._aspas = self.builder.get_object('aspas')
        self._backspace = self.builder.get_object('backspace')
        self._barra_direita = self.builder.get_object('barra-direita')
        self._barra_esquerda = self.builder.get_object('barra-esquerda')
        self._b = self.builder.get_object('b')
        self._capslock = self.builder.get_object('capslock')
        self._colchete_direito = self.builder.get_object('colchete-direito')
        self._colchete_esquerdo = self.builder.get_object('colchete-esquerdo')
        self._control_direito = self.builder.get_object('control-direito')
        self._control_esquerdo = self.builder.get_object('control-esquerdo')
        self._c = self.builder.get_object('c')
        self._ç = self.builder.get_object('ç')
        self._d = self.builder.get_object('d')
        self._enter = self.builder.get_object('enter')
        self._e = self.builder.get_object('e')
        self._esc = self.builder.get_object('esc')
        self._espaço = self.builder.get_object('espaço')
        self._f10 = self.builder.get_object('f10')
        self._f11 = self.builder.get_object('f11')
        self._f12 = self.builder.get_object('f12')
        self._f1 = self.builder.get_object('f1')
        self._f2 = self.builder.get_object('f2')
        self._f3 = self.builder.get_object('f3')
        self._f4 = self.builder.get_object('f4')
        self._f5 = self.builder.get_object('f5')
        self._f6 = self.builder.get_object('f6')
        self._f7 = self.builder.get_object('f7')
        self._f8 = self.builder.get_object('f8')
        self._f9 = self.builder.get_object('f9')
        self._f = self.builder.get_object('f')
        self._g = self.builder.get_object('g')
        self._h = self.builder.get_object('h')
        self._igual = self.builder.get_object('igual')
        self._i = self.builder.get_object('i')
        self._j = self.builder.get_object('j')
        self._k = self.builder.get_object('k')
        self._l = self.builder.get_object('l')
        self._menos = self.builder.get_object('menos')
        self._menu = self.builder.get_object('menu')
        self._m = self.builder.get_object('m')
        self._n = self.builder.get_object('n')
        self._o = self.builder.get_object('o')
        self._ponto = self.builder.get_object('ponto')
        self._ponto_virgula = self.builder.get_object('ponto-virgula')
        self._p = self.builder.get_object('p')
        self._q = self.builder.get_object('q')
        self._r = self.builder.get_object('r')
        self._shift_direito = self.builder.get_object('shift-direito')
        self._shift_esquerdo = self.builder.get_object('shift-esquerdo')
        self._s = self.builder.get_object('s')
        self._tab = self.builder.get_object('tab')
        self._til = self.builder.get_object('til')
        self._t = self.builder.get_object('t')
        self._u = self.builder.get_object('u')
        self._virgula = self.builder.get_object('virgula')
        self._v = self.builder.get_object('v')
        self._windows_direito = self.builder.get_object('windows-direito')
        self._windows_esquerdo = self.builder.get_object('windows-esquerdo')
        self._w = self.builder.get_object('w')
        self._x = self.builder.get_object('x')
        self._y = self.builder.get_object('y')
        self._z = self.builder.get_object('z')
        self._mostrar_maos = self.builder.get_object('mostrar_maos')
        self._maos = self.builder.get_object('maos')
        self._auto_apagar = self.builder.get_object('auto_apagar')
        self._professor = self.builder.get_object('professor')
        self._aluno = self.builder.get_object('aluno')
        self._aluno_texto = self.builder.get_object('texto_aluno')
        self._professor_texto = self.builder.get_object('texto_professor')
        self._arquivo = self.builder.get_object('arquivo')
        self._limpar_arquivo = self.builder.get_object('limpar_arquivo')
        self._popover = self.builder.get_object('popover')
        self._poplabel = self.builder.get_object('poplabel')
        self._jogos = self.builder.get_object('jogos')
        self._niveis = self.builder.get_object('niveis')
        self._area_arquivo = self.builder.get_object('area_arquivo')
        self._area_opcoes = self.builder.get_object('area_opcoes')

        # conectando objetos.
        self._janela.connect('destroy', Gtk.main_quit)
        self._mostrar_maos.connect('toggled', self.mostrar_imagem)
        self._aluno_texto.connect('end-user-action', self.aluno_digitando)
        self._professor_texto.connect('end-user-action',
                                      self.professor_digitando)
        self._auto_apagar.connect('toggled', self.auto_apagar_clicado)
        self._arquivo.connect('file-set', self.arquivo_escolhido)
        self._limpar_arquivo.connect('clicked', self.remover_arquivo)
        self._jogos.connect('changed', self.jogo_alterado)

        # configurando.
        self._janela.set_title('programa para aprender a digitar')

    def mostrar_imagem(self, widget):
        var = not self._maos.is_visible()
        self._maos.set_visible(var)

    def aluno_digitando(self, widget):
        prof = self._professor_texto
        texto = widget.get_text(widget.get_start_iter(), widget.get_end_iter(),
                                False)
        texto_professor = prof.get_text(prof.get_start_iter(),
                                        prof.get_end_iter(), False)
        if int(self._jogos.get_active_id()):
            return self._jogo(texto[-1:])
        self._normalizar_imagem()
        if texto_professor == texto:
            # apagar e talvez inserir texto do arquivo
            if not self.texto:
                self.remover_arquivo(None)
            else:
                prof.set_text(self.texto[0])
                self.professor_digitando(self._professor_texto)
                texto_professor = self.texto[0]
                texto = ''
                self.texto.pop(0)
                self.n_word_cache = -1
            widget.set_text('')
        elif texto_professor.startswith(texto) and texto_professor != texto:
            # imagem branca
            self.cache = texto_professor[len(texto):][0]
            self._definir_imagem(self.cache, 'brancas')
        elif not texto_professor.startswith(texto):
            # imagem vermelha
            if all([texto, self._apagar]):
                self._aluno.do_backspace(self._aluno)
            else:
                imagem = f'{self.local}/imagens/brancas/backspace.png'
                getattr(self, '_backspace').set_from_file(imagem)
            self.red_cache = texto[-1]
            self._definir_imagem(self.red_cache, 'vermelhas')
        self._colorir_texto(prof, texto_professor, texto)

    def professor_digitando(self, widget):
        prof = self._professor_texto
        texto_professor = prof.get_text(prof.get_start_iter(),
                                        prof.get_end_iter(),
                                        False)
        if len(texto_professor) == 1 or self.texto:
            self._normalizar_imagem()
            self.cache = self.prof_cache = texto_professor[0]
            self._definir_imagem(self.prof_cache, 'brancas')
        elif not texto_professor:
            self._normalizar_imagem()
            self._popover.hide()
            self._poplabel.set_text('')

    def auto_apagar_clicado(self, widget):
        self._apagar = not self._apagar

    def _normalizar_imagem(self):
        if self.cache:
            self._definir_imagem(self.cache, 'normais')
            self.cache = ''
        if self.red_cache:
            self._definir_imagem(self.red_cache, 'normais')
            self._definir_imagem('backspace', 'normais')
            self.red_cache = ''
        if self.prof_cache:
            self._definir_imagem(self.prof_cache, 'normais')
            self.prof_cache = ''

    def _definir_imagem(self, a, pasta):
        rd = dr(a)
        if isinstance(rd, str):
            rd = [rd]
        for b in rd:
            quadro = getattr(self, '_' + b.lower(), '')
            imagem = f'{self.local}/imagens/{pasta}/{b.lower()}.png'
            quadro and quadro.set_from_file(imagem)  # noqa
        if pasta == 'brancas':
            self._dedos(a, b, quadro)
        if all([a.isupper(), a.lower() in lr]):
            if b.lower() in right_shift:
              shift = 'direito'
            elif b.lower() in left_shift:
              shift = 'esquerdo'
            quadro = getattr(self, f'_shift_{shift}')
            imagem = f'{self.local}/imagens/{pasta}/shift_{shift}.png'
            quadro.set_from_file(imagem)

    def _dedos(self, a, b, quadro):
        for c in dedos:
            if b.lower() in c or a.lower() in c:
                texto = str(dedos.index(c) % 4 + 1)
                self._mostrar_popup(quadro, texto)
        if a == ' ':
            self._mostrar_popup(quadro, '5')

    def arquivo_escolhido(self, widget):
        with open(widget.get_filename(), 'r') as f:
            self.texto = f.readlines()
        self.aluno_digitando(self._aluno_texto)

    def remover_arquivo(self, widget):
        if self._arquivo.get_filename():
            self._arquivo.unselect_file(self._arquivo.get_file())
        # limpar o self.texto, aluno e professor, normalizar as imagens
        self._normalizar_imagem()
        self.texto = ''
        prof, aluno = self._professor_texto, self._aluno_texto
        prof.delete(prof.get_start_iter(), prof.get_end_iter())
        aluno.delete(aluno.get_start_iter(), aluno.get_end_iter())
        self._popover.hide()

    def _mostrar_popup(self, tecla, texto):
        self._popover.hide()
        self._poplabel.set_text('dedo: ' + texto)
        self._popover.set_relative_to(tecla)
        self._popover.show()

    def jogo_alterado(self, widget):
        self.remover_arquivo(None)
        self.jogo_escolhido = widget.get_active_id()
        if self.jogo_escolhido == '0':
            self._normalizar_imagem()
            self._niveis.set_visible(False)
            self._professor.set_sensitive(True)
            self._area_arquivo.set_sensitive(True)
            self._area_opcoes.set_sensitive(True)
        else:
            self._niveis.set_visible(True)
            self._professor.set_sensitive(False)
            self._area_arquivo.set_sensitive(False)
            self._area_opcoes.set_sensitive(False)
            self._auto_apagar.set_active(False)
            self._mostrar_maos.set_active(False)
        self.aluno_digitando(self._aluno_texto)

    def _colorir_texto(self, prof, texto_p, texto):
        condicoes = [bool(texto_p),
                     texto.count(' ') <= texto_p.count(' '),
                     texto_p.count(' ') > 0,
                     texto.count(' ') != self.n_word_cache]
        if all(condicoes):
            prof.set_text('')
            prof.insert_markup(prof.get_end_iter(),
                               colorir(texto_p, texto.count(' ')), -1)
            self.n_word_cache = texto.count(' ')

    def _jogo(self, texto):
        if texto == self.cache:
            self._normalizar_imagem()
            if self.jogo_escolhido == '1':
                self.cache = choice(jogo1)
                quadro = getattr(self, '_' + dr(self.cache), '')
                imagem = f'{self.local}/imagens/?/pequenas.png'
                quadro.set_from_file(imagem)
            elif self.jogo_escolhido == '4':
                self.cache = choice(jogo4)
                self._definir_imagem(self.cache, 'brancas')
                self._professor_texto.set_text(self.cache)
        self._aluno_texto.set_text(texto)


def main():
    app = Janela()  # noqa
    Gtk.main()


# mostrar imagem do procedimento com o shift? mostrar essa imagem no jogo?

# jogos:
# aperte a tecla antes que ela desapareça
# adivinhe a tecla
# tempo para digitar palavras com tread
