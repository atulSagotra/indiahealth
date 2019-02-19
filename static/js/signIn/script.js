        function toggle(e){
            let z = e.innerHTML;
            if(z=='Sign Up'){
                document.getElementById('signin-form').style.display = 'none';
                document.getElementById('signup-form').style.display = 'block';
                document.querySelector('.sign-user-container-head').innerHTML = "Join Here";
                document.querySelector('.sign-user-container-p').innerHTML = "Welcome here! You can join our org. Hey there! To keep connected with us Please Signup here with your account.";
                e.innerHTML = 'Log In';
                document.querySelector('.create-account').innerHTML = 'Sign Up';
                document.querySelector('.sign-user-container-head-2').innerHTML = 'Already have <br>an account?'
                document.querySelector('.sign-user-container-head-2').style.marginTop = '95px';

            } else {
                document.getElementById('signin-form').style.display = 'block';
                document.getElementById('signup-form').style.display = 'none';
                document.querySelector('.sign-user-container-head').innerHTML = "Join Here";
                document.querySelector('.sign-user-container-p').innerHTML = "Welcome here! You can join our org. Please login here with your account. Please login here with your.";
                e.innerHTML = 'Sign Up';
                document.querySelector('.create-account').innerHTML = 'Log In';
                document.querySelector('.sign-user-container-head-2').innerHTML = 'New User?'
                document.querySelector('.sign-user-container-head-2').style.marginTop = '55px';
            }
        }
        function validateSignUp(){
            x = document.querySelector('#signup-pwd').value;
            y = document.querySelector('#cpwd').value;
            if(x!=y){
                window.alert('Passwords do not match');
                return false;
            }
            if(x.length<6){
                alert('Length too short.');
                return false;
            }
            //signUp();
            return true;
        }
        function validateSignIn(){
            x = document.querySelector('#signin-pwd').value;
            if(x.length<6){
                alert('Length too short.');
                return false;
            }
            //signIn();
            return false;
        }
