from . import film_bp

@film_bp.route('/')
def film_bp():
    return "This is from film bp."