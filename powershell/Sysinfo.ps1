function getIP {
(Get-NetIPAddress).IPv4Address | Select-String "192*"
}

$IP = getIP
write-host("This machine's IP is $IP")

$USER = $env:USERNAME
$Host = GetHost
$HOST = GetHOST.Version
$DATE = Get-Date -Format "dddd MM/dd/yyyy"

Send-MailMessage -To "beckwilb@mail.uc.edu" -From "Luke.Beckwith93@gmail.com" -Subject "it3080c"
-Body $BODY -SmtpServer smtp.gmail.com -port 587 UseSsl -Credential (Get-Credential)

$BODY = "This machine's IP is $IP. User is $USER. Hostname is $Host. $HOST. Today's Date is $DATE."
