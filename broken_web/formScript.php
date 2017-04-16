<?php

$customerName =$_POST['customerName'];
$email = $_POST['email'];
$message = $_POST['message'];

echo "CustomerName:".$customerName."<br/>";
echo "email:".$email."<br/>";
echo "message:".$message."<br/>";



// challenge level 1
// very easy challenge they simple need to enter 
// phpinfo(); and they get the points

// eval($message);


// challenge level 2
// here we increase the level of
// security and make them think a little harder 
// than normal their a few ways on how to do it.

// if ($message == "phpinfo();"){
//   $message = "";
//   echo "You need to try harder than that";
// }
// eval(urldecode($message));



// challenge level 3
// This challenge is very diffcult, only a jedi
// can solve this one

// $check_input = substr($message, -1);
// if ( $check_input == ";")
// {
//   $message = "";
//   echo "Nice Try";
// }
// else
// {
//   $message = urldecode($message);
//   if ( $message == "phpinfo();" )
//   {
//     $message = "";
//   }
//   else
//   {
//     $check_symbol = substr($message, 0, 1);
//     if ( $check_symbol == "$" )
//     {
//       $message = "";
//     }
//     eval($message);
//   }
// }


?>