<!doctype html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <title>Eugeni Bonet - crossreads</title>
  <meta charset="utf-8">
  <!--<link href='http://fonts.googleapis.com/css?family=Oldenburg' rel='stylesheet' type='text/css'>-->
  <link href='http://fonts.googleapis.com/css?family=Bitter' rel='stylesheet' type='text/css'>
  <link href="../css/style.css" rel="stylesheet">

</head>
<body>
<?php 
if(isset($_POST['email'])) {
    // EDIT THE 2 LINES BELOW AS REQUIRED 
    $email_to = "jaumeriereta@gmail.com";
    $email_subject = "Crossreads :: EugeniBonet :: FeedBack Form";
 
    function died($error) {
        // your error code can go here 
	// Catalan
	echo "<p>Catal&agrave;:<br />";
	echo "Ho sentim molt, per&ograve; hi ha hagut algun error en enviar el formulari.<br />";
	echo "Vegeu a sota aquests errors<br />";
	echo " ----</p>";

	echo "<p>Espa&ntilde;ol<br />";	
	echo "Lo sentimos, pero ha habido algun error al enviar el formulario.<br />";
	echo "Veanse abajo estos errores<br />";
	echo "----</p>";	


        echo "<p>We are very sorry, but there were error(s) found with the form you submitted.<br />";
        echo "These errors appear below.<br />";
        echo $error."<br /><br />";
	echo "<p><input Type=\"button\" VALUE=\"Enrrere / Atr&aacute;s / Back\" onClick=\"history.go(-1);return true;\"></p>";
        die();
    }
    // validation expected data exists 
    if(!isset($_POST['first_name']) ||
        !isset($_POST['last_name']) ||
        !isset($_POST['email']) ||
        !isset($_POST['telephone']) ||
        !isset($_POST['comments'])) {
        died('Ho sentim molt, per&ograve; hi ha hagut algun error en enviar el formulari.<br />Lo sentimos, pero ha habido algun error al enviar el formulario.  <br />We are sorry, but there appears to be a problem with the form you submitted.');       
    }
    $first_name = $_POST['first_name']; // required 
    $last_name = $_POST['last_name']; // required
    $email_from = $_POST['email']; // required
    $telephone = $_POST['telephone']; // not required
    $comments = $_POST['comments']; // required
     
    $error_message = "";
    $email_exp = '/^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/';
  if(!preg_match($email_exp,$email_from)) {
    $error_message .= 'L\'email no sembla correcte.<br />El email no parece correcto <br />The Email Address you entered does not appear to be valid.<br />';
  }
  $string_exp = "/^[A-Za-z .'-]+$/";
  if(!preg_match($string_exp,$first_name)) { 
    $error_message .= 'EL nom no sembla correcte<br />El nombre no parece correcto <br />The First Name you entered does not appear to be valid.<br />';
  }
  if(!preg_match($string_exp,$last_name)) {
    $error_message .= 'El cognom no sembla correcte<br />El apellido no parece correcto <br />The Last Name you entered does not appear to be valid.<br />';
  }
  if(strlen($comments) < 2) {
    $error_message .= 'El comentari no sembla correcte<br />El comentario no parece correcto<br />The Comments you entered do not appear to be valid.<br />';
  }
  if(strlen($error_message) > 0) {
    died($error_message);
  }
  $email_message = "Detalls del formulari a continuaci&oacute;: <br /><Detalles del formulario a continuaci&oacute;n:<br />Form details below.\n\n"; 
     
    function clean_string($string) {
      $bad = array("content-type","bcc:","to:","cc:","href");
      return str_replace($bad,"",$string);
    }
    $email_message .= "First Name: ".clean_string($first_name)."\n";
    $email_message .= "Last Name: ".clean_string($last_name)."\n";
    $email_message .= "Email: ".clean_string($email_from)."\n";
    $email_message .= "Telephone: ".clean_string($telephone)."\n"; 
    $email_message .= "Comments: ".clean_string($comments)."\n";

// create email headers
$headers = 'From: '.$email_from."\r\n".
'Reply-To: '.$email_from."\r\n" .
'X-Mailer: PHP/' . phpversion();
@mail($email_to, $email_subject, $email_message, $headers);  
?>
<!-- include your own success html here -->
<p>Gr&agrave;cies per contactar-nos. Et contestarem ben aviat.</p>
<p>Gracias por contactarnos. Te contestaremos muy pronto.</p>
<p>Thank you for contacting us. We will be in touch with you very soon.</p>
<?php
}
?>
</body>
</html>
