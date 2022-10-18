body = '''
    <br>
    <br>

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
'''
