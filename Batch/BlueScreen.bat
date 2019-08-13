@Echo Off
:Be
echo Welcome to the Windows Blue Screen Troubleshooter! (Credits go to Nathan Knight)
echo Before we get started please make sure your device can boot up correctly!
PAUSE
:c
echo Next, please type the error code you had below (It would look like something like this 0x0000001 (note: just type it in))
set /p code=
if %code%==0 (
echo This BSOD means that there has been a mismatch in the APC state index. BSOD error code 0x00000001 may also show "APC_INDEX_MISMATCH" on the same blue screen.
)

