import execjs

jsfunction1 = 'function myFunction() {alert("You enter the wrong password")}'

execjs.compile(jsfunction1)