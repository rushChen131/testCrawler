


function base64_encode(a) {
    return window.btoa(a)
}

function base64_decode(a) {
    return decode(a)
}

decode = function (input) {
        var output = "", chr1, chr2, chr3, enc1, enc2, enc3, enc4, i = 0;
        input = input.replace(/[^A-Za-z0-9\+\/\=]/g, "");
        while (i < input.length) {
            enc1 = this._keyStr.indexOf(input.charAt(i++));
            enc2 = this._keyStr.indexOf(input.charAt(i++));
            enc3 = this._keyStr.indexOf(input.charAt(i++));
            enc4 = this._keyStr.indexOf(input.charAt(i++));
            chr1 = (enc1 << 2) | (enc2 >> 4);
            chr2 = ((enc2 & 15) << 4) | (enc3 >> 2);
            chr3 = ((enc3 & 3) << 6) | enc4;
            output = output + String.fromCharCode(chr1);
            if (enc3 != 64) {
                output = output + String.fromCharCode(chr2);
            }
            if (enc4 != 64) {
                output = output + String.fromCharCode(chr3);
            }
        }
        output = this._utf8_decode(output);
        return output;
    }


function time() {
    var a = new Date().getTime();
    return parseInt(a / 1000)
}

function microtime(b) {
    var a = new Date().getTime();
    var c = parseInt(a / 1000);
    return b ? (a / 1000) : (a - (c * 1000)) / 1000 + " " + c
}

function chr(a) {
    return String.fromCharCode(a)
}

function ord(a) {
    return a.charCodeAt()
}

function md5(a) {
    return hex_md5(a)
}

var jd9tyaUwh3vvC3QncC1iwiApdgIzNvbiBk = function (n, t, e) {
    var f = "DECODE";
    var t = t ? t : "";
    var e = e ? e : 0;
    var r = 4;
    t = md5(t);
    var d = n;
    var p = md5(t.substr(0, 16));
    var o = md5(t.substr(16, 16));
    if (r) {
        if (f == "DECODE") {
            var m = n.substr(0, r)
        }
    } else {
        var m = ""
    }
    var c = p + md5(p + m);
    var l;
    if (f == "DECODE") {
        n = n.substr(r);
        l = base64_decode(n)
    }
    var k = new Array(256);
    for (var h = 0; h < 256; h++) {
        k[h] = h
    }
    var b = new Array();
    for (var h = 0; h < 256; h++) {
        b[h] = c.charCodeAt(h % c.length)
    }
    for (var g = h = 0; h < 256; h++) {
        g = (g + k[h] + b[h]) % 256;
        tmp = k[h];
        k[h] = k[g];
        k[g] = tmp
    }
    var u = "";
    l = l.split("");
    for (var q = g = h = 0; h < l.length; h++) {
        q = (q + 1) % 256;
        g = (g + k[q]) % 256;
        tmp = k[q];
        k[q] = k[g];
        k[g] = tmp;
        u += chr(ord(l[h]) ^ (k[(k[q] + k[g]) % 256]))
    }
    if (f == "DECODE") {
        if ((u.substr(0, 10) == 0 || u.substr(0, 10) - time() > 0) && u.substr(10, 16) == md5(u.substr(26) + o).substr(0, 16)) {
            u = u.substr(26)
        } else {
            u = ""
        }
        u = base64_decode(d)
    }
    return u
};

function jandan_load_img(b) {
    return jd9tyaUwh3vvC3QncC1iwiApdgIzNvbiBk(b, "6NY2R9dI5vLvnEw6fBZ6jSNINhbeSakZ");

}
