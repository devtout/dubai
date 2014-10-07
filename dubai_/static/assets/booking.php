<?php

if(!$_POST) exit;

// Email verification, do not edit.
function isEmail($email ) {
	return(preg_match("/^[-_.[:alnum:]]+@((([[:alnum:]]|[[:alnum:]][[:alnum:]-]*[[:alnum:]])\.)+(ad|ae|aero|af|ag|ai|al|am|an|ao|aq|ar|arpa|as|at|au|aw|az|ba|bb|bd|be|bf|bg|bh|bi|biz|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|com|coop|cr|cs|cu|cv|cx|cy|cz|de|dj|dk|dm|do|dz|ec|edu|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gh|gi|gl|gm|gn|gov|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|in|info|int|io|iq|ir|is|it|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mil|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|museum|mv|mw|mx|my|mz|na|name|nc|ne|net|nf|ng|ni|nl|no|np|nr|nt|nu|nz|om|org|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|pro|ps|pt|pw|py|qa|re|ro|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|sk|sl|sm|sn|so|sr|st|su|sv|sy|sz|tc|td|tf|tg|th|tj|tk|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|um|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)$|(([0-9][0-9]?|[0-1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5])\.){3}([0-9][0-9]?|[0-1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5]))$/i",$email ));
}

if (!defined("PHP_EOL")) define("PHP_EOL", "\r\n");

$checkin     = $_POST['checkin'];
$checkout    = $_POST['checkout'];
$guest    = $_POST['guest'];
$child   = $_POST['child'];
$rooms= $_POST['rooms'];
$name= $_POST['name'];
$email= $_POST['email'];
$phone= $_POST['phone'];
$verify_booking= $_POST['verify_booking'];
	

if(trim($checkin) == '') {
	echo '<div class="error_message"><i class="icon-attention"></i> Enter a Check in date.</div>';
	exit();
} else if(trim($checkout) == '') {
	echo '<div class="error_message"><i class="icon-attention"></i> Enter a Check out date.</div>';
	exit();
} else if(trim($guest) == '') {
	echo '<div class="error_message"><i class="icon-attention"></i> Enter number of Guests.</div>';
	exit();
} else if(trim($child) == '') {
	echo '<div class="error_message"><i class="icon-attention"></i> Enter number of Child.</div>';
	exit();
} else if(trim($rooms) == '') {
	echo '<div class="error_message"><i class="icon-attention"></i> Enter room type.</div>';
	exit();
} else if(trim($name) == '') {
	echo '<div class="error_message"><i class="icon-attention"></i> Enter your Name.</div>';
	exit();
} else if(trim($email) == '') {
	echo '<div class="error_message"><i class="icon-attention"></i> Enter a valid email address.</div>';
	exit();
} else if(!isEmail($email)) {
	echo '<div class="error_message"><i class="icon-attention"></i> Invalid e-mail address, try again.</div>';
	exit();
	} else if(trim($phone) == '') {
	echo '<div class="error_message"><i class="icon-attention"></i> Enter a valid phone number.</div>';
	exit();
} else if(!is_numeric($phone)) {
	echo '<div class="error_message"><i class="icon-attention"></i> Phone number can only contain numbers.</div>';
	exit();
} else if(!isset($verify_booking) || trim($verify_booking) == '') {
	echo '<div class="error_message"><i class="icon-attention"></i> Enter the verification number.</div>';
	exit();
} else if(trim($verify_booking) != '4') {
	echo '<div class="error_message"><i class="icon-attention"></i> The verification number is incorrect.</div>';
	exit();
}


//$address = "HERE your email address";
$address = "test@ansonika.com";


// Below the subject of the email
$e_subject = 'Booking request from ' . $name . '.';

// You can change this if you feel that you need to.
$e_body = "You have been contacted by $name " . PHP_EOL . PHP_EOL;
$e_content = "\nRequest of availability\n\nCheck in date: $checkin\nCheck out date: $checkout\nNumber of guests: $guest\nNumber of child: $child\nRoom type: $rooms" . PHP_EOL . PHP_EOL;
$e_reply = "You can contact $name via $email or $phone. ";

$msg = wordwrap( $e_body . $e_content . $e_reply, 70 );

$headers = "From: $email" . PHP_EOL;
$headers .= "Reply-To: $email" . PHP_EOL;
$headers .= "MIME-Version: 1.0" . PHP_EOL;
$headers .= "Content-type: text/plain; charset=utf-8" . PHP_EOL;
$headers .= "Content-Transfer-Encoding: quoted-printable" . PHP_EOL;

$user = "$email";
$usersubject = "Thank You";
$userheaders = "From: booking@paradise.com\n";
$usermessage = "Thank you for contact PARADISE HOTEL. We will reply shortly with a confirmation of your booking. Here a summary of your request: \n $e_content\n Call 0034 434324  for further information.";
mail($user,$usersubject,$usermessage,$userheaders);

if(mail($address, $e_subject, $msg, $headers)) {

	// Success message
	echo "<div id='success_page' style='padding:20px;text-align:center'>";
	echo "<strong >Email Sent.</strong>";
	echo "Thank you <strong>$name</strong>,<br> your booking request has been submitted. We will contact you shortly in order to confirm your booking.";
	echo "</div>";

} else {

	echo 'ERROR!';

}
