if (!$) {
    $ = django.jQuery;
}

$(document).ready(function () {
    function getCookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        console.log(decodedCookie);
        var ca = decodedCookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }

    $('.refresh').on('click', function () {
        // $('#my_results').css('display', 'none');
        let results = $('#my_results');
        let req = results.data('req');
        let url = results.data('url');
        let sessionid = results.data('sessionid');
        console.log(sessionid);
        $.ajax({
            url: req,
            method: 'GET',
            data: {
                url,
                sessionid
            },
            success: function (res) {
                results.empty();
                setTimeout(() => {
                    results.html(res.table);
                }, 500);
            }
        })
    })
});