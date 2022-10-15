
head1 = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- CSS only -->
    <link rel="stylesheet" href="static/site/css/style.css">
    <link rel="stylesheet" href="static/site/css/form.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"
        integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <title>
'''
  
head2 = '''</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <div class="container">
            <a class="navbar-brand" href="#">Logo</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link" aria-current="page" href="#">Producto</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Información</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Seguridad</a>
                    </li>
                </ul>
                <ul class="navbar-nav mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link">Ayuda</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <section class="ContentBackground divlogin">
        <article class="loginform">
            <div class="form-wrap">
                <div class="tabs">
                    <h3 class="login-tab"><a href="#login-tab-content">Ya soy miembro</a></h3>
                    <h3 class="signup-tab"><a class="active" href="#signup-tab-content">Quiero registrarme</a></h3>
                </div>
                <!--.tabs-->
                <div class="tabs-content">
                    <div id="signup-tab-content" class="active">
                        <form class="signup-form" action="" method="post">
                            <input type="email" class="input" id="user_email" autocomplete="off" placeholder="Email">
                            <input type="text" class="input" id="user_name" autocomplete="off" placeholder="Usuario">
                            <input type="password" class="input" id="user_pass" autocomplete="off"
                                placeholder="Contraseña">
                            <input type="submit" class="button" value="Registrar">
                        </form>
                        <!--.login-form-->
                        <div class="help-text">
                            <p>Al aceptar, aceptas nuestros</p>
                            <p><a href="#">Términos de servicio</a></p>
                        </div>
                        <!--.help-text-->
                    </div>
                    <!--.signup-tab-content-->
                    <div id="login-tab-content">
                        <form class="login-form" action="" method="post">
                            <input type="text" class="input" id="user_login" autocomplete="off"
                                placeholder="Email o Usuario">
                            <input type="password" class="input" id="user_pass" autocomplete="off"
                                placeholder="Contraseña">
                            <input type="checkbox" class="checkbox" id="remember_me">
                            <label for="remember_me">Recordarme</label>
                            <input type="submit" class="button" value="Enviar">
                        </form>
                        <!--.login-form-->
                        <div class="help-text">
                            <p><a href="#">Olvide mi contraseña</a></p>
                        </div>
                        <!--.help-text-->
                    </div>
                    <!--.login-tab-content-->
                </div>
                <!--.tabs-content-->
            </div>
            <!--.form-wrap-->
        </article>
    </section>
    <footer>
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-4 footer-column">
                    <ul class="nav flex-column">
                        <li class="nav-item">
                            <span class="footer-title">Productos</span>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link footlink" href="#">Producto 1</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link footlink" href="#">Producto 2</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link footlink" href="#">Planes & Precios</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link footlink" href="#">Preguntas Frecuentes</a>
                        </li>
                    </ul>
                </div>
                <div class="col-md-4 footer-column">
                    <ul class="nav flex-column">
                        <li class="nav-item">
                            <span class="footer-title">Compañia</span>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link footlink" href="#">Acerca de</a>
                        </li>
                    </ul>
                </div>
                <div class="col-md-4 footer-column">
                    <ul class="nav flex-column">
                        <li class="nav-item">
                            <span class="footer-title">Contacto & Soporte</span>
                        </li>
                        <li class="nav-item">
                            <span class="nav-link"><i class="fas fa-phone"></i>+54 11 2721 8440 </span>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link footlink" href="#"><i class="fas fa-comments"></i>Chat directo</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link footlink" href="#"><i class="fas fa-envelope"></i>Contacto</a>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="text-center"><i class="fas fa-ellipsis-h"></i></div>
            <div class="row text-center">
                <div class="col-md-4 box">
                    <span class="copyright quick-links">Copyright &copy; Match
                        <script>document.write(new Date().getFullYear())</script>
                    </span>
                </div>
                <div class="col-md-4 box">
                    <ul class="list-inline social-buttons">
                        <li class="list-inline-item">
                            <a href="#">
                                <i class="fab fa-twitter"></i>
                            </a>
                        </li>
                        <li class="list-inline-item">
                            <a href="#">
                                <i class="fab fa-facebook-f"></i>
                            </a>
                        </li>
                        <li class="list-inline-item">
                            <a href="#">
                                <i class="fab fa-linkedin-in"></i>
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="col-md-4 box">
                    <ul class="list-inline quick-links">
                        <li class="list-inline-item">
                            <a class=" footlink" href="#">Politicas de Privacidad</a>
                        </li>
                        <li class="list-inline-item">
                            <a class=" footlink" href="#">Términos y usos</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </footer>
</body>
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3"
    crossorigin="anonymous"></script>
<script src="https://code.jquery.com/jquery-3.6.1.min.js"
    integrity="sha256-o88AwQnZB+VDvE9tvIXrMQaPlFFSUTR+nldQm1LuPXQ=" crossorigin="anonymous"></script>
<script src="static/site/js/form.js"></script>
</html>
'''