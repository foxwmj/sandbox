del /Q /S /F "%USERPROFILE%\.vim"
rmdir /Q /S "%USERPROFILE%\.vim"
mkdir "%USERPROFILE%\.vim"
mkdir "%USERPROFILE%\.vim\bundle"
xcopy /S bundle "%USERPROFILE%\.vim\bundle"



mkdir "%USERPROFILE%\code_projs"
svn checkout https://mingjin-sandbox.googlecode.com/svn/branches/projs %USERPROFILE%\code_projs --username Mingjin.Wu@gmail.com
