from redes_sociais.redes_sociais import Profile
from redes_sociais.redes_sociais import linkedin
from redes_sociais.redes_sociais import facebook
from redes_sociais.redes_sociais import GitHub
from redes_sociais.redes_sociais import Instagram
import pytest


class TestRedesSociais:

    def test_class_facebook(self):
        profile = facebook()
        assert isinstance(profile, Profile)
        assert isinstance(profile, facebook)
        assert len(profile.getSections()) == 2
    
    
    def test_class_linkedin(self):
        profile = linkedin()
        assert isinstance(profile, Profile)
        assert isinstance(profile, linkedin)
        assert len(profile.getSections()) == 2

    def test_class_github(self):
        profile = GitHub()
        assert isinstance(profile, Profile)
        assert isinstance(profile, GitHub)
        assert len(profile.getSections()) == 2

    def test_class_instagram(self):
        profile = Instagram()
        assert isinstance(profile, Profile)
        assert isinstance(profile, Instagram)
        assert len(profile.getSections()) == 2

    
    def test_class_abstractClass(self):
        msg_erro = "Can't instantiate abstract class Profile "
        msg_erro = msg_erro + "with abstract methods createProfile"
        with pytest.raises(TypeError) as error:
            Profile()
        assert str(error.value) == msg_erro
    