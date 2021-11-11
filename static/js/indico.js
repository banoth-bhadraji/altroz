alert("Welcome to Django javascript scripting language....")

var message = "Due to Security reasons, Right Click is not allowed !";

        function rtclickcheck(keyp) {
            if (navigator.appName == "Netscape" && keyp.which == 3) { alert(message); return false; }

            if (navigator.appVersion.indexOf("MSIE") != -1 && event.button == 2) { alert(message); return false; }
        }
        document.onmousedown = rtclickcheck;
