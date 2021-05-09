from redes_sociais.sessoes import Section
from redes_sociais.sessoes import AlbumSection
from redes_sociais.sessoes import PublicationSection
from redes_sociais.sessoes import PersonalSection
from redes_sociais.sessoes import UploadCodeSection
import pytest


class TestSection:

    def test_class_album(self):
        objeto = AlbumSection()
        assert isinstance(objeto, Section)
        assert isinstance(objeto, AlbumSection)
        assert str(objeto) == "Sessão para fotos"
    
    def test_class_personal(self):
        objeto = PersonalSection()
        assert isinstance(objeto, Section)
        assert isinstance(objeto, PersonalSection)
        assert str(objeto) == 'Dados Pessoais'

    def test_class_publication(self):
        objeto = PublicationSection()
        assert isinstance(objeto, Section)
        assert isinstance(objeto, PublicationSection)
        assert str(objeto) == 'Sessão publicações'
    
    def test_class_upload_code(self):
        objeto = UploadCodeSection()
        assert isinstance(objeto, Section)
        assert isinstance(objeto, UploadCodeSection)
        assert str(objeto) == 'Sessão upload de códigos'
    
    def test_class_abstractClass(self):
        msg_erro = "Can't instantiate abstract class Section "
        msg_erro = msg_erro + "with abstract methods __repr__, __str__, sobre"
        with pytest.raises(TypeError) as error:
            Section()
        assert str(error.value) == msg_erro


