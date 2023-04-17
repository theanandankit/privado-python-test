from .models import Comment

class PressInForm(Comment):
    def submit_form(self):
        print(self.user)