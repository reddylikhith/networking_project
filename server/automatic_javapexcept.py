import pexpect as px
def install_java():
    child=px.spawn("sudo apt-get update")
    child.expect(".*password.*")
    child.sendline("Liki@123")
    print(child.before.decode("utf-8"))
    ch=px.spawn("sudo apt install opendjk-18-jre-headless")
    ch.expect("*password.*")
    child.sendline("Liki@123")
    ch.expect("do you .*")
    ch.sendline("yes")
    #ch.except(px,EOF)
    print(child.before.decode("utf-8"))
if __name__=="__main__":
    install_java()