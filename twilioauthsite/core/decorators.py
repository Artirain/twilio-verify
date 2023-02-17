from django.contrib.auth.decorators import user_passes_test

# этот декоратор использует ту же логику login_required, 
# но проверяет is_verified атрибут пользователя вместо is_authenticated, и перенаправляет на страницу /verify/ вместо /login/
def verification_required(f):
    return user_passes_test(lambda u: u.is_verified, login_url='/verify')(f)